from game_cards.DeckOfCards import DeckOfCards
from game_cards.Player import Player

class CardGame:
    def __init__(self, p1name, p2name, num_of_cards = 26):
        self.playerOne=Player(p1name, num_of_cards)
        self.playerTwo=Player(p2name, num_of_cards)
        self.deck = DeckOfCards()
        self.gameOn=False

    def new_game(self):
        if self.gameOn==False:
            self.gameOn=True
            self.deck.cards_shuffle()
            self.playerOne.set_hand(self.deck)
            self.playerTwo.set_hand(self.deck)
        else:
            print("game no bueno, already running")


    def get_winner(self):
        if len(self.playerOne.playerhand) < len(self.playerTwo.playerhand):
            self.gameOn=False
            return f"game ended, {self.playerTwo.name} is the winner!"
        elif len(self.playerOne.playerhand) > len(self.playerTwo.playerhand):
            self.gameOn=False
            return f"game ended, {self.playerOne.name} is the winner!"
        elif len(self.playerOne.playerhand) == len(self.playerTwo.playerhand):
            self.gameOn=False
            return None