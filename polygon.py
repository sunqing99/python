#!/usr/local/bin/python3

from turtle import *
import sys
side = 200
points = int(sys.argv[1])
if points > 0:
  turn = 360.0 / points
  yoff = -side
else:
  turn = 180.0 * (1 - 1.0 / points)
  yoff = 0.0
  side *= 2

color('red', 'yellow')
up()
setpos(-side,yoff)
home=pos()
down()

begin_fill()
while True:
    forward(side)
    left(turn)
    if distance(home) < 1:
        break
end_fill()
done()
