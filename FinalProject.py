import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)
value = random.randint(0, 247)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour < 18:
        speak("goon afternoon!")

    else:
        speak("good evening!")

    speak("i am EDITH sir. how i can help you ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("say that again please....")
        return"none"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia.......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play songs' in query:
            music_dir = 'F:\\English Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[value]))

        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            print(strTime)

        elif 'attention' in query:
            music_dir = 'F:\\English Songs\\a'
            songs = os.listdir(music_dir)
            
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'hello' in query:
            speak("hello sir. how i can help")

        elif 'open code' in query:
            codePath = "C:\\Users\\prajw\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open Firefox' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox"
            os.startfile(codePath)


        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif 'quit' in query:
            exit()

        elif "how are you" in query:
            speak("I'm fine, glad you me that")    
         
        elif "who are you" in query:
            speak("I am your virtual assistant created by Prajwal")  
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
            
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'joke' in query:
            speak(pyjokes.get_joke()) 

        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")