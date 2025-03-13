from Card import Card
import random


class Deck:
    """Represents a deck of playing cards, supporting Spanish 21."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    standard_ranks = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }
    spanish_ranks = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'J': 10, 'Q': 10, 'K': 10, 'A': 11  # No '10' cards in Spanish 21
    }

    def __init__(self, num_decks=1, spanish_21=False):
        ranks = self.spanish_ranks if spanish_21 else self.standard_ranks
        self.cards = [Card(rank, suit, value) for rank, value in ranks.items()
                      for suit in self.suits for _ in range(num_decks)]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

