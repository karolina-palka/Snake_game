#

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #if (snake.get_snake_head_poisiton()== [food.x_index, food.y_index]):
    if snake.head.distance(food) < 15:
        food.create_food()
        score.increase_score()

    if (snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290):
        score.game_over()
        time.sleep(1)
        is_game_on = False