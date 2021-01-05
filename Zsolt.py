import turtle
t = turtle.Turtle()
def valami():
  t.speed(0)
  t.hideturtle()
  t.pendown()
  for x in range (50):
    t.circle(80,90)
    if x % 2 == 0:
      t.circle(60,100)
valami()