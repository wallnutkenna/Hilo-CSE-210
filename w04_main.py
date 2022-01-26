
def main ():
    
    score = 300
    deck = 13

    # print (f"The card is: 9")
    # print ("Higher or lower? [h/l] L")
    # print (f"Next card was: 5")
    score += 100

    if score > 0 and deck != 0:
        play_again = input("Play again? [y/n] ")
        print ()

    if play_again == "y":
        keep_playing = True

while keep_playing:
    if __name__ == "__main__":
        main ()