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
    print round(self.handicap,2)

  def delete(self, Score):
    self.scores.remove(Score)

  # method that imports a dictionary into an object
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


# have a function that creates a dictionary of the player's scores to store the info 

def dict_player(Player):
  storage = {}
  storage['name'] = Player.name
  count = 1
  for i in Player.scores:
    storage['score' + str(count)] = {'date':i.date, 'esc_score':i.esc_score, 'slope_rating':i.slope_rating, 'course_rating':i.course_rating}
    count += 1
  print storage
  return storage 



