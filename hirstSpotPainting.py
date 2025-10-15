from turtle import Turtle,Screen
import random

color_list = [(219, 161, 107), (194, 151, 171), (229, 240, 244), (163, 167, 34), (240, 77, 54), (149, 52, 98), (240, 222, 66), (236, 68, 134), (11, 145, 66), (63, 198, 221), (6, 138, 181), (20, 169, 128)]

timmy = Turtle()
timmy.penup()
timmy.pensize(15)
timmy.speed(10)
screen = Screen()
timmy.hideturtle()
screen.colormode(255)
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for _ in range(10):
    for _ in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

screen = Screen()
screen.exitonclick()