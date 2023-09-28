from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.title("PONG GAME")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(1)
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True
while is_game_on:

    time.sleep(ball.move_speed_choice)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(l_paddle) < 80 and ball.xcor() < -320 or ball.distance(r_paddle) < 80 and ball.xcor() > 320 :
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
