from turtle import Turtle,Screen

timmy = Turtle()
timmy.color("coral")

for _ in range(50):
    timmy.pendown()
    timmy.forward(3)
    timmy.penup()
    timmy.forward(3)

screen = Screen()
screen.exitonclick()