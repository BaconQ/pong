from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len= 1, stretch_wid= 1)
        self.penup()
        self.goto(0,0)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *=-1
        self.move_speed *= 0.5

    def reset(self):
            self.goto(0,0)
            self.move_speed = 0.1
            self.bounce_x()
        

    
