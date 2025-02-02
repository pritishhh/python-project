import text_to_speech
import speech_to_text
import datetime
import weather
import webbrowser


def Action(data):
    user_data = data.lower()

    if "what is your name " in user_data:
       text_to_speech.text_to_speech("My name is virtual assistant ")
       return "My name is virtual assistant"

    elif "hello" in user_data or "hey" in user_data:
       text_to_speech.text_to_speech("hello,sir how i can help you ")
       return "hello,sir how i can help you "

    elif "good morning" in user_data:
       text_to_speech.text_to_speech("good morning sir") 
       return "good morning sir"
   
    elif "time now" in user_data:
       current_time=datetime.datetime.now()
       Time=(str)(current_time)+"Hour :",(str)(current_time.minute)+"Minute"
       text_to_speech.text_to_speech(Time)
       return Time
   
    elif"shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"
        
    elif"play music" in user_data:
        webbrowser.open("http://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is reay for you sir ")
        return "gaana.com is ready for u sir "
        
    elif "open youtube" in user_data:
        webbrowser.open("http://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is reay for you sir ")
        return "youtube.com is ready for u sir "
    
    elif "open google" in user_data:
        webbrowser.open("http://google.com/")
        text_to_speech.text_to_speech("google.com is reay for you sir ")
        return "google.com is ready for u sir "
    
    elif "weather" in user_data:
        ans= weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
    
    elif "good afternoon" in user_data:
        text_to_speech.text_to_speech("good afternoon sir")
        return "good afternoon sir"
    
    else:
       text_to_speech.text_to_speech("i m not able to understand")
       return "i m not able to understand"

