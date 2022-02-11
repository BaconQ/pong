from display import Display
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

display = Display()
scoreboard = Scoreboard()
player1 = Paddle((350,0) , "Up", "Down")
player2= Paddle((-350,0), "w" , "s")
ball = Ball()

display.listen()
is_game_on = True

while is_game_on:
    display.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    
    elif ball.xcor() > 330 and ball.distance(player1) < 50 or ball.xcor() < -330 and ball.distance(player2) < 50:
        ball.bounce_x()

    elif ball.xcor() > 400:
        ball.reset()
        scoreboard.point_l()

    elif ball.xcor() < -400:
        ball.reset()
        scoreboard.point_r()
    
    
display.exit()      
