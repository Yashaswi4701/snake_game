from turtle import Screen, Turtle
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
food = Food()
food.refresh()

scoreboard = Scoreboard()
while game_is_on:

    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.snake_head.distance(food)<15:
        food.refresh()
        snake.increase_snake_size()
        scoreboard.update_scoreboard()
    if snake.snake_self_collision():
        scoreboard.game_over()
        print('Game over')
        game_is_on=False
    a=snake.snake_head.xcor()
    b=snake.snake_head.ycor()
    if a<-280 or a>280 or b>280 or b<-280:
        scoreboard.game_over()
        print('Game Over')
        game_is_on=False

screen.exitonclick()
