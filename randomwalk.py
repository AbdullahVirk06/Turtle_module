from turtle import Turtle,Screen
import random

timmy = Turtle()
timmy.pensize(15)
timmy.speed(10)
direction = [0,90,180,270]

num_step = 100
step_length = 10

for sides in range(num_step):
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.color(r,g,b)
    random_direction = random.choice(direction)
    timmy.setheading(random_direction)
    timmy.forward(20)
    

screen = Screen()
screen.exitonclick()