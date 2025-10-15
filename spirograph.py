from turtle import Turtle,Screen
import random

timmy = Turtle()
timmy.pensize(10)
timmy.speed(20)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

for angle in range(0, 360, 10):   
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(angle)
    

screen = Screen()
screen.exitonclick()