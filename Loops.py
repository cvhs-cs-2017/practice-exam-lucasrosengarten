"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""

import turtle
n = turtle.Turtle()
for i in range(100):
    turtle.speed(0)
    turtle.forward(50)
    turtle.right(85)
turtle.done()
