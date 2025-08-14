import turtle

# Ekranni sozlash
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.color("lime")
t.speed(0)
t.hideturtle()
t.left(90)  # yuqoriga qarab boshlaydi
t.penup()
t.goto(0, -250)
t.pendown()

# Fraktal daraxt funksiyasi
def draw_tree(branch_length):
    if branch_length < 10:  # eng kichik shox
        return
    t.forward(branch_length)
    t.left(30)
    draw_tree(branch_length - 15)
    t.right(60)
    draw_tree(branch_length - 15)
    t.left(30)
    t.backward(branch_length)

# Daraxtni chizish
draw_tree(100)

turtle.done()
