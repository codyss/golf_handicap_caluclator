#this app calculates a players handicap based on score entered

import json
import os
from pymongo import MongoClient

class Score(object):
  def __init__(self, esc_score, date, slope_rating, course_rating):
    self.esc_score = esc_score
    self.date = date
    self.slope = slope_rating
    self.course = course_rating
    self.differential = (esc_score-course_rating)*115/slope_rating 

class Course(object):
  def __init__(self, slope_rating, course_rating):
    self.slope_rating = slope_rating
    self.course_rating = course_rating


class Player(object):
  def __init__(self, name, bday, scores=[], handicap=18):
    self.name = name
    self.bday = bday
    self.scores = scores
    self.handicap = handicap

  def post(self, Score):
    self.scores.append(Score)
    self.update_handicap()

  def update_handicap(self):
    self.handicap = calculate_handicap(self.scores)

  def show_handicap(self):
    print round(self.handicap,2)

  def delete(self, Score):
    self.scores.remove(Score)

  # method that imports a dictionary into an object
  # needs to be updated to include new dictionary data 
  def load_old_scores(self, old_scores):
    for i in old_scores:
      esc_score = old_scores[i]['esc_score']
      date = old_scores[i]['date']
      slope_rating = old_scores[i]['slope_rating']
      course_rating = old_scores[i]['course_rating']
      score_to_post = Score(esc_score, date, slope_rating, course_rating)
      self.post(score_to_post)
      

def calculate_handicap(score_list):
  score_list.sort(key = lambda score: score.date, reverse=True)
  rounds = 0
  total_differential = 0.0
  #use only the most recent 20 scores 
  scores_used = score_list[0:20]
  scores_used.sort(key = lambda score: score.differential)
  for i in scores_used:
    rounds += 1
    total_differential += i.differential
  return total_differential / rounds

def dict_player(Player):
  """function creates a dictionary of the player's scores to store in a file"""
  storage = {}
  player_data = {}
  player_data[Player.name] = storage
  storage['name'] = Player.name
  storage['bday'] = Player.bday
  storage['scores'] = {}
  count = 1
  for i in Player.scores:
    storage['scores']['score' + str(count)] = {'date':i.date, 'esc_score':i.esc_score, 'slope_rating':i.slope, 'course_rating':i.course}
    count += 1
  return player_data 

def userprompt():
  name = raw_input("What's your name?")
  bday = int(raw_input("What is your birthday? (MMDD)"))
  player = Player(name, bday)
  client = MongoClient()
  db = client.test
  #load saved scores
  #give a player a ghin number (using bday) to identify and save scores  - use bday
  #load needs to incorporate mongo db instead of file
  f= open('handicap_data.json','r')
  if os.stat('handicap_data.json').st_size == 0:
    all_scores = {}
  else: 
    all_scores = json.load(f)
  scores_to_load = {}
  for i, v in all_scores.iteritems():
    if v['bday'] == bday:
      scores_to_load = v['scores']
      player.load_old_scores(scores_to_load)
  f.close()
  if scores_to_load != {}:
    print "scores loaded"

 
  while True:
    # prompt the user for what they would like to do
    choice = raw_input("What do you want to do? A) post B) check handicap C) View scores D) Delete E) save g)quit")
    # Posting
    if choice.lower() == 'a':
      score = int(raw_input("what'd you shoot?"))
      date = int(raw_input("When did you play. In MDDYYYY format"))
      slope_rating = int(raw_input("What was the slope?"))
      course_rating = float(raw_input("What was the course rating?"))
      inputted_score = Score(score, date, slope_rating, course_rating)
      player.post(inputted_score)  
    
    #check handicap
    elif choice.lower() == 'b':
      player.show_handicap()   
    

    #see scores
    elif choice.lower() == 'c':
      if len(player.scores) > 0:
        print "score: "
        for i in player.scores:
          print "%i on %i" %(i.esc_score, i.date)
      else:
        print "No scores, enter one!"


    #delete a score
    elif choice.lower() == 'd':
      print "Which score would you like to delete?"
      for i in player.scores:
        print "%i on %s" % (i.esc_score, i.date)
      print "Enter the date shown"
      date_of_score_to_delete = int(raw_input().strip())
      for i in player.scores:
        if i.date == date_of_score_to_delete:
          player.delete(i)
    
    #save scores into the file with all the scores
    #there really should be no save - posting should save the score 
    #mongo db started... data is added, but now there are multiple records
    elif choice.lower() == 'e':
      if all_scores == {}:
        all_scores = dict_player(player)
      else:
        player_new_scores = dict_player(player)
        all_scores[player.name] = player_new_scores[player.name]
      f= open('handicap_data.json','w')
      json.dump(all_scores, f)
      f.close()
      result = db.handicap_data.insert_one(all_scores)

    #quit
    elif choice.lower() == 'g':
      break
    else:
      choice = raw_input("Please make a valid choice!")

