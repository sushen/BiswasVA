import speech_recognition as sr
import pyttsx3
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("I am alaxa")
engine.say("What I can do for you.")
engine.runAndWait()

name = 'alexa'

alexa_voice = [
    "You need to tell my name , Then I understand you are talking to me.",
    "Can you tell my name?, Then I understand you are talking to me. ",
    "Are you talking to me?, Please start With my mame."
]

try:
    with sr.Microphone() as source:
        print("Hearing...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if name in command:
            print(command)
        else:
            alexa_request = random.choice(alexa_voice)
            engine.say(alexa_request)
            print(alexa_request)
            engine.runAndWait()

except:
    pass
