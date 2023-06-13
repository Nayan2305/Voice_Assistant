import pyttsx3 #pip install pyttsx3
import speech_recognition as sr 
import datetime #pre installed in the py program
import wikipedia 
import webbrowser #pip install webbrowser
import os #pre installed in the py program
import smtplib #pip install smtplib
import sys #pre installed in the py program
from pywikihow import search_wikihow 
import random #pre installed in the py program
import pyjokes 
import pywhatkit 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print (voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    ra = 'How are you sir?', 'Welcome back sir!', 'Nice to meet you again..', 'Any request sir?'
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("Hello. I am Natasha aka Natt.")
    speak(random.choice(ra))

         
def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")  

    except Exception as e:
        #print(e)
        print("Say that again please....!")
        speak("Say that again please....!")
        return "None"   
    return query    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hermoine.virtual.ai@gmail.com', 'Hermoine1321$')
    server.sendmail('hermoine.virttual.ai@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for exwcuting the task
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif  'open youtube' in query:
            webbrowser.open("youtube.com")

        elif  'hello google' in query:
            speak (" Hello sir, Please ask your question!")
            how = takeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        
        elif  'open google' in query:
            webbrowser.open("google.com")
        
        elif  'open gmail' in query:
            webbrowser.open("gmail.com")
        
        elif  'open college website' in query:
            webbrowser.open("www.viit.ac.in")


        # elif  'play music' in query:
        #     music_dir = 'G:\\jarvis_music'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))


        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("google search", "")
            query = query.replace("google", "")
            speak("Here is somthing I found on the internet")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query, 3)
                speak(result)

            except:
                speak("No data available. please try again!...")





        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Sir, the time is {strTime}")
            

        # elif 'open code' in query:
        #     codepath = "C:\\Users\\Samarth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codepath)

        # elif 'open minesweeper' in query:
        #     minesweeperpath = "C:\\Windows\\winsxs\\amd64_microsoft-windows-s..oxgames-minesweeper_31bf3856ad364e35_6.1.7600.16385_none_fe560f0352e04f48\\Minesweeper.exe"    
        #     os.startfile(minesweeperpath)


        # elif 'open card game' in query:
        #     cardgamepath = "C:\\Windows\\winsxs\\amd64_microsoft-windows-s..nboxgames-solitaire_31bf3856ad364e35_6.1.7600.16385_none_d1124c00155dfd14\\Solitaire.exe"    
        #     os.startfile(cardgamepath)

        # elif 'open chess' in query:
        #     chesspath = "C:\\Windows\\winsxs\\amd64_microsoft-windows-s..iuminboxgames-chess_31bf3856ad364e35_6.1.7600.16385_none_d0c99374981840d5\\Chess.exe"    
        #     os.startfile(chesspath)

        
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "ritesh.ksingh1311@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry email was not sent")

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif "thank you" in query:
            speak("Thank you sir, Have a nice day")
            sys.exit()



