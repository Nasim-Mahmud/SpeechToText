import pyttsx3 as pt
from pyttsx3 import voice
engine = pt.init()
voices = engine.getProperty('voices')

# Changing the gender of voice to female
engine.setProperty('voice', voices[1].id) 
engine.say("Hello, My name is Sara, and you?")

# Changing the gender of voice to male
engine.setProperty('voice', voices[0].id)
engine.say("Hey, I am Pirate, nice to meet you Sara")

engine.runAndWait()