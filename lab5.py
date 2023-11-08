import board
import time
import rotaryio
from math import pi

lenc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)
renc = rotaryio.IncrementalEncoder(board.GP19, board.GP18)

ENCODER_TICKS_PER_REVOLUTION = 200
WHEELBASE_DIAMETER = 82.0
WHEEL_DIAMETER = 34.0 # mm

while True:
    left_dist  = pi * WHEEL_DIAMETER * lenc.position / 200
    right_dist = pi * WHEEL_DIAMETER * renc.position / 185 

    dist  = 0.5 * (left_dist + right_dist)
    theta = (right_dist - left_dist) / WHEELBASE_DIAMETER

    print(dist, theta)
    time.sleep(0.05)

