#Code and Debugges by Ankit Mishra --- Email at :- mankit490@gmail.com
#Enable less secure apps in Gmail , otherwise Gmail feature will not work

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #Microsoft Sppech API
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): #CREATED TO GET THE FEATURE , "WISH ME" WHILE STARTING.
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good evening")
    speak("I am Lucy sir. Designed by Ankit , Please tell me how may i help you")

def takecommand():
    #it will take command from user(from microphone of device) , currently in development stage as per marked by developer , so it may take extra time in recognition
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold = 1 #seconds(Here 1 second as default now) of non_speaking audio before a phrase is considered complete
        audio=r.listen(source)
    try:     #we may face error , so its better to have a backup read more in documentation
        print("Recognizing.. ")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query} \n") #Fstrings are similar tp formAT method in python.
    except Exception as e:
        #print(e) can be used if you want to show the error occured
        print("Say that again Please") #Just to make a good environment if recognition fails
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your password') #Might have security isuues.
    server.sendmail('youremail@gmail.com',to,content)
    server.close()


if __name__ == "__main__":

    wishMe()
    query= takecommand().lower() #To convert our speech into lower case letters and match query
    
    
    
    # Logic for executing our tasks.. !
    
    #-----Searching by " Question"+on wikipedia :
    if 'wikipedia' in query:
        speak('Searching Wikipedia..')
        query=query.replace('wikipedia', "")
        results= wikipedia.summary(query,sentences=2) #It will return two sentences from wikipedia.
        speak("According to wikipedia")
        print(results) #This will simply print the result
        speak(results) #This will simply speakout the results
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
    elif 'open ' in query:
        webbrowser.open("youtube.com")
    elif 'play music' in query:
        music_dir= 'E:\\song'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0])) #to make a shuffle play you can use random to create numbers.
    elif 'tell time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")
    elif 'open code' in query:
        codePath= "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath) #Os module helps us in opening file at a particluar position.
    elif 'email to harry' in query:
        try:
            speak("what should i say")
            content=takeCommand()
            to='ankkityt@gmail.com'
            sendEmail(to,content)
            speak("Email Has been sent")
            except Exception as e:
                speak("Sorry might have some network issues!")
    elif 'quit' in query:
        exit()
