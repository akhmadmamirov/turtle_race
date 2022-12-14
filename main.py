from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500,400)

user_bet =  screen.textinput('Make your bet', 'Which turtle w ill win the race? Enter a color: ')
colors = ['red', 'green', 'orange', 'yellow', 'blue', 'purple']
y_post = [-100, -60, -20, 20, 60, 100]

all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_post[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True 


while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() >230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You have won! The {winning_color} turtle is the winner!')
            else:
                print(f'You have lost! The {winning_color} turtle is the winner!')
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()