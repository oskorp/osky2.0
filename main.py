import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyaudio
import os
from translate import Translator
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import wolframalpha
from twilio.rest import Client


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


T=Translator(
from_lang = "English", to_lang = "Hindi"
)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 6:
        speak("Good Midnight")

    elif hour >= 6 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Hello sir")

    speak("I'm osky")
    speak("Please tell me how may i help you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('omkarkhandalkar846@gmail.com', 'Rakmo!@#123')
    server.sendmail('omkarkhandalkar846@gmail.com', to, content)
    server.close()


def main():
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)
            speak('According to wikipedia')
            speak(results)
            print(results)



        elif 'open college website' in query:
            webbrowser.open("mydy.dypatil.edu")

        elif 'start youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")



        elif 'open Linkedin' in query:
            speak("opening linkedin")
            webbrowser.open("Linkedin.com")

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif 'open dashboard' in query:
            speak("opening college website")
            webbrowser.open("http://mydy.dypatil.edu/rait/my/")

        elif 'open whatsapp' in query:
            speak("openign whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Sir, the time is {strTime}")



        elif 'email to omkar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "omkarkhandalkar846@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'translate' in query:
            query = query.replace('translate', '')
            translation = T.translate(query)
            speak(query)
            print(translation)
            speak(translation)

        elif 'joke' in query:
            print(joke())
            joke()


        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")




        elif 'cpu' in query:
            cpu()


        elif 'search youtube' in query:
            speak("Kya dekhna pasand karoge boss")
            search_video = takeCommand().lower()
            speak('Muje ye videos mili')
            webbrowser.open('https:/www.youtube.com/results/search_query=' + search_video)

        elif 'search google' in query:
            speak("Kya search karu janab?")
            search = takeCommand().lower()
            speak('wahh kya smart hu mein ye lijiye')
            webbrowser.open('https://www.google.com/webhp =' + search)

        elif 'find' in query:
            query = query.replace('find', '')
            location = query
            speak('Finding' + location)
            webbrowser.open('https:/www.google.com/maps/place/=' + location)



        elif "calculate" in query:

            app_id = "A7Y5GV-YT6RP2WPP3"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)


        elif "what is" in query or "who is" in query:

            client = wolframalpha.Client("A7Y5GV-YT6RP2WPP3")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")






root_1 = tk.ThemedTk()
root_1.set_theme('radiance')
root_1.title("Voice assistant")
root_1.geometry("400x350")
lbl1 = ttk.Label(master=root_1, text="Welcome to voice assistant app\n\n", wraplength=600)
lbl1.pack()
but1 = ttk.Button(root_1, text="Run the assistant🤖🔊", command=main)
but1.config(width=22)
but1.pack(padx=10, pady=10)
quit4 = ttk.Button(root_1, text="EXIT", command=root_1.destroy)
quit4.config(width=22)
quit4.pack(padx=10, pady=20)
root_1.mainloop()
