# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle
import webbrowser

def draw_triangle():

    window = turtle.Screen()
    window.bgcolor("red")

    bob = turtle.Turtle()
    bob.shape("triangle")
    bob.color("green")
    bob.speed(2)
    bob.forward(100)
    bob.left(120)
    bob.forward(100)
    bob.left(120)
    bob.forward(100)
    window.exitonclick()

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    window.exitonclick()

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow" , "green")
    brad.speed(3)
    for i in range(0, 4):
        brad.forward(100)
        brad.right(90)

    window.exitonclick()

def main():
    webbrowser.open("https://www.youtube.com/watch?v=cGufy1PAeTU") 
