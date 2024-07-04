from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
   def __init__(self):
       super().__init__()
       self.shape("turtle")
       self.setheading(90)
       self.color("black")
       self.penup()
       self.goto(STARTING_POSITION)


   def move_up(self):
       x=self.xcor()
       y=self.ycor()
       self.goto(x,y+MOVE_DISTANCE)

   def move_down(self):
       x = self.xcor()
       y = self.ycor()
       self.goto(x, y - MOVE_DISTANCE)

