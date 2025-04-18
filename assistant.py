import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 180)


def parle(text):
    engine.say(text)
    engine.runAndWait()



def ecoute():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        commande = r.recognize_google(audio, language='fr-FR')
        return commande
    except sr.UnknownValueError:
        parle("Je n'ai pas compris")
        return ''
    except sr.RequestError:
        parle('Pas de service')
        return ''



parle('Bonjour, je suis votre assistant')

while True:
    commande = ecoute().lower()

    if 'bonjour' in commande:
        parle('Bonjour, comment allez vous ?')
    elif 'au revoir' in commande:
        parle('Au revoir')
        break
    elif 'heure' in commande:
        maintenant = datetime.datetime.now().strftime('%H:%M')
        parle('Il est ' + maintenant)


