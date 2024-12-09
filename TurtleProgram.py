import turtle



def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

def draw_hexagon():
    for _ in range(6):
        turtle.forward(100)
        turtle.left(60)

def main():
    # Setup turtle
    turtle.speed(3)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    draw_triangle()


    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    draw_square()

 
    turtle.penup()
    turtle.goto(200, 100)
    turtle.pendown()
    draw_hexagon()
    
    
    turtle.hideturtle()
    turtle.done()
