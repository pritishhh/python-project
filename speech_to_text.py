import speech_recognition as sr
import bot_action

def speech_to_text():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
      voice_data=""
      voice_data =r.recognize_google(audio)
      print(voice_data)
      return voice_data
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError:
        print("Request error")
    
speech_to_text() 