keep_playing = True

def main ():
    score = 300
    deck = 13
    play_again= ""

    if score > 0 and deck > 0:
        play_again = input("Play again? [y/n] ")
        print ()

        if play_again == "n":
            global keep_playing 
            keep_playing = False
            print ("\nThank you for playing.")

    else:
        print ("Game Over.")
        keep_playing = False

while keep_playing:
    if __name__ == "__main__":
        main ()