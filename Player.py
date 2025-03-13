class Player:
    """Represents a player in the game."""
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def receive_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        value = sum(card.value for card in self.hand)
        num_aces = sum(1 for card in self.hand if card.rank == 'A')
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

    def display_hand(self):
        return f"{self.name}'s Hand: {', '.join(map(str, self.hand))} (Value: {self.get_hand_value()})"