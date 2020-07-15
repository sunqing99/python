#!/usr/local/bin/python3

from turtle import *
import sys, math
register_shape('viv.gif')
shape('viv.gif')
radius = 350
points = int(sys.argv[1])
if points > 0:
  turn = 360.0 / points
  yoff = -radius
  side = 2.0 * radius * math.sin(math.pi / points)
else:
  turn = 180.0 * (1 - 1.0 / points)
  yoff = 0.0
  side = 2 * radius

color('red', 'yellow')
bgcolor('lightblue')
speed(8)
setup(width=1., height=1., startx=None, starty=None)
up()
setpos(-radius,yoff)
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
