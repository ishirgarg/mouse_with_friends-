# import board
# import digitalio
# import time

# # left encoder
# a = digitalio.DigitalInOut(board.GP12)
# b = digitalio.DigitalInOut(board.GP13)

# counter = 0
# position = 0
# a_prev = a.value

# def leftEncoderRisingEdge():
#     global position # access global position
#     if a.value == 1 and b.value == 0:
#         position += 1
#     elif a.value == 1 and b.value == 1:
#         position -= 1

# while True:
#     a_val = a.value
#     if a_val and not a_prev: # rising edge
#         leftEncoderRisingEdge()
#     a_prev = a_val

#     if counter % 1000 == 0:
#         print(position)
#     counter += 1

import board
import time
import rotaryio

enc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)

while True:
    print(enc.position)
    time.sleep(0.001)
