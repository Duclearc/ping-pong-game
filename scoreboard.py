from turtle import Turtle

FONT_SIZE = 80
FONT = ("Courier", FONT_SIZE, "normal")
BUFFER = 100


class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.SCREEN_HEIGHT = screen_height
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.speed('fastest')
        self.show_scoreboard()

    def right_score_point(self):
        """adds a point to the right player's score"""
        self.right_score += 1
        self.show_scoreboard()

    def left_score_point(self):
        """adds a point to the left player's score"""
        self.left_score += 1
        self.show_scoreboard()

    def show_scoreboard(self):
        """clears the current score text and rewrites the new one"""
        self.clear()
        # right side
        self.goto(100, int(self.SCREEN_HEIGHT / 2) - BUFFER)
        self.write(self.right_score, align='center', font=FONT)
        # left side
        self.goto(-100, int(self.SCREEN_HEIGHT / 2) - BUFFER)
        self.write(self.left_score, align='center', font=FONT)
