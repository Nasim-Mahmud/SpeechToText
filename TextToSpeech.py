import pyttsx3 as pt
from pyttsx3 import voice
engine = pt.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.say("Picchi keeeeea maaarr")
engine.setProperty('voice', voices[0].id)
engine.say("Parmu naa, Tui marr")
engine.runAndWait()