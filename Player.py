import random

class Player:
    def __init__(self, name, NumOfCards = 26):
        self.name = name
        self.NumOfCards = NumOfCards
        self.playerhand = []
        if NumOfCards > 26 or NumOfCards < 10:
            self.NumOfCards=26


    def set_hand(self, cards):
        for i in range(self.NumOfCards):
            if (len(self.playerhand) < (self.NumOfCards)):
                self.playerhand.append(cards.deal_one())

    def get_card(self):
        card_index=random.choice(range(len(self.playerhand)))
        return self.playerhand.pop(card_index)

    def add_card(self, card):
        self.playerhand.append(card)

    def __str__(self):
        return 'Playerhand:', {self.playerhand}, 'number of cards in hand:', {self.NumOfCards}

    def __repr__(self):
        return 'Playerhand:', {self.playerhand}, 'number of cards in hand:', {self.NumOfCards}

