import speech_recognition as sr

import pyttsx3

recognizer = sr.Recognizer()
engine  = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__=="__main__":
    speak("Hey how may I help you")
    while True:
        r=sr.Recognizer()
        with sr.Microphone() as source :
            print("Listening...")
            audio=r.listen(source)




        print("Recognizing.....")
        try:
            command=r.recognize_google(audio)
            print(command)
     
        except Exception as e :
            print("Error , {0}" .format(e))        
