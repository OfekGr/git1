
class Card:

    def __init__(self, value, suit):
        self.value=value
        self.suit=suit


    def __gt__(self, current_card, other_card):
        if current_card.value > other_card.value:
            return True
        elif current_card.value == other_card.value:
            if current_card.suit > other_card.suit:
                return True
            else:
                return False
        else:
            return False

    def check_sign(self):
        if self.value == 2 and self.suit == 0:
            return  "Two of Diamonds"
        elif self.value == 2 and self.suit == 1:
            return  "Two of Spades"
        elif self.value == 2 and self.suit == 2:
            return "Two of Hearts"
        elif self.value == 2 and self.suit == 3:
            return "Two of Clubs"
        if self.value == 3 and self.suit == 0:
            return  "Three of Diamonds"
        elif self.value == 3 and self.suit == 1:
            return  "Three of Spades"
        elif self.value == 3 and self.suit == 2:
            return "Three of Hearts"
        elif self.value == 3 and self.suit == 3:
            return "Three of Clubs"
        if self.value == 4 and self.suit == 0:
            return  "Four of Diamonds"
        elif self.value == 4 and self.suit == 1:
            return  "Four of Spades"
        elif self.value == 4 and self.suit == 2:
            return "Four of Hearts"
        elif self.value == 4 and self.suit == 3:
            return "Four of Clubs"
        if self.value == 5 and self.suit == 0:
            return  "Five of Diamonds"
        elif self.value == 5 and self.suit == 1:
            return  "Five of Spades"
        elif self.value == 5 and self.suit == 2:
            return "Five of Hearts"
        elif self.value == 5 and self.suit == 3:
            return "Five of Clubs"
        if self.value == 6 and self.suit == 0:
            return  "Six of Diamonds"
        elif self.value == 6 and self.suit == 1:
            return  "Six of Spades"
        elif self.value == 6 and self.suit == 2:
            return "Six of Hearts"
        elif self.value == 6 and self.suit == 3:
            return "Six of Clubs"
        if self.value == 7 and self.suit == 0:
            return  "Seven of Diamonds"
        elif self.value == 7 and self.suit == 1:
            return  "Seven of Spades"
        elif self.value == 7 and self.suit == 2:
            return "Seven of Hearts"
        elif self.value == 7 and self.suit == 3:
            return "Seven of Clubs"
        if self.value == 8 and self.suit == 0:
            return  "Eight of Diamonds"
        elif self.value == 8 and self.suit == 1:
            return  "Eight of Spades"
        elif self.value == 8 and self.suit == 2:
            return "Eight of Hearts"
        elif self.value == 8 and self.suit == 3:
            return "Eight of Clubs"
        if self.value == 9 and self.suit == 0:
            return  "Nine of Diamonds"
        elif self.value == 9 and self.suit == 1:
            return  "Nine of Spades"
        elif self.value == 9 and self.suit == 2:
            return "Nine of Hearts"
        elif self.value == 9 and self.suit == 3:
            return "Nine of Clubs"
        if self.value == 10 and self.suit == 0:
            return  "Ten of Diamonds"
        elif self.value == 10 and self.suit == 1:
            return  "Ten of Spades"
        elif self.value == 10 and self.suit == 2:
            return "Ten of Hearts"
        elif self.value == 10 and self.suit == 3:
            return "Ten of Clubs"
        if self.value == 11 and self.suit == 0:
            return  "Jack of Diamonds"
        elif self.value == 11 and self.suit == 1:
            return  "Jack of Spades"
        elif self.value == 11 and self.suit == 2:
            return "Jack of Hearts"
        elif self.value == 11 and self.suit == 3:
            return "Jack of Clubs"
        if self.value == 12 and self.suit == 0:
            return  "Queen of Diamonds"
        elif self.value == 12 and self.suit == 1:
            return  "Queen of Spades"
        elif self.value == 12 and self.suit == 2:
            return "Queen of Hearts"
        elif self.value == 12 and self.suit == 3:
            return "Queen of Clubs"
        if self.value == 13 and self.suit == 0:
            return  "King of Diamonds"
        elif self.value == 13 and self.suit == 1:
            return  "King of Spades"
        elif self.value == 13 and self.suit == 2:
            return "King of Hearts"
        elif self.value == 13 and self.suit == 3:
            return "King of Clubs"
        if self.value == 14 and self.suit == 0:
            return  "Ace of Diamonds"
        elif self.value == 14 and self.suit == 1:
            return  "Ace of Spades"
        elif self.value == 14 and self.suit == 2:
            return "Ace of Hearts"
        elif self.value == 14 and self.suit == 3:
            return "Ace of Clubs"
