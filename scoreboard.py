from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.show_point()
       
        

    def point_l(self):
        self.score_l += 1
        self.show_point()
        

    def point_r(self):
        self.score_r += 1
        self.show_point()
        

    def show_point(self):
        self.clear()
        self.goto(-100,250)
        self.write(self.score_l, align= "center", font=("Courier", 80, "bold"))
        self.goto(100,250)
        self.write(self.score_r, align= "center", font=("Courier", 80, "bold"))

