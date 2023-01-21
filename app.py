# Turtle race
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)


game_on = False
user_bet = screen.textinput(title="Place Bet", prompt="Which turtle win win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y_position = -100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-240, y_position)
    y_position += 30
    turtles.append(new_turtle)


if user_bet:
    game_on = True


while game_on:
    moving_turtle = random.choice(turtles)
    rand_distance = random.randint(0, 10)
    moving_turtle.forward(rand_distance)
    if moving_turtle.xcor() > 230:
        game_on = False
        winning_color = moving_turtle.pencolor()
        if winning_color == user_bet:
            print(f"You won! The {winning_color} turtle won the race")
        else:
            print(f"You lost! The {winning_color} turtle won the race")


screen.exitonclick()
