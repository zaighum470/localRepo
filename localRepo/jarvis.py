import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize the speech engine
engine = pyttsx3.init()

# Set voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use [1] for female voice if available

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could not understand. Please say that again.")
        return "None"
    return query.lower()

def run_assistant():
    wish_user()
    while True:
        query = take_command()

        if 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

run_assistant()