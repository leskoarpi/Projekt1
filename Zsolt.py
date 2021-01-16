import turtle
t = turtle.Turtle()
def valami():
  t.speed(0)
  t.hideturtle()
  t.pendown()
  for x in range (80):
    t.circle(100,110)
    if x % 2 == 0:
      t.circle(80,120)
valami()