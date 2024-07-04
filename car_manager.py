from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
       super().__init__()
       self.cars = []
       self.game_on=True



    def generate_position(self):
        y=random.randint(-280,280)
        position=(0,y)
        return position

    def set_color(self):
        r=random.random()
        g=random.random()
        b=random.random()
        color=(r,g,b)
        return color

    def move(self):
        for car in self.cars:
            x=car.xcor()
            y=car.ycor()
            car.goto(x,y-STARTING_MOVE_DISTANCE)
    def initialize_car(self,car):
        car.shape("square")
        car.setheading(180)
        car.penup()
        car.color(self.set_color())
        car.goto(self.generate_position())


    def generate_cars(self):

        while self.game_on:
            choice = random.randint(1, 5)

            if choice==5:
             car=Turtle()
             self.initialize_car(car)
             self.cars.append(car)

            self.move()



