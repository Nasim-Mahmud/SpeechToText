# People on Windows may face problem with pyaudio I faced the same
# pip install pipwin
# pipwin install pyaudio

import pyttsx3 as pt
from pyttsx3 import voice
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:

    print('Speak anything: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))

    except:
        print('Sorry, not clear')

