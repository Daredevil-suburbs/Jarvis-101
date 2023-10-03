import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
        except:
            print("Sorry, I couldn't understand you.")
            text = ""
            
    return text.lower()

# Define function to perform tasks based on user command
def perform_task(command):
    if "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(result)
    elif "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com/")
    elif "what time is it" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")
    elif "open code" in command:
        speak("Opening Visual Studio Code...")
        os.startfile("C:\\Users\\<username>\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

# Main program loop
while True:
    command = recognize_speech()
    if "jarvis" in command:
        perform_task(command)
    elif "stop" in command:
        speak("Goodbye!")
        break
