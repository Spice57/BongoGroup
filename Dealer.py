from Player import Player

class Dealer(Player):
    """Represents the dealer in the game."""

    def __init__(self):
        super().__init__("Dealer")

    def should_hit(self):
        return self.get_hand_value() < 17
