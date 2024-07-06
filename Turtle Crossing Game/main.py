from turtle import Screen
from player import Player
from car_manager import Cars
from score import Score
import time

screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Score()
car = Cars()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car.create_car()
    car.move_cars()

    if player.ycor() > 280:
        player.next_level()
        score.next_level()
        car.next_level()

    # Detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()