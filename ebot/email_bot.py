import smtplib
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('sreeram.vishal1@gmail.com','Arsenal14!$')
    server.sendmail('sreeram.vishal1@gmail.com',
                    'sreeram.vishal@gmail.com',
                    'Hi! This is just a test message. Please ignore.')

def get_email_info():
    engine_talk("To whom do you want to send the Email to")
    name = get_info()
    engine_talk("What would the subject be")
    subject = get_info()
    engine_talk("What is the message that you'd like to be conveyed")
    message = get_info()
get_email_info()
