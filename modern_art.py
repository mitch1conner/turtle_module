from turtle import Turtle,Screen
tim=Turtle()

#for _ in range(4):
    #tim.forward(100)
    #tim.left(90)

import turtle

def dashed_line(length, dash_length):
    num_dashes = length // (2 * dash_length)
    for _ in range(num_dashes):
        turtle.forward(dash_length)
        turtle.penup()
        turtle.forward(dash_length)
        turtle.pendown()

# Örnek olarak, 200 birim uzunluğunda kesikli bir çizgi çizelim:
turtle.speed(1)
dashed_line(200, 10)

turtle.done()
























screen=Screen()
screen.exitonclick()