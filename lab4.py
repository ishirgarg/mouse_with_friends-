import board
import time
import digitalio
from analogio import AnalogIn

l_en  = digitalio.DigitalInOut(board.GP7)
l_en.direction = digitalio.Direction.OUTPUT
l_adc = AnalogIn(board.GP28)
l_a   = digitalio.DigitalInOut(board.GP5)   
l_a.direction  = digitalio.Direction.OUTPUT
l_a.drive_mode = digitalio.DriveMode.OPEN_DRAIN
l_a.value = True # high Z mode

l_b =  digitalio.DigitalInOut(board.GP6)
l_b.direction  = digitalio.Direction.OUTPUT
l_b.drive_mode = digitalio.DriveMode.OPEN_DRAIN
l_b.value = True # high Z mode




while True:
    # TODO enable IR emitters using l_en
    l_en.value = True
    # TODO enable chosen sensor l_a or l_b
    l_a.value = False
    # TODO wait a bit
    time.sleep(0.1)
    # TODO take analog reading for future printing
    reading = l_adc.value
    # TODO disable chosen sensor l_a or l_b
    l_a.value = True
    # TODO disable IR emitters using l_en
    l_en.value = False
    time.sleep(0.05)
    print(reading)
