import turtle
wn = turtle.Screen()

def draw_line(angle):
    mike = turtle.Turtle()
    mike.left(angle)
    mike.left(90)
    mike.forward(90)
    mike.left(90)
    mike.forward(90)
    mike.left(90)
    mike.forward(90)
    mike.left(90)
    mike.forward(180)
    mike.right(90)
    mike.forward(90)
    mike.right(90)
    mike.forward(90)
    mike.right(90)
    mike.forward(180)
    mike.right(90)
    mike.forward(90)
    mike.right(90)
    mike.forward(90)
    mike.right(90)
    mike.forward(180)
    mike.left(90)
    mike.forward(90)
    mike.left(90)
    mike.forward(90)
    mike.left(90)
    mike.forward(90)

def square(lines):
    for angle in range(0, 180, int(180/lines)):
        draw_line(angle)
        
square(5)

wn.exitonclick()
