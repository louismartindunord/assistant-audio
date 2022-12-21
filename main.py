import speech_recognition as sr
import pyttsx3 as ttx

listener = sr.Recognizer()
engine=ttx.init(driverName='nsss')
voices = engine.getProperty("voices")




try:
    with sr.Microphone() as source:
        print("parler maintenant")
        audio = listener.listen(source)
        command = listener.recognize_google(audio)
        engine.runAndWait

        print('test :',command)
        engine.say(command)
        
except:
    pass 


 #afficher la liste des micros disponibles
        #print(sr.Microphone.list_microphone_names())