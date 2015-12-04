#this app calculates a players handicap based on score entered


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

  def delete(self, Score):
    self.scores.remove(Score)

def calculate_handicap(score_list):
  score_list.sort(key = lambda score: score.date, reverse=True)
  rounds = 0
  total_differential = 0
  #use only the most recent 20 scores 
  scores_used = score_list[0:20]
  scores_used.sort(key = lambda score: score.differential)
    for i in score_used:
      rounds += 1
      total_differential += i.differential
  return total_differential / rounds  

