from turtle import Turtle
ALIGNMENT='center'
FONT= ("Courier", 14, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def game_over(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)