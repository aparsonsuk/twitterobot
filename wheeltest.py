import explorerhat

from time import sleep

from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


def forw (channel,event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backwards(100)
    explorerhat.output.one.on()
    sleep(1)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.output.one.fade(100,0,2)
    message = ("i've moved forward")
    twitter.update_status(status=message)
    print ("Tweeted: %s" % message)

def back (channel,event):
    explorerhat.motor.one.backwards(100)
    explorerhat.motor.two.forward(100)
    explorerhat.output.one.on()
    sleep(1)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.output.one.fade(100,0,2)
    message = ("i've moved backwards")
    twitter.update_status(status=message)
    print ("Tweeted: %s" % message)

def left (channel,event):
    explorerhat.motor.one.backwards(100)
    explorerhat.motor.two.backwards(100)
    explorerhat.output.one.on()
    sleep(1)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.output.one.fade(100,0,2)

def right (channel,event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.forwards(100)
    explorerhat.output.one.on()
    sleep(1)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.output.one.fade(100,0,2)
    

explorerhat.touch.one.pressed(forw)
explorerhat.touch.two.pressed(back)
explorerhat.touch.three.pressed(left)
explorerhat.touch.four.pressed(right)
