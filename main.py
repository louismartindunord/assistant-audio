import speech_recognition as sr
import pyttsx3 as ttx

listener = sr.Recognizer()
engine=ttx.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', 'french')

with sr.Microphone() as source:
    print("parler maintenant")
    audio = listener.listen(source)
    command = listener.recognize_google(audio, language='fr-FR')
                
engine.say(command)
engine.runAndWait()

