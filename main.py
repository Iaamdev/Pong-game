import time
from turtle import Screen

from ball import Ball
from paddles import Left, Right
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Left()
right_paddle = Right()
ball = Ball()
scoreboard = Scoreboard()

# FIX: when holding movement buttons for dif. paddles, one stops. FIX ME!!
screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(right_paddle.up, "i")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.down, "k")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # NOTE: creates ball border for top and bottom walls
    if ball.ycor() > 260 or ball.ycor() < -280:
        ball.wall_bounce()

    # NOTE: adds points to scoreboard for each player
    if ball.xcor() > 400:
        ball.reset_bounce()
        scoreboard.playerone_score += 1
        scoreboard.update_score()
    if ball.xcor() < -400:
        ball.reset_bounce()
        scoreboard.playertwo_score += 1
        scoreboard.update_score()

    # NOTE: collision detection for paddles
    if (
        (ball.xcor() > 360)
        and (ball.xcor() < 370)
        and (
            ball.ycor() < right_paddle.ycor() + 50
            and ball.ycor() > right_paddle.ycor() - 50
        )
    ):
        ball.setx(360)
        ball.paddle_bounce()
    if (
        (ball.xcor() < -370)
        and (ball.xcor() > -380)
        and (
            ball.ycor() < left_paddle.ycor() + 50
            and ball.ycor() > left_paddle.ycor() - 50
        )
    ):
        ball.setx(-370)
        ball.paddle_bounce()
