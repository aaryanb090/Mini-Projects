import random
from turtle import Turtle, Screen

is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a color from"
                                                          " (red, orange, yellow, green, blue, purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-150, -100, -50, 0, 50, 100]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle is the winner.")
screen.exitonclick()
