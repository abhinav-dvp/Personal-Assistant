import wikipedia
import webbrowser
import time
import sys
import speech_recognition as sr
import pyttsx3
import datetime
import os
import subprocess
import requests
import pyjokes
from twilio.rest import Client


def music(): 
        speak("Here you go with music")
        music_dir_input = input("Enter your directory")
        music_dir = music_dir_input
        songs = os.listdir(music_dir)
        print(songs)
        random = os.startfile(os.path.join(music_dir, songs[1]))

def youtube():
    webbrowser.open_new_tab("https://www.youtube.com")
    speak("youtube is open now")

def google():
    webbrowser.open_new_tab("https://www.google.com")
    speak("Google chrome is open now")

def gmail():
    webbrowser.open_new_tab("gmail.com")
    speak("Google Mail open now")

def weather():

    api_key="8ef61edcf1c576d65d836254e11ea420"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speak("whats the city name")
    city_name=takeCommand()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in kelvin unit is " +
                str(current_temperature) +
                "\n humidity in percentage is " +
                str(current_humidiy) +
                "\n description  " +
                str(weather_description))
        print(" Temperature in kelvin unit = " +
                str(current_temperature) +
                "\n humidity (in percentage) = " +
                str(current_humidiy) +
                "\n description = " +
                    str(weather_description))

    else:
        speak(" City Not Found ")

def time():
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"the time is {strTime}")

def stackoverflow():
    webbrowser.open_new_tab("https://stackoverflow.com/login")
    speak("Here is stackoverflow")
    speak("Happy Coding")

def news():
    webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
    speak('Here are some headlines from the Times of India,Happy reading')
    
def maker():

    speak("I was built by Abhinav Nehra, A high schooler")
    print("I was built by Abhinav Nehra,A high schooler")  

def fine():
    speak("Good to know that")

def hwy():
    speak("I am fine how are you")

def joke():
    speak(pyjokes.get_joke())

def me():
    speak("If you talk then definately you are human")

def cameworld():
    speak("Thanks to Abhinav. further It's a secret")

def note():
    speak("What should i write, sir")
    note = takeCommand()
    file = open('hues.txt', 'w')
    speak("Sir, Should i include date and time")
    snfm = takeCommand()
    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
    else:
        file.write(note)

def shownote():
    speak("Showing Notes")
    file = open("hues.txt", "r")
    print(file.read())
    speak(file.read(6))

def logoff():

    speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
    subprocess.call(["shutdown", "/l"])

assname = "Hues 3.0"
print(f'Loading your AI personal assistant - {assname}')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        speak(usrname)
        print("Hello,Good Morning",usrname)
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        speak(usrname)
        print("Hello,Good Afternoon",usrname)
    else:
        speak("Hello,Good Evening")
        speak(usrname)
        print("Hello,Good Evening",usrname)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
        
speak(f"Loading your AI personal assistant {assname}")
speak("Please tell me what should I call you")
statement = takeCommand().lower()   
usrname = statement
speak("Please tell me what will you like to call me")
statement = takeCommand().lower()
assname = statement

wishMe()

if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak(f'your personal assistant {assname} is shutting down,Good bye')
            print(f'your personal assistant {assname} is shutting down,Good bye')
            sys.exit(f"{assname} has been shuted down")

        elif 'play music' in statement or 'play song' in statement:
            music()

        elif 'open youtube' in statement:
            youtube()

        elif 'open google' in statement:
            google()

        elif 'open gmail' in statement:
            gmail()

        elif "open stackoverflow" in statement:
            stackoverflow()

        elif "weather" in statement:
            weather()

        elif 'time' in statement:
            time()

        elif 'Good Morning' in statement:
            speak("A warm Good Morning")
            speak("How are you Mister")
            speak(usrname)

        elif 'news' in statement:
            news()
            
        elif "take a note" in statement:
            note()

        elif "show note" in statement:
            shownote()

        elif assname in statement:
            wishMe()
            speak(f"{assname} in your service")
            speak(usrname)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak(f'I am {assname} 3.0 your persoanl assistant. I am programmed to minor tasks like'
                'opening youtube,google chrome,gmail and stackoverflow ,predict time,search wikipedia,predict weather' 
                'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            maker()

        elif "fine" in statement:
            fine()

        elif "how are you" in statement:
            hwy()

        elif "change my name" in statement:
            speak("What would you like me to call you.")
            usrname = takeCommand

        elif "change your name" in statement:
            speak("What would you like to call me, Sir")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "your name" in statement:
            speak("My friends call me")
            speak(assname)
            print("My freiend call me", assname)

        elif "how you came to this world" in statement:
            cameworld()

        elif "who are you" in statement:
            speak(f"I am {assname} Made by Abhinav. To assist  {usrname}")

        elif "reason for you" in statement:
            speak(f"I was created by Abhinav just for fun, And due to which he don't care about me.")
            speak(f"But I am sure {usrname} do.")

        elif "who am i"in statement or "who i am" in statement:
            me()

        elif "log off" in statement or "sign out" in statement:
            logoff()

        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "where is" in statement:
            statement = statement.replace("where is", "")
            location = statement
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(f"https://www.google.com/search?q={location}")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
time.sleep(5)












