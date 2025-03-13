class Card:
    """Represents a single card in a deck."""

    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.rank} of {self.suit}"