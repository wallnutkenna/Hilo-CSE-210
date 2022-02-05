"""McKenna Wall, Ruth Ale Bravo, Alejandro Vinay
"""

keep_playing = True
import random

def main ():
    play_game()

class Deck:
    # Creates a deck with 52 cards and 4 suits with 13 cards in each suit 
    def __init__(self):
        self.card_deck = []
        #creates the deck with the cards in it 
        for i in range(0,13):
            self.card_deck.append(['heart',i+1])
        for i in range(0,13):
            self.card_deck.append(['clover',i+1])
        for i in range(0,13):
            self.card_deck.append(['spade',i+1])
        for i in range(0,13):
            self.card_deck.append(['diamond',i+1])
            

    def remaining_cards(self):
        return len(self.card_deck)

    def show_number(self):
        #Counts the number of cards in/remainding 
        self.cards_in_deck = len(self.card_deck)
        print(f"{self.cards_in_deck}")

    def pull_random_card(self):
        self.random_card = random.choice(self.card_deck)
        self.card_deck.remove(self.random_card)
        return self.random_card

    def card_to_string(self, card):
        return "" + card[0] + "  " + str(card[1])


class play_game:
    """Starts with score, loops till loss, calcs score.
    """

    def __init__(self): 
        """loops till lost or out of cards. NEEDS DECK
    """
        self.keep_playing = True
        self.deck = Deck()
        self.old_card = self.deck.pull_random_card()
        self.current_card = self.old_card
        print(f" {self.deck.card_to_string(self.old_card)}")
        self.player_score = 300
        while self.player_score > 0 and self.deck.remaining_cards() != 0 and self.keep_playing:  
            guess = input("What is your guess? (+/-) ")
            self.guess = guess
            self.current_card = self.deck.pull_random_card()
            print(f" {self.deck.card_to_string(self.current_card)}")
            self.calc_score()
            self.old_card = self.current_card

    def calc_score(self):
        """start with 300. corrtect earn 100. incorrect lose 75. 
        player reach <=0 game over. NEEDS CARDS
    """
        answer = None
        
        if self.old_card[1] < self.current_card[1] and self.guess == "+":
            self.player_score += 100
        elif self.old_card[1] > self.current_card[1] and self.guess == "-":
            self.player_score += 100
        elif self.old_card[1] > self.current_card[1] and self.guess == "+":
            self.player_score -= 75
        elif self.old_card[1] < self.current_card[1] and self.guess == "-":
            self.player_score -= 75
        elif self.old_card[1] == self.current_card[1]:
            print(f'"The House" always wins!')
            incorrect = answer
            self.player_score -= 75
        print(f"your score is: {self.player_score}")
        print(f"Cards remainding: {self.deck.remaining_cards()}\n")
        giveUp = input("would you like to continue? (y/n) ")
        if giveUp == 'N' or giveUp == 'n':
            print(f"Thanks for playing\n")
            self.keep_playing = False

if __name__ == "__main__":
    main ()    
