import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

colors = ["#EA53D9", "#55D8EA", "#18EA1C"]

sides = 3
for i in range(150):
    pen.pencolor(colors[i % sides]) 
    pen.forward(i * 3)              
    pen.left(360 / sides + 1)       
    pen.width(i / 50 + 1)           

turtle.done()