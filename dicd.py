import random

class Dicd:
    def __init__(self):
        self.face = 0
        self.roll()

    def roll(self):
        self.face = random.randint(1, 7)

    def get_face(self):
        return self.face
