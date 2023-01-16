import speech_recognition as sr
import pyttsx3 as ttx

listener = sr.Recognizer()
engine=ttx.init()
voices = engine.setProperty('voice', 'french')
from commandes.play_musique import musique_spotify



try :
    with sr.Microphone() as source:
        print("parler maintenant")
        audio = listener.listen(source)
        command = listener.recognize_google(audio, language='fr-FR')
    
    if "joue la musique" in command:
        musique = command.replace("joue la musique",'')
        musique_spotify(musique)

except:
   command = "Commande non reconnue"



                  
engine.runAndWait()

