# Turtle race
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place Bet", prompt="Which turtle win win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    turtles.append(new_turtle)

y_position = -100

for turtle in turtles:
    turtle.penup()
    turtle.goto(-240, y_position)
    y_position += 30



screen.exitonclick()
