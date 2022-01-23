
class game_loop:
    """This class will make the game to repeat in a loop until the player
    doesn't want to continue, or until 0 points of score are reached.
    """

    def __init__(self):
        """A special method called a Constructor, that iniciates one 
        attribute. It is invoked using the class name followed by a 
        parenthesis.
        """
        self.play_again = True

    def ask_user (self):
        """If the total score is more than 0 points, ask if the player 
        wants to continue playing and repeat the game.
        """
        keep_playing = input("Play again? [y/n] ")
        self.play_again = (keep_playing == "y")
