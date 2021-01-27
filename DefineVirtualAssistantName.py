import speech_recognition as sr

listener = sr.Recognizer()

name = 'alexa'

try:
    with sr.Microphone() as source:
        print("Hearing...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if name in command:
            print(command)
        else:
            print("My name is alexa. You need to tell my name, Then I understand you are talking to me.")

except:
    pass
