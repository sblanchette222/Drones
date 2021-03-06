from djitellopy import tello

import KeyPressModule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


def flip_left(self):
    self.flip("l")


def getkeyboardinput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getkey("LEFT"):
        lr = -speed
    elif kp.getkey("RIGHT"):
        lr = speed

    if kp.getkey("UP"):
        fb = speed
    elif kp.getkey("DOWN"):
        fb = -speed

    if kp.getkey("w"):
        ud = speed
    elif kp.getkey("s"):
        ud = -speed

    if kp.getkey("a"):
        speed
    elif kp.getkey("d"):
        -speed

    if kp.getkey("q"):  me.land()
    if kp.getkey("e"):  me.takeoff()
    if kp.getkey("x"): me.flip_left()

    return [lr, fb, ud, yv]


me.takeoff()
while True:
    vals = getkeyboardinput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
