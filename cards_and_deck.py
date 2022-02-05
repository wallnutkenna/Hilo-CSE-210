import random


class Deck:
    # Creates a deck with 52 cards and 4 suits with 13 cards in each suit 
    def _int_(self):
        #creates the deck with the cards in it 
        self.card_deck = []
        for i in range(0,13):
            self.card_deck.append(['heart',i+1])
        for i in range(0,13):
            self.card_deck.append(['clover',i+1])
        for i in range(0,13):
            self.card_deck.append(['spade',i+1])
        for i in range(0,13):
            self.card_deck.append(['diamond',i+1])

    def show_number(self):
        #Counts the number of cards in/remainding 
        self.cards_in_deck = len(self.card_deck)
        print(f"{self.cards_in_deck}")

    def pull_random_card(self):
        self.random_card = random.choice(self.card_deck)
        print(f"{self.random_card}")

    def pop_pulled_card(self):
        self.card_deck.remove(self.random_card)

