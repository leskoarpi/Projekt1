import turtle
t = turtle.Turtle()


def virag():
    t.color("purple")
    t.speed(0)
    t.hideturtle()
    t.pendown()
    for x in range(50):
        t.circle(80, 90)
        if x % 2 == 0:
            t.circle(60, 100)


def nap():
    t.color("orange")
    t.width(5)
    t.speed(10)
    for side in range(10):
        t.forward(160)
        t.right(108)


def logo():
    t.color("blue")
    t.pensize(4)
    t.circle(99)
    t.color("red")
    t.pensize(2)
    t.left(60)
    t.forward(173)
    t.left(150)
    t.forward(200)
    t.right(150)
    t.forward(173)
    t.right(120)
    t.forward(173)
    t.right(150)
    t.forward(200)
    t.left(150)
    t.forward(173)
    t.color("black")


def haromszog():
    t.color("green")
    t.forward(45)
    t.left(120)
    t.forward(45)
    t.left(120)
    t.forward(45)


def negyszog():
    t.color("pink")
    t.forward(45)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(45)


virag()
