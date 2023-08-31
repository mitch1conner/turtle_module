from turtle import Turtle, Screen
import random
tim = Turtle()
loop_var=30
iteration=0


while loop_var>1:
    angle_random=random.randint(0,270)   
    direction_random=random.randint(50,200)
    pensize=(random.randint(2,20))
    iteration=iteration+1    
    r = random.random()
    g = random.random()
    b = random.random()
    tim.pencolor(r, g, b)
    tim.right(angle_random)
    tim.forward(direction_random)
    tim.speed(1)
    tim.pensize(pensize)
    print("-------------------------------------")
    print("Iteration:",iteration)
    print("Direction:",direction_random)
    print("Angle:",angle_random)
    print("Thickness:",pensize)
    print("-------------------------------------")
    loop_var=loop_var-1












screen = Screen()
screen.exitonclick()