import random

class Card:
    def __init__(self):
        self.card1 = random.randint(1, 13)
        self.card2 = random.randint(1, 13)
        self.point_total = 0

    def card(self):
        self.card1 = random.randint(1, 13)
        self.num_turns += 1
    
    def high(self):
        if self.card2 > self.card1:
            return +100
        elif self.card2 < self.card1:
            return -75


    def low(self):
        if self.card2 < self.card1:
            return self.point_total + 100
        elif self.card2 > self.card1:
            return self.point_total - 75

    

