from game.Card import Card
import random


class Director:

    def __init__(self):
        self.card = Card()
        self.another = "y"
        self.choice = ""
        self.score = 300
        self.keep_playing = True

    def start_playing(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        self.card.card1 = random.randint(1, 13)

    def do_updates(self):
        if self.choice == "l":
            self.score += self.card.low()

        if self.choice == "h":
            self.score += self.card.high()

    def do_outputs(self):
        print(f"\nThe Card is: {self.card.card1}")
        self.card.card2 = random.randint(1, 13)

        self.choice = input("Higher or Lower? [h/l]:")
        print(f"Next card is: {self.card.card2}")
        self.do_updates()

        print(f"Your score is: {self.score}")
        self.card.card1 = self.card.card2

        if self.score > 0:
            self.another = input("would you like to play again? [y/n]:")
            if self.another == "n":
                self.keep_playing = False
        else:
            self.keep_playing = False
