"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
<<<<<<< HEAD
        speed.x = (x + 210) / 25
        speed.y = (y + 210) / 25

=======
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10
>>>>>>> 0844657d37e7405e7f3a319b259e10819da9e4f6

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
<<<<<<< HEAD
        dot(20, 'yellow')
=======
        #Targets negros JOE
	dot(20, 'black')
>>>>>>> 0844657d37e7405e7f3a319b259e10819da9e4f6

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'green')

    update()


def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        # increased moving target speed Sebastian 
        target.x -= 2.5

    if inside(ball):
    #aumentar gravedad JOE (antes estaba en 0.35)
        speed.y -= 0.5
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return
    # increased ball speed Sebastian 
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
