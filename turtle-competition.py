import turtle
import random
import time

screen = turtle.Screen()
screen.title("Turtle poygasi")
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-200, 100)
pen.pendown()
pen.right(90)
pen.forward(200)
pen.penup()
pen.goto(200, 100)
pen.pendown()
pen.forward(200)
pen.hideturtle()

colors = ["red", "green", "blue", "orange", "purple"]
racers = []

y_positions = [60, 30, 0, -30, -60]

for i in range(5):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(colors[i])
    racer.penup()
    racer.goto(-200, y_positions[i])
    racers.append(racer)

time.sleep(1)
finish_line_x = 200
race_on = True

while race_on:
    for racer in racers:
        move = random.randint(1, 5)
        racer.forward(move)
        if racer.xcor() >= finish_line_x:
            race_on = False
            winner_color = racer.pencolor()
            break

turtle.penup()
turtle.goto(-50, -100)
turtle.color("black")
turtle.write(f"G'olib: {winner_color} turtle!", font=("Arial", 16, "bold"))

turtle.done()
