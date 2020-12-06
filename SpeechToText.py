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

engine = pt.init()
voices = engine.getProperty('voices')

if(text == 'hello'):
    engine.setProperty('voice', voices[1].id)
    engine.say("Hello sweety!")
    

elif(text == 'how are you'):
    engine.setProperty('voice', voices[0].id)
    engine.say("Awesome buddy, thanks")

engine.runAndWait()


# People on Windows may face problem with pyaudio I faced the same
# pip install pipwin
# pipwin install pyaudio
