from turtle import Turtle

AXIS_MOVE_SPEED = 5
BALL_SPEED = 0.03
SPEED_INCREMENT = 0.7


class Ball(Turtle):
    def __init__(self, ball_size, screen_width, screen_height):
        super().__init__()
        self.move_speed = BALL_SPEED
        self.X_SPEED = AXIS_MOVE_SPEED
        self.Y_SPEED = AXIS_MOVE_SPEED
        self.SCREEN_WIDTH = int(screen_width / 2)
        self.SCREEN_HEIGHT = int(screen_height / 2)
        self.penup()
        self.speed('fastest')
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=int(20 / ball_size), stretch_len=int(ball_size / 20))

    def move(self):
        """moves the ball to one of the screen edges"""
        self.goto(x=self.xcor() + self.X_SPEED, y=self.ycor() + self.Y_SPEED)

    def bounce_y(self):
        """causes the ball to revert it's Y axis direction"""
        self.Y_SPEED *= -1

    def bounce_x(self):
        """causes the ball to revert it's X axis direction"""
        self.X_SPEED *= -1
        self.increase_speed()

    def reset_position(self):
        """resets the ball's position and speed at the center of the screen and triggers a bounce"""
        self.home()
        self.reset_speed()
        self.bounce_x()

    def increase_speed(self):
        """increases the ball's speed by the SPEED_INCREMENT"""
        self.move_speed *= SPEED_INCREMENT

    def reset_speed(self):
        """resets the ball's speed to it's initial value"""
        self.move_speed = BALL_SPEED
