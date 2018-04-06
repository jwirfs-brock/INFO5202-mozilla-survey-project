from microbit import *
import speech

from microbit import *

#Russia
while True:
    if pin2.is_touched():
        display.show(Image.HAPPY)
        speech.say("V P N ...", speed=120, pitch=100, throat=100, mouth=200)
        sleep(600)
        speech.say("Connected Devices ...", speed=120, pitch=100, throat=100, mouth=200)
        sleep(600)
        speech.say("D D O S ...", speed=120, pitch=100, throat=100, mouth=200)
        sleep(600)
        speech.say("Tor ...", speed=120, pitch=100, throat=100, mouth=200)
        sleep(600)
        speech.say("Bot net ...", speed=120, pitch=100, throat=100, mouth=200)
        sleep(600)
        speech.say("Block chai ...", speed=120, pitch=100, throat=100, mouth=200)
        sleep(50000)
    else:
        display.show(Image.COW)
