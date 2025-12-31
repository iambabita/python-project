import turtle
turtle.speed(16)
turtle.bgcolor('black')
turtle.color('red','pink')
turtle.pensize(3)
def curve():
 for i in range(200):
  turtle.right(1)
  turtle.forward(1)
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()
turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
