import Deck
from Player import Player
from Dealer import Dealer
from Deck import Deck
class GameEngine:
    """Controls the game flow."""

    def __init__(self, num_decks=1, spanish_21=False):
        self.spanish_21 = spanish_21
        self.deck = Deck(num_decks, spanish_21)
        self.player = Player("Player")
        self.dealer = Dealer()

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.receive_card(self.deck.draw_card())
            self.dealer.receive_card(self.deck.draw_card())

    def player_hit(self):
        if self.player.get_hand_value() > 21:
            return "Bust!"
        if self.deck.cards:
            self.player.receive_card(self.deck.draw_card())
        return self.player.get_hand_value()

    def dealer_turn(self):
        while self.dealer.should_hit():
            self.dealer.receive_card(self.deck.draw_card())

    def check_winner(self):
        player_value = self.player.get_hand_value()
        dealer_value = self.dealer.get_hand_value()
        if player_value > 21:
            return "Dealer wins!"
        elif dealer_value > 21:
            return "Player wins!"
        elif self.spanish_21 and player_value == 21:
            return "Player wins! (Spanish 21 rule)"
        elif player_value > dealer_value:
            return "Player wins!"
        elif player_value == dealer_value:
            return "Push! It's a tie." if not self.spanish_21 else "Player wins! (Spanish 21 rule)"
        else:
            return "Dealer wins!"

