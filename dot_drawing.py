import turtle as turtle_module
import random
tim = turtle_module.Turtle()
tim.speed("fastest")
turtle_module.colormode(255)
color_list=[(244,227,206),(200,225,242),(245,196,218),(226,167,192),(176,171,202),(193,212,167),(164,213,212),(197,218,202),(163,213,215),(191,168,197),(177,176,208)]
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots=100
for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count %10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

















screen = turtle_module.Screen()
screen.exitonclick()