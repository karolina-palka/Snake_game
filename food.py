from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.create_food()
        #self.goto(self.x_index, self.y_index)

    def create_food(self):
        self.x_index = random.randint(-280, 280)
        self.y_index = random.randint(-280, 280)
        self.goto(self.x_index, self.y_index)
        #return [x_index, y_index]

