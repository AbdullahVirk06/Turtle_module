from turtle import Turtle,Screen
import random

timmy = Turtle()


for sides in range(3,11):
    angle = 360/sides
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.color(r,g,b)
    for _ in range(sides):
        timmy.forward(100)
        timmy.left(angle)

screen = Screen()
screen.exitonclick()