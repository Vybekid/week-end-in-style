import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

colors = ["#FF0000", "#9400D3","#FFFF00","#4B0082",  "#FF7F00", "#0000FF",   "#00FF00",  ]

sides = 3
for i in range(150):
    pen.pencolor(colors[i % sides]) 
    pen.forward(i * 3)              
    pen.left(360 / sides + 1)       
    pen.width(i / 50 + 1)           

turtle.done()