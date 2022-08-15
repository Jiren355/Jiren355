from http import server
from logging import exception
from random import random
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening Sir!")
      
    speak ("Allow me to intruduce my self i am jarvis. How May I Help You")
    print ("Allow me to intruduce my self i am jarvis. How May I Help You?") 
     
def takecommand():
    #it takes microphone inpur from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
           
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language=('en-in'))
        print(f"user said:{query}\n")
        
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "none"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp,gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('fg47566@gmail.com','mbmcvqjwtipsiamj')
    server.sendmail('shahriarmostofafahim@gmail.com')
    server.close()
    
if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()
        # logic for executing takes based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Acording to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("Google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")
        
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            
        elif 'tell me about yourself' in query:
            speak('I am jarvis. I am an Ai robot created By Shahriar Mostofa Fahim and I love cookies')
            print('I am jarvis. I am an Ai robot created By Shahriar Mostofa Fahim and I love cookies')
            
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        
        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime}")
            print(f"Sir the time is {strtime}")
        
        elif 'open vs code' in query:
            codepath = "C:\\Users\\shahr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'send email to fahim' in query:
            try:
                speak("what should I say?")
                content = takecommand()
                to = "shahriarmostofafahim@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry i am unable to send an email at this moment")
        
        elif 'thank you' in query:
            speak('You are welcome')
            print('You are welcome')
        
        elif 'goodbye jarvis' in query:
            speak("Goodbye sir")
            print("Goodbye sir")
        elif 'open my channel' in query:
            webbrowser.open("www.youtube.com//c//HeyItzShahriar")
        
        elif 'say hello' in query:
            speak("Hello")
            print("Hello")
        
        elif 'favourite song' in query:
            webbrowser.open('www.youtube.com//watch?v=0OGguI0uDfE')
        
        elif 'go to infra website' in query:
            webbrowser.open('http://portal.infra.edu.bd/')
       
        
        
        