import pygame
import tkinter as tk
from pygame import mixer
from tkinter import messagebox
from GameEngine import GameEngine

class BlackjackUI:
    def show_endgame_popup(self, message):
        self.winner_label.config(text=message)  # Display winner in UI
        if self.game.player.get_hand_value() >= 21:
            self.hit_button.config(state=tk.DISABLED)
            self.stand_button.config(
                state=tk.DISABLED)  # Prevent actions after bust
        self.stand_button.config(state=tk.DISABLED)

        response = messagebox.askquestion("Game Over",
                                          f"{message}\n\nWould you like to play again?",
                                          icon='warning')

        if response == 'yes':
            self.new_game()
        else:
            self.show_main_menu()


    def update_probability(self):
        total_cards = len(self.game.deck.cards)
        if total_cards == 0:
            bust_prob, blackjack_prob = 0.0, 0.0
        else:
            player_value = self.game.player.get_hand_value()
            bust_count = sum(1 for card in self.game.deck.cards if
                             player_value + card.value > 21)
            blackjack_count = sum(1 for card in self.game.deck.cards if
                                  player_value + card.value == 21)
            bust_prob = (bust_count / total_cards) * 100
            blackjack_prob = (blackjack_count / total_cards) * 100

        self.probability_label.config(
            text=f"Bust Probability: {bust_prob:.1f}% | Blackjack Probability: {blackjack_prob:.1f}%")

    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()  # Clearing main menu before switching views
        # Ensuring UI resets properly without duplicates
        self.root.configure(bg="lightgreen")

        title_label = tk.Label(self.root, text="Blackjack Odds and Probabilities Game Menu",
                               font=("Arial", 16))
        title_label.pack()

        play_button = tk.Button(self.root, text="Start Game",
                                command=self.start_game)
        play_button.pack()

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack()

        pygame.mixer.init()
        mixer.music.load("Lounge.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

    def start_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        play_button = tk.Button(self.root, text="Spanish 21",
                                command=self.spanish_21)
        play_button.pack()
        play_button = tk.Button(self.root, text="Standard Blackjack",
                                command=self.standard_blackjack)
        play_button.pack()

    def spanish_21(self):
        self.game = GameEngine(spanish_21=True)
        for widget in self.root.winfo_children():
            widget.destroy()  # Ensuring UI resets properly without duplicates

        self.label = tk.Label(self.root, text="Spanish 21 Game",
                                font=("Arial", 16))
        self.label.pack()

        self.player_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.player_label.pack()

        self.dealer_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.dealer_label.pack()

        self.probability_label = tk.Label(self.root,
                                            text="Bust Probability: ---% | Blackjack Probability: ---%",
                                            font=("Arial", 12))
        self.probability_label.pack()

        self.winner_label = tk.Label(self.root, text="", font=("Arial", 14),
                                         fg="red")
        self.winner_label.pack()

        self.hit_button = tk.Button(self.root, text="Hit", command=self.hit)
        self.hit_button.pack()

        self.stand_button = tk.Button(self.root, text="Stand",
                                          command=self.stand)
        self.stand_button.pack()

        self.new_game_button = tk.Button(self.root, text="New Game",
                                             command=self.new_game)
        self.new_game_button.pack()

        self.new_game()  # Ensuring cards are drawn automatically at game start

        exit_button = tk.Button(self.root, text="Exit",
                                    command=self.root.quit)
        exit_button.pack()

    def standard_blackjack(self):
        self.game = GameEngine(spanish_21=False)
        for widget in self.root.winfo_children():
            widget.destroy()  # Ensuring UI resets properly without duplicates

        self.label = tk.Label(self.root, text="Standard Blackjack Game",
                              font=("Arial", 16))
        self.label.pack()

        self.player_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.player_label.pack()

        self.dealer_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.dealer_label.pack()

        self.probability_label = tk.Label(self.root,
                                          text="Bust Probability: ---% | Blackjack Probability: ---%",
                                          font=("Arial", 12))
        self.probability_label.pack()

        self.winner_label = tk.Label(self.root, text="", font=("Arial", 14),
                                     fg="red")
        self.winner_label.pack()

        self.hit_button = tk.Button(self.root, text="Hit", command=self.hit)
        self.hit_button.pack()

        self.stand_button = tk.Button(self.root, text="Stand",
                                      command=self.stand)
        self.stand_button.pack()

        self.new_game_button = tk.Button(self.root, text="New Game",
                                         command=self.new_game)
        self.new_game_button.pack()

        self.new_game()  # Ensuring cards are drawn automatically at game start

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack()

    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Odds and Probabilities Game")
        self.show_main_menu()

    def update_ui(self):
        self.player_label.config(
            text=f"Player's Hand: {', '.join(map(str, self.game.player.hand))} (Value: {self.game.player.get_hand_value()})")
        self.dealer_label.config(text=f"Dealer's Hand: {self.game.dealer.hand[0]}, [Hidden]")
        self.update_probability()

    def hit(self):
        if self.game.player.get_hand_value() >= 21:
            return# Prevents drawing more after bust
        self.game.player.receive_card(self.game.deck.draw_card())
        if self.game.player.get_hand_value() >= 21:
            self.stand()
        self.update_ui()
        self.update_probability()

    def stand(self):
        self.game.dealer_turn()
        self.dealer_label.config(text=self.game.dealer.display_hand())
        self.update_probability()
        result = self.game.check_winner()
        self.show_endgame_popup(result)  # Ensuring only one endgame popup

    def new_game(self):
        self.hit_button.config(state=tk.NORMAL)  # Re-enable Hit button
        self.stand_button.config(state=tk.NORMAL)  # Re-enable Stand button
        self.game = GameEngine(spanish_21=True)  # Ensuring correct game mode
        self.game.deal_initial_cards()
        self.update_ui()  # Ensuring UI updates when game starts
        self.winner_label.config(text="")
