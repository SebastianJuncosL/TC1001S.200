"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    # Expanded boundaries by 1
    return -201 < head.x < 19`1 and -201 < head.y < 191


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
       #Solo muestra puntajes de 5 en 5 JOE 
        if len(snake)%5==00:
           print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
<<<<<<< HEAD
        square(body.x, body.y, 9, 'green')
=======
       #Cambio de color JOE (hubo conflict)
        square(body.x, body.y, 9, 'black')
>>>>>>> 0844657d37e7405e7f3a319b259e10819da9e4f6

    square(food.x, food.y, 9, 'brown')
    update()
    # Increased snake speed Sebastian
    ontimer(move, 200)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'D')
onkey(lambda: change(-10, 0), 'A')
onkey(lambda: change(0, 10), 'W')
onkey(lambda: change(0, -10), 'S')
move()
done()
