from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"score : {self.scores}", align="center", font=("Arial", 13, "normal"))


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over\nFinal Score : {self.scores}", align="center", font=("Arial", 13, "normal"))



    def new_score(self):
        self.clear()
        self.scores += 1
        self.write(f"score : {self.scores}", align="center", font=("Arial",13,"normal"))
