ALIGNMENT="center"
FONT=("Arial",12,"normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=("courier",24,"normal"))