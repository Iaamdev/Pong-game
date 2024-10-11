from turtle import Turtle


class Ball(Turtle):

    # NOTE: creates the ball used for game
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.ball_dx = 8
        self.ball_dy = 8
        self.move_speed = 0.1

    def move(self):
        set_x = self.xcor() + self.ball_dx
        set_y = self.ycor() + self.ball_dy
        self.goto(set_x, set_y)

    def wall_bounce(self):
        self.ball_dy *= -1

    def paddle_bounce(self):
        self.ball_dx *= -1
        self.move_speed *= 1.5

    def reset_bounce(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_bounce()
