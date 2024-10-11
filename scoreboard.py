from turtle import Turtle

FONT = ("Courier", 18, "normal")


# TODO: Create a scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.playerone_score = 0
        self.playertwo_score = 0
        self.write(
            f"P1: {self.playerone_score}              P2: {self.playertwo_score}",
            False,
            align="center",
            font=FONT,
        )

    def update_score(self):
        self.clear()
        if self.playerone_score + 1 or self.playertwo_score + 1:
            self.write(
                f"P1: {self.playerone_score}              P2: {self.playertwo_score}",
                False,
                align="center",
                font=FONT,
            )
