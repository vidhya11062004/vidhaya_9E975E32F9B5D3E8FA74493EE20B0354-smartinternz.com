'''Implement a class called player that represent a circket player. The player class should have a
method called play() which prints "The player is playing circket. Derive two classes, Batsman and
Bowler, from the player class. Override the play() method in each derived class to print "The batsman
is batting" and "The bowler is bowling ",respectively. Write a  program to create objects of both the
Batsman and Bowler classes and call the play() method for each   object,'''


# Define the base class player
class player:
  def play(self):
      print("The player is player cricket.")

# Define the drived class Batsman
class Batsman(player):
  def play(self):
      print ("The batsman is batting.")

  # Define the derived class bowler
class Bowler(player):
    def player(self): 
        print ("The bowler is bowling.")

# create object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object
batsman.play()
bowler.play()