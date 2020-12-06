import pyttsx3 as pt
from pyttsx3 import voice
engine = pt.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.say("Hello, My name is Sara, and you?")
engine.setProperty('voice', voices[0].id)
engine.say("Hey, I am Pirate, nice to meet you Sara")

engine.runAndWait()