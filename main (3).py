#Define the player class
class player:
  def play(self):
    print("The player is playing cricket.")
#Define the Batsman class,derived from player
class Batsman(player):
    def play(self):
        print("The batsman is batting.")
#Define the Bowlerclass,derived from player
class Bowler(player):
    def play(self):
        print("The bowler is bowling.")
 #create objects of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()
#call the play() method for each object 
batsman.play()
bowler.play()