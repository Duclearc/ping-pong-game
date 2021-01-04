from turtle import Turtle

BUFFER = 50


class Paddle(Turtle):
    def __init__(self, side, screen_width, screen_height):
        super().__init__()
        self.side = side
        self.y_axis = int(screen_height / 2)
        self.x_axis = int(screen_width / 2) - BUFFER
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.height = 100
        self.start_position()

    def start_position(self):
        """positions the paddle at the correct starting point at the ends of the screen"""
        if self.side == 'right':
            self.goto(x=self.x_axis, y=0)
        elif self.side == 'left':
            self.goto(x=-self.x_axis, y=0)

    def go_up(self):
        """moves the paddle upwards by 20 pixels"""
        if self.ycor() < self.y_axis:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        """moves the paddle downwards by 20 pixels"""
        if self.ycor() > -self.y_axis:
            self.goto(self.xcor(), self.ycor() - 20)
