import random

class Dice:
    def __init__(self, sides=6):
        valid_sides = (4,6,8,10,12,20,100)
        if sides not in valid_sides:
            raise Exception(f"Invalid value sides={sides}. Use one of following: {valid_sides}")
        self.sides = sides
        self.rolls = []

    def __str__(self):
        return f"sides=d{self.sides} rolls={self.rolls} sum={sum(self.rolls)}"


    def roll(self, n=1):
        self.rolls = []
        for _ in range(n):
            self.rolls.append(random.randint(1, self.sides))
        return sum(self.rolls)

