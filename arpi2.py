import turtle
def star(turtle, n,r):
 for k in range(0,n):
    turtle.pendown()
    turtle.forward(r)
    turtle.penup()
    turtle.backward(r)
    turtle.left(360/n)
fred = turtle.Turtle() 
def recursive_star(turtle, n, r, depth, f):
 if depth == 0:
    star(turtle, n, f*4)
 else:
    for k in range(0,n):
        turtle.pendown()
        turtle.forward(r)
        recursive_star(turtle, n, f*r, depth - 1,f)
        turtle.penup()
        turtle.backward(r)
        turtle.left(360/n)
 
fred = turtle.Turtle()
fred.speed("fastest")
recursive_star(fred, 5 , 150, 4, 0.4)
 
import turtle
import random
fred = turtle.Turtle()
 
fred.speed(10)
 
colors=['lavender', 'pink', 'blue', 'midnight blue', 'lime']
 