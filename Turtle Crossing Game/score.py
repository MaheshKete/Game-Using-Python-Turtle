from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-285,275)
        self.level = 1
        self.write(f"Level: {self.level}",font=("Aerial",14,"normal"))

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=("Aerial", 14, "normal"))

    def game_over(self):
        self.goto(-80,0)
        self.write(f"GAME OVER", font=("Aerial", 24, "normal"))
