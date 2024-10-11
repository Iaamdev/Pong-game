from turtle import Turtle

# NOTE: can refactor classes Right and Left into one (Paddle) class
# giving "self.goto" a "position" argument and setting "left_paddle"
# and "right_paddle" variable in main file as tuples:
# right_paddle = Paddle(said "xcor", said "ycor")
# left_paddle = Paddle(said "xcor", said "ycor")


class Right(Turtle):

    # NOTE: builds the right paddle
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.speed(0)
        self.goto(380, 0)

    def up(self):
        u = self.ycor()
        u += 30
        self.sety(u)

    def down(self):
        d = self.ycor()
        d -= 30
        self.sety(d)


class Left(Turtle):
    # NOTE: may possible make this paddle move randomly
    # make single and two player functionality?
    # NOTE: builds the left paddle
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.speed(0)
        self.goto(-390, 0)

    def up(self):
        u = self.ycor()
        u += 30
        self.sety(u)

    def down(self):
        d = self.ycor()
        d -= 30
        self.sety(d)
