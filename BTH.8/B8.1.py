import turtle
print("Nguyen Van An")
print("Msv:235752021610082")
def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")
    
    pen = turtle.Turtle()
    pen.color("blue")
    pen.pensize(2)

    for _ in range(4):
        pen.forward(100)
        pen.right(90)

    window.mainloop()

draw_square()
