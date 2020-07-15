#!/usr/local/bin/python3

from turtle import *
import sys
register_shape('viv.gif')
shape('viv.gif')
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
setup(width=1., height=1., startx=None, starty=None)
up()
setpos(-side,yoff)
home=pos()
down()

begin_fill()
while True:
    forward(side)
    stamp()
    left(turn)
    if distance(home) < 1:
        break
end_fill()
done()
