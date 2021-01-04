from turtle import Turtle


class GameTable(Turtle):
    def __init__(self, screen_height, screen_width, ball_and_paddle_width):
        super().__init__()
        self.BOTTOM_SCREEN = -(screen_height + ball_and_paddle_width - 5)
        self.TOP_SCREEN = screen_height + ball_and_paddle_width - 5
        self.LEFT_EDGE_SCREEN = -(screen_width + ball_and_paddle_width)
        self.RIGHT_EDGE_SCREEN = screen_width + ball_and_paddle_width
        self.BOTTOM_LEFT_SCREEN = (self.LEFT_EDGE_SCREEN, self.BOTTOM_SCREEN)
        self.BOTTOM_RIGHT_SCREEN = (self.RIGHT_EDGE_SCREEN, self.BOTTOM_SCREEN)
        self.TOP_LEFT_SCREEN = (self.LEFT_EDGE_SCREEN, self.TOP_SCREEN)
        self.TOP_RIGHT_SCREEN = (self.RIGHT_EDGE_SCREEN, self.TOP_SCREEN)
        self.draw_game_table()

    def draw_game_table(self):
        """draws the edges around the game table"""
        self.hideturtle()
        self.color('yellow')
        self.goto(0, self.TOP_SCREEN)
        self.goto(0, self.BOTTOM_SCREEN)
        self.goto(self.BOTTOM_LEFT_SCREEN)
        self.goto(self.TOP_LEFT_SCREEN)
        self.goto(self.TOP_RIGHT_SCREEN)
        self.goto(self.BOTTOM_RIGHT_SCREEN)
        self.goto(self.BOTTOM_LEFT_SCREEN)
