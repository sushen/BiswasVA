import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

name = 'alexa'

try:
    with sr.Microphone() as source:
        print("Hearing...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if name in command:
            talk(command)
        else:
            engine.say("I am alexa. You need to tell my name, Then I understand you are talking to me.")
            engine.runAndWait()

except:
    pass
