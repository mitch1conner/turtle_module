from turtle import Turtle, Screen
import random
tim = Turtle()
edge_list = [3, 4, 5, 6, 8, 9]
tim.speed(1)

def shape_creator(number):
    angle = 360 / number  # 360 dereceye bölünmeli
    edge_number = number
    for line in range(number):
        tim.forward(100)
        tim.right(angle)  # Çizgiyi sağa çizmek için right kullanılmalı
    r = random.random()
    g = random.random()
    b = random.random()
    tim.pencolor(r, g, b)
for edges in edge_list:
    shape_creator(edges)

screen = Screen()
screen.exitonclick()
