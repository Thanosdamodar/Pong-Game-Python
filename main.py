# TODO LIST
# TODO 1 Make Two Paddles for two players wth its own control
# TODO 2 Make a ball move itself
# TODO 3 Make the ball bounce of the wall and paddles
# TODO 4 Keep score

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Objects
screen = Screen()
turtle = Turtle()
ball = Ball()

# Setting up the screen
screen.setup(width=800, height=600)
screen.bgcolor("black")
turtle.hideturtle()
screen.title("Pong - The Arcade Game")
screen.tracer(0)

# Paddle creation

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
scoreboard = Scoreboard()

# Paddle Movement

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True
while game_on:
    scoreboard.update_score()
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_score()

    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_score()

    if scoreboard.right_score == 10 or scoreboard.left_score == 10:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
