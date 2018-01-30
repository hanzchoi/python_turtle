from turtle import*

def sierpinski(l, n):
    if n == 0:
        begin_fill()
        forward(l)
        left(120)
        forward(l)
        left(120)
        forward(l)
        left(120)
        end_fill()
    else:
        sierpinski(l/2, n-1)
        forward(l/2)
        sierpinski(l/2, n-1)
        left(120)
        forward(l/2)
        right(120)
        sierpinski(l/2, n-1)
        right(120)
        forward(l/2)
        left(120)

speed(10)
range = 6
sierpinski(600, range)
window.exitonclick()
