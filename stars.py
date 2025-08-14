import turtle
import random

# Ekranni sozlash
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Yulduzlar osmoni")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.colormode(255)

# Yulduz chizish funksiyasi
def draw_star(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 5 burchakli yulduz burchagi
    t.end_fill()

# Tasodifiy yulduzlar joylashuvi
for _ in range(100):  # 100 ta yulduz
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(5, 15)
    color = (255, 255, 255)  # oq rang
    draw_star(x, y, size, color)

# Ba’zi yulduzlar sariq rangda bo‘lishi uchun
for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(5, 15)
    color = (255, 255, 150)  # och sariq rang
    draw_star(x, y, size, color)

turtle.done()
