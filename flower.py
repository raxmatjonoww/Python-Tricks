import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.colormode(255)

n = 36  
h = 0
colors = []
for i in range(n):
    col = colorsys.hsv_to_rgb(h, 1, 1)
    colors.append((int(col[0]*255), int(col[1]*255), int(col[2]*255)))
    h += 1/n

for i in range(360):
    t.color(colors[i % n])
    t.circle(190 - i, 90)
    t.left(90)
    t.circle(190 - i, 90)
    t.left(18)

t.hideturtle()
turtle.done()
