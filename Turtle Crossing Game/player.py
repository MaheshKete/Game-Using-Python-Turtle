from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        self.shape("turtle")
        self.move_speed = 0.1

    def move(self):
        self.fd(20)

    def next_level(self):
        self.goto(0,-280)
        self.move_speed *= 0.9