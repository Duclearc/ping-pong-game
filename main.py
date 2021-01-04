from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from game_table import GameTable

SCREEN_SIZE = {
    'width': 800,
    'height': 600,
}
BALL_SIZE = 20
GAME_Y_BARRIER = int(SCREEN_SIZE['height'] / 2) - BALL_SIZE
GAME_X_BARRIER = int(SCREEN_SIZE['width'] / 2) - BALL_SIZE * 4 + 10

# Screen setup
screen = Screen()
screen.bgcolor('black')
screen.screensize(canvwidth=SCREEN_SIZE['width'], canvheight=SCREEN_SIZE['height'])
screen.title('Pong Game')
screen.tracer(0)

# Paddles setup
paddle_right = Paddle(side='right', screen_width=SCREEN_SIZE['width'], screen_height=SCREEN_SIZE['height'])
paddle_left = Paddle(side='left', screen_width=SCREEN_SIZE['width'], screen_height=SCREEN_SIZE['height'])
screen.listen()
screen.onkeypress(paddle_right.go_up, 'Up')
screen.onkeypress(paddle_right.go_down, 'Down')
screen.onkeypress(paddle_left.go_up, 'e')
screen.onkeypress(paddle_left.go_down, 's')

# Ball setup
ball = Ball(BALL_SIZE, SCREEN_SIZE['width'], SCREEN_SIZE['height'])

# Game setup
game_table = GameTable(GAME_Y_BARRIER, GAME_X_BARRIER, BALL_SIZE)
score = Scoreboard(SCREEN_SIZE['height'])
game_on = True


def detect_collision():
    """makes the ball bounce upon collision between it and the screen edges or the paddles"""
    # with the top and bottom of screen
    if ball.ycor() > GAME_Y_BARRIER or ball.ycor() < -GAME_Y_BARRIER:
        ball.bounce_y()
    # with the paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > GAME_X_BARRIER \
            or ball.distance(paddle_left) < 50 and ball.xcor() < -GAME_X_BARRIER:
        ball.bounce_x()


def detect_miss():
    """increases the score of the opposite side upon ball passing a certain screen threshold"""
    # misses the right paddle
    if ball.xcor() > (GAME_X_BARRIER + 100):
        score.left_score_point()
        ball.reset_position()

    # misses the left paddle
    if ball.xcor() < -(GAME_X_BARRIER + 100):
        score.right_score_point()
        ball.reset_position()


while game_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()
    detect_collision()
    detect_miss()

screen.exitonclick()
