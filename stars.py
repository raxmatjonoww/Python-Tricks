import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Yulduzlar osmoni")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.colormode(255)

def draw_star(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

for _ in range(100): 
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(5, 15)
    color = (255, 255, 255) 
    draw_star(x, y, size, color)

for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(5, 15)
    color = (255, 255, 150) 
    draw_star(x, y, size, color)

turtle.done()
