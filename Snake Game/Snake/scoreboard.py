from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # with open("data.txt") as data:
        #     self.high_score = int(data.read())
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()
        self.increase_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} ", align="center", font=("Aerial", 14, "normal"))

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",font=("Aerial",24,"normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        # if self.score > self.high_score:
        #     with open("data.txt",mode="w") as file:
        #         file.write(str(self.score))
        self.high_score = self.score
        self.score = 0
        self.update_scoreboard()