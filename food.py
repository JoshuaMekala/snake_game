from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle") # creating the shape of piece of food
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) # 10x10 circle down from 20x20
        self.color("blue") 
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)        