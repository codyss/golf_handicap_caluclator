#this app calculates a players handicap based on score entered

import handicap

def userprompt():
  name = raw_input("What's your name?")
  player = handicap.Player(name)

 
  while True:
    choice = raw_input("What do you want to do? A) post B) check handicap C) View scores D) Delete E) quit")
    if choice.lower() == 'a':
      score = int(raw_input("what'd you shoot?"))
      date = int(raw_input("When did you play. In MDDYYYY format"))
      slope_rating = int(raw_input("What was the slope?"))
      course_rating = float(raw_input("What was the course rating?"))
      inputted_score = handicap.Score(score, date, slope_rating, course_rating)
      player.post(inputted_score)  
    elif choice.lower() == 'b':
      round(player.show_handicap(),2)   
    elif choice.lower() == 'c':
      for i in player.scores:
        print "score: %i, " %i.esc_score
        print ""
    elif choice.lower() == 'd':
      print "Which score would you like to delete?"
      for i in player.scores:
        print "%i on %s" % (i.esc_score, i.date)
      print "Enter the date shown"
      date_of_score_to_delete = int(raw_input())
      for i in player.scores:
        if i.date == date_of_score_to_delete.strip():
          player.delete(i)
    elif choice.lower() == 'e':
      break
    else:
      choice = raw_input("Please make a valid choice!")

userprompt()
#raw_input to ask what the person wants to do: post, check handicap, etc.
#potentially add a dictionary/table with the data on a set of courses to use








