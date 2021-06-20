
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
    if snake.head.distance(food) < 15:
        x = snake.head.xcor()
        y = snake.head.ycor()
        snake.extend()
        food.create_food()
        score.increase_score()
        snake.extend()

    if (snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290):
        is_game_on = False
        score.game_over()
        time.sleep(1)

    for segment in snake.segments[1:]:

        if (snake.head.distance(segment)) < 10:
            is_game_on = False
            score.game_over()
            time.sleep(1)