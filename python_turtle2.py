# #turtle event listeners
# #when tapped a even something should happen
# import turtle
# import random

# screen = turtle.Screen()


# # def move_forward():
# #     tim.forward(10)

# # def move_backwards():
# #     tim.backward(10)

# # def turn_left():
    
# #     tim.left(10)

# # def turn_right():
# #     tim.right(10)
    
# # def clear():
# #     tim.clear()
# #     tim.penup()
# #     tim.home()    #turtle ko beech mein laata hai
# #     tim.pendown()

# # screen.listen()
# # screen.onkey(key="w" , fun = move_forward)    #space key se move hoga  # no move_forward()   def calculator(add):       #add is a function
# # screen.onkey(key='s',fun= move_backwards)
# # screen.onkey(key='a',fun= turn_left)
# # screen.onkey(key='d',fun= turn_right)

# # screen.onkey(fun = clear,key = "c")

# # w - forwards
# # s - backwards
# # a - counter-clockwise
# # d - clockwise

# #turtle racing

# screen.setup(width=500, height=400) #sets the screen size to height=400 and width=500
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
# colors = ["Purple", "Indigo", "red", "green","yellow","blue"]
# all_turtles =[]
# is_race_on = False

# y_positions = [-70,-40,-10,20,50,80]
# for turtle_index in range(0,6):
#     new_turtle = turtle.Turtle()
#     new_turtle.penup()
#     new_turtle.shape("turtle")
#     new_turtle.color(colors[turtle_index])
#     new_turtle.goto(x=-230, y=y_positions[turtle_index])
#     all_turtles.append(new_turtle)

# if user_bet:
#     is_race_on =True

# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on=False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You won, the {winning_color} turtle is the winner!")
#             else:
#                 print(f"You lost, the {winning_color} turtle is the winner!")
#         random_distance = random.randint(0,10)
#         turtle.forward(random_distance)


# new_turtle.screen.exitonclick()



#snake game
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import turtle
#run from this page
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)  #turning off the tracer by putting it 0  , with tracer we need to use update nhi toh output nhi dikhega 

snake = Snake()   #object of snake class
food = Food() #as soon as object is created food ka init() execute hoga
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,key='Up')     #Up - upward arrow keys
screen.onkey(snake.down,key='Down')
screen.onkey(snake.left,key='Left')
screen.onkey(snake.right,key='Right')
#creating a snake there will be 3 boxes each a turtle


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) #after 0.1 seconds the screen will get refreshed
    
    snake.move()

    #detect collision with food
    if snake.head.distance(food)<15:       #if food aur snake ka head distance kam hai toh snake ne touch kiya food ko  , food ka size 10 hai
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
     
    #detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor() < -280:
        game_is_on=False
        scoreboard.game_over()
   
    #detect collision with tail
    for segment in snake.segments[1:]:      #excepts the head
        if snake.head.distance(segment) <10:
            game_is_on=False
            scoreboard.game_over()
    #if head collision with any segment in the tail then gameover


screen.exitonclick()
