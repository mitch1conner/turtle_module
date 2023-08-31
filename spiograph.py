from turtle import Turtle, Screen
import random
tim = Turtle()
rad=int(input("Enter radius value:"))
head=int(input("Enter heading value:"))
num=int(input("Enter repeating time:"))

def draw_circle(radius,heading,repeat):

    for repeating in range(repeat+1):
        r = random.random()
        g = random.random()
        b = random.random()
       
        tim.pencolor(r,g,b)
        tim.setheading(tim.heading()+10)
        tim.circle(radius)

draw_circle(rad,head,num)















screen = Screen()
screen.exitonclick()
