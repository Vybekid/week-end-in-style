import turtle

screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0) # Set the drawing speed to the fastest
pen.hideturtle()

# Define a vibrant rainbow color palette
colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]

# Drawing loop
sides = 7 # The number of points on the star
for i in range(150):
    pen.pencolor(colors[i % sides]) # Cycle through the rainbow colors
    pen.forward(i * 3)              # Move forward by an increasing amount
    pen.left(360 / sides + 1)       # Turn to create the star's points
    pen.width(i / 50 + 1)           # Gradually increase the line width

# Keep the window open until it's closed
turtle.done()