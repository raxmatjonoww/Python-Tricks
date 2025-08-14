import turtle
import math
import time

# Ekranni sozlash
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Raketa uchish trayektoriyasi")
turtle.colormode(255)

raketa = turtle.Turtle()
raketa.color(255, 0, 0)
raketa.shape("triangle")
raketa.penup()
raketa.speed(1)

path = turtle.Turtle()
path.hideturtle()
path.speed(0)
path.color("white")

for angle in range(0, 91, 2): 
    x = angle * 5
    y = (angle * math.sin(math.radians(60))) * 4 - 0.05 * (angle ** 2)
    path.goto(x - 200, y - 200)

for angle in range(0, 91, 2):
    x = angle * 5
    y = (angle * math.sin(math.radians(60))) * 4 - 0.05 * (angle ** 2)
    raketa.goto(x - 200, y - 200)
    time.sleep(0.05)

turtle.done()
