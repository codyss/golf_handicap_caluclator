#this app calculates a players handicap based on score entered


class Score(object):
  def __init__(self, esc_score, date, slope_rating, course_rating):
    self.esc_score = esc_score
    self.date = date
    self.slope = slope_rating
    self.course = course_rating
    self.differential = (esc_score-course_rating)*115/slope_rating 

class Player(object):
  def __init__(self, name, scores=[], handicap=18):
    self.name = name
    self.scores = scores
    self.handicap = handicap

  def post(self, Score):
    self.scores.append(Score)
    self.update_handicap()

  def update_handicap(self):
    self.handicap = calculate_handicap(self.scores)

  def show_handicap(self):
    print self.handicap

def calculate_handicap(score_list):
  sorted(score_list, key = lambda score: score.date, reverse=True)
  rounds = 0
  total_differential = 0
  #needs to do just last 20 scores
  for i in score_list:
    rounds += 1
    total_differential += i.differential
  return total_differential / rounds  

def userprompt():
  name = raw_input("What's your name?")
  player = Player(name)

  choice = raw_input("What do you want to do? A) post B) check handicap C) View scores D) quit")
  while choice.lower() != 'd':
    if choice.lower() == 'a':
      score = int(raw_input("what'd you shoot?"))
      date = int(raw_input("When did you play. In MDDYYYY format"))
      slope_rating = int(raw_input("What was the slope?"))
      course_rating = float(raw_input("What was the course rating?"))
      inputted_score = Score(score, date, slope_rating, course_rating)
      player.post(inputted_score)
      choice = raw_input("What do you want to do? A) post B) check handicap C) View scores D) quit")
    elif choice.lower() == 'b':
      round(player.show_handicap(),2)
      choice = raw_input("What do you want to do? A) post B) check handicap C) View scores D) quit")
    elif choice.lower() == 'c':
      for i in player.scores:
        print "score: %i, " %i.esc_score
        print ""
      choice = raw_input("What do you want to do? A) post B) check handicap C) View scores D) quit")

userprompt()
#raw_input to ask what the person wants to do: post, check handicap, etc.
#potentially add a dictionary/table with the data on a set of courses to use








