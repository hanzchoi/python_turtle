import turtle

CONST_SIZE = 50

def draw_triangle(point):

    point.forward(CONST_SIZE)
    point.left(120)
    point.forward(CONST_SIZE)
    point.left(120)
    point.forward(CONST_SIZE)

def draw_triforce(point):
    draw_triangle(point)
    point.left(120)
    point.forward(CONST_SIZE)
    draw_triangle(point)
    point.left(120)
    point.forward(CONST_SIZE)
    point.left(120)
    point.forward(CONST_SIZE)
    draw_triangle(point)

def draw_tri_triforce(point):
    draw_triforce(point)
    point.right(60)
    point.forward(CONST_SIZE)
    point.left(60)
    draw_triforce(point)
    point.left(120)
    point.forward(CONST_SIZE)
    point.left(60)
    point.forward(CONST_SIZE*2)
    point.right(180)
    draw_triforce(point)

def main():
    window = turtle.Screen()
    window.bgcolor("black")
    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("green")
    bob.speed(2)

    draw_tri_triforce(bob)

    window.exitonclick()



main()
