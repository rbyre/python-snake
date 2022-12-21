from turtle import Screen, Turtle
import time
import random as r
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)


snake = Snake()
scoreboard = Scoreboard()
scoreboard.write_score()
food = Food()


food_list = []



# def spawn_random_food():
#   food = Food()
#   food.refresh()
  # food_list.append(food)

# def update_score(score):
#   return score+1

# def check_food_eaten(snake, list_with_food, score):
def check_food_eaten(snake, score, food):
  # for food in list_with_food:
  if snake.head.distance(food) <= 15:
    # list_with_food.remove(food)
    # food.hideturtle()
    food.refresh()
    # spawn_random_food()
    score.add_one_point()
    new_position = snake.get_snake_parts()[-1].position()
    snake.add_part(new_position)
  
def check_self_crash(snake):
  snakeparts = snake.get_snake_parts()
  for part in snakeparts:
    if snake.head.distance(part) == 0:
      return False
    else:
      return True

game_on = True
counter = 20

while game_on:
  # counter -=1
  # if counter == 0:
  #   spawn_random_food()
  #   counter = 20
  
  screen.onkey( snake.move_up, 'Up')
  screen.onkey( snake.move_down, 'Down')
  screen.onkey( snake.move_left, 'Left')
  screen.onkey( snake.move_right, 'Right')
  screen.onkey( snake.move_up, 'w')
  screen.onkey( snake.move_down, 's')
  screen.onkey( snake.move_left, 'a')
  screen.onkey( snake.move_right, 'd')
  screen.listen()
  screen.update()
  time.sleep(.2)
  
  snake.move()
  if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.add_one_point()
    randomlength = r.randint(1,5)
    for length in range(randomlength):
      new_position = snake.get_snake_parts()[-1].position()
      snake.add_part(new_position)

  # Game over når kanten treffes
  # if snake.head.xcor() >= 300 or snake.head.xcor()<= -300 or snake.head.ycor() >= 300 or snake.head.ycor()<= -300:
  #   game_on = False
  #   scoreboard.reset()

  # Kommer inn i skjerm på motsatt side når en går ut av skjerm
  if snake.head.xcor() > 300:
    snake.head.goto(-300, snake.head.ycor())
  elif snake.head.xcor() < -300:
    snake.head.goto(300, snake.head.ycor())
  elif snake.head.ycor() > 300:
    snake.head.goto(snake.head.xcor(), -300)
  elif snake.head.ycor() < -300:
    snake.head.goto(snake.head.xcor(), 300)
  
  # Detect collision with tail
  for part in snake.get_snake_parts()[1 : ]:
    if snake.head.distance(part) < 10:
      game_on = False
      scoreboard.reset()

  


screen.exitonclick()