#this app calculates a players handicap based on score entered

import handicap
import json

def userprompt():
  name = raw_input("What's your name?")
  player = handicap.Player(name)

 
  while True:
    # prompt the user for what they would like to do
    choice = raw_input("What do you want to do? A) post B) check handicap C) View scores D) Delete E) save f) load g)quit")
    # Posting
    if choice.lower() == 'a':
      score = int(raw_input("what'd you shoot?"))
      date = int(raw_input("When did you play. In MDDYYYY format"))
      slope_rating = int(raw_input("What was the slope?"))
      course_rating = float(raw_input("What was the course rating?"))
      inputted_score = handicap.Score(score, date, slope_rating, course_rating)
      player.post(inputted_score)  
    
    #check handicap
    elif choice.lower() == 'b':
      player.show_handicap()   
    

    #see scores
    elif choice.lower() == 'c':
      if len(player.scores) > 0:
        for i in player.scores:
          print "score: %i, " %i.esc_score
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
    
    #save scores
    elif choice.lower() == 'e':
      dict_to_save = handicap.dict_player(player)
      f= open('handicap_data.json','w')
      json.dump(dict_to_save, f)
      f.close()

    #load saved scores
    elif choice.lower() == 'f':
      f= open('handicap_data.json','r')
      scores_to_load = json.load(f)
      player.load_old_scores(scores_to_load)
      f.close()

    #quit
    elif choice.lower() == 'g':
      break
    else:
      choice = raw_input("Please make a valid choice!")

userprompt()
#raw_input to ask what the person wants to do: post, check handicap, etc.
#potentially add a dictionary/table with the data on a set of courses to use








