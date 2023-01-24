from turtle import Turtle

FONT = ("Courier",14,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0,270)
        self.counter = 0
        self.update_score()
        self.refresh_score()

    def update_score(self):
        self.write("Score: "+ str(self.counter),align="center",font= FONT)


    def refresh_score(self):
        self.clear()
        self.update_score()
        self.counter += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.",align="center",font= FONT)


        


