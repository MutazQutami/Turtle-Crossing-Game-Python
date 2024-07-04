

# #Declaration of blocks
# blocks = []
#
#
# game_is_on=True
#
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     random_chance = random.randint(1, 3)
#
#     #Generating blocks
#     if random_chance==2:
#       new_block = Block()
#       blocks.append(new_block)
#
#
#     #Turtle block collision
#     for block in blocks:
#         block.move()
#         if  block.xcor() in range (-48,48) and turtle.distance(block)<10:
#             game_is_on=False
#         if block.xcor()<-340:
#             blocks.remove(block)
#
#     #Turlte wins the round
#     if turtle.ycor()>290:
#         screen.clear()
#         blocks=[]
#         turtle=declare_turtle()
#
#
#
#
#
#
# screen.exitonclick()
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()

#Control turtle movement
screen.listen()
screen.onkeypress(player.move_up,"Up")
screen.onkeypress(player.move_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()



screen.exitonclick()