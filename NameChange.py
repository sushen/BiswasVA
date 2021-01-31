import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import random
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def replaceName():
    try:
        with sr.Microphone() as source:
            print("Hearing...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'shahrukh' in command:
                replaceShahrukh = command.replace('shahrukh','alexa')
                print(replaceShahrukh)
    except:
        pass

    return command

# name = 'alexa' or replaceName()

alexa_voice = [
    "You need to tell my name , Then I understand you are talking to me.",
    "Can you tell my name?, Then I understand you are talking to me. ",
    "Are you talking to me?, Please start With my mame."
]


def take_commend():
    try:
        with sr.Microphone() as source:
            print("Hearing...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if replaceName() in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass

    return command


def run_alaxa():
    command = take_commend()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt('playing' + song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('time is ' + time)

    elif 'wikipedia' in command:
        persion = command.replace('wki', '')
        info = wikipedia.summary(persion, 2)
        print(info)
        talk(info)
    elif 'search' in command:
        searchelement = command.replace('search', '')
        googleSearch = pywhatkit.search(searchelement)
        print(googleSearch)
        talk('searching' + searchelement)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'stop' in command:
        sys.exit()


    else:
        alexa_request = random.choice(alexa_voice)
        engine.say(alexa_request)
        print(alexa_request)


while True:
    run_alaxa()

