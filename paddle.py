from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self, position, btn1, btn2):
        super().__init__()
        self.screen = Screen()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len= 1, stretch_wid=5)
        self.penup()
        self.goto(position)
        self.move(btn1, btn2)

        

    def up(self):
        if self.ycor() < 340:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -340:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)


    def move(self ,btn1 , btn2):
        self.screen.onkeypress(self.up, btn1)
        self.screen.onkeypress(self.down,btn2)

