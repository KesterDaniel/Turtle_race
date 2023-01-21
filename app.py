# Turtle race
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

still_playing = True
wallet = 1000


def game():
    global still_playing
    global wallet
    game_on = False
    user_bet = screen.textinput(title="Place Bet", prompt="Which turtle win win the race?")
    user_stake = screen.numinput(title="Stake", prompt="What's your stake?")
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

    if user_bet and user_stake:
        game_on = True

    while game_on and still_playing:
        moving_turtle = random.choice(turtles)
        rand_distance = random.randint(0, 10)
        moving_turtle.forward(rand_distance)
        if moving_turtle.xcor() > 230:
            game_on = False
            winning_color = moving_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won the race")
                wallet += user_stake
                print(wallet)
            else:
                print(f"You lost! The {winning_color} turtle won the race")
                wallet -= user_stake
                print(wallet)
        if wallet == 0:
            still_playing = False
    screen.clearscreen()


while still_playing:
    game()

screen.exitonclick()
