import speech_recognition as sr
import pyttsx3
import webbrowser
import pyaudio


recognizer = sr.Recognizer()
engine=pyttsx3.init()

"""musiclibrary={
    "sad":"https://youtu.be/AX6OrbgS8lI?feature=shared",
    "supreme":"https://youtu.be/AX1zRInC_TA?feature=shared",
    "wavy":"https://youtu.be/XTp5jaRU3Ws?feature=shared"
}"""
def processcommand(c):
   if "open youtube" in c.lower():
       webbrowser.open("https://youtube.com")
   elif "open facebook" in c.lower():
       webbrowser.open("https://facebook.com")
   elif "open google" in c.lower():
       webbrowser.open("https://google.com")
   elif "open instagram" in c.lower():
       webbrowser.open("https://instagram.com") 
   elif (c.lower().startswith("play wavy")):
      webbrowser.open("https://youtu.be/XTp5jaRU3Ws?feature=shared")

      
       

   """ c.lower().startswith("play"):
      song =c.lower.split("")[1]
      link =musiclibrary.music[song]
      webbrowser.open(link)"""



def speak(text):
  engine.say(text)
  engine.runAndWait()

  
if __name__== "__main__":
    speak("initializing jarvis....")

while True:
    r =sr.Recognizer()
    print("recognizing...")
    try:
       with sr.Microphone() as source:
           print("listening...")
           audio= r.listen(source,timeout=2,phrase_time_limit=1)
       word =r.recognize_google(audio)
       if (word.lower()=="jarvis"):
          speak("yes how can i help you")
          with sr.Microphone() as source:
             print("jarvis acrive!")
             audio = r.listen(source)
             command =r.recognize_google(audio)

             processcommand(command)

             
    except  Exception as e:
       print("error:{0}".format(e))
       