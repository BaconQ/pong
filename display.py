from turtle import Screen

class Display:
    def __init__(self):
       self.screen = Screen()
       self.screen.bgcolor("black")
       self.screen.setup(width=800, height=800)
       self.screen.tracer(0)
       self.screen._root.resizable(False, False)

    
       
       
       


    def exit(self):
        self.screen.exitonclick()

    def listen(self):
        self.screen.listen()

    def update(self):
        self.screen.update()

    