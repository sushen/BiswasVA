import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

name = 'alexa'

def take_commend():
    try:
        with sr.Microphone() as source:
            print("Hearing...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if name in command:
                command = command.replace('alexa','')
                print(command)
            else:
                engine.say("I am alexa. You need to tell my name, Then I understand you are talking to me.")
                engine.runAndWait()

    except:
        pass

    return command

def run_alaxa():
    command = take_commend()
    # print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt('playing' + song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('time is ' + time)



run_alaxa()

