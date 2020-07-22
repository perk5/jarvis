import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

q = True
master = "Perk"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# print("initializing Jarvis")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak('Good Morning')
    elif hour >= 12 and hour <= 18:
        speak('Good Afternoon...')
    else:
        speak("good evening...")

    speak("i am jarvis.... how can i help you" + master)

    # speak("Hello There")
    

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')
    except Exception as e:
        print("Please say something....")
        query = "None"

    return query.lower()

# wishMe()
# query = takecommand()
while q:
    query = takecommand()
    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)
    elif 'open youtube' in query:
        url = 'https://www.youtube.com/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        q = False
    elif 'open facebook' in query:
        url = 'http://www.facebook.com/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        # webbrowser.open("facebook.com")
        q = False
    elif 'open google' in query:
        url = 'http://www.google.com/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        # webbrowser.open("facebook.com")
        q = False
    elif 'music' in query:
        songs_dir = 'C:\\Users\\91846\\Desktop\\my_music'
        songs = os.listdir(songs_dir)
        # print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
        q = False
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H-%M-%S")
        speak(f"{master} it's..{strTime}")
    elif 'thank' in query:
        speak('Welcome' + master)
    elif 'quit' in query:
        q = False
    elif 'maps' in query:
        url = 'https://www.google.com/maps/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        # webbrowser.open("facebook.com")
        q = False


