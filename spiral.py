import turtle
import colorsys

# Ekranni sozlash
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.colormode(255)

# Ranglar ro'yxati
n = 36
h = 0
colors = []
for i in range(n):
    col = colorsys.hsv_to_rgb(h, 1, 1)
    colors.append((int(col[0]*255), int(col[1]*255), int(col[2]*255)))
    h += 1/n

# Spiral naqsh chizish
t.width(2)
for i in range(360):
    t.color(colors[i % n])
    t.forward(i * 2)
    t.right(59)  # burchak o'zgartirish spirallikni beradi

t.hideturtle()
turtle.done()
