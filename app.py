# Turtle race
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place Bet", prompt="Which turtle win win the race?")
print(user_bet)

timmy = Turtle(shape="turtle")
timmy.penup()

timmy.goto(-240, -100)


screen.exitonclick()
