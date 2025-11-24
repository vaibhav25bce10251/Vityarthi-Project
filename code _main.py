import speech_recognition as sr
import win32com.client
import webbrowser
import os
from groq import Groq
import datetime
speaker = win32com.client.Dispatch("SAPI.SpVoice")
print("Hello I am ANANT AI")
speaker.Speak("Hello I am ANANT AI")
def takeCommand():
    r = sr.Recognizer()
    with (sr.Microphone() as source):
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query1 = r.recognize_google(audio, language='en-in')
            print(f"User said:{query1}")
            return query1
        except Exception:
            print("Sorry, didn't recognize your input")
            return "Sorry, didn't recognize your input"
while True:
    print("Listening...")
    query = takeCommand()
    if "Desktop Mode".lower() in query.lower():
        print("Desktop Mode activated")
        speaker.Speak("Desktop Mode activated")
    elif "Open Youtube".lower() in query.lower():
        webbrowser.open("https://www.youtube.com")
        print("Opening YouTube")
        speaker.Speak("Opening YouTube")
    elif "Open Wikipedia".lower() in query.lower():
        webbrowser.open("https://www.wikipedia.org")
        print("Opening Wikipedia")
        speaker.Speak("Opening Wikipedia")
    elif "Open Chess.com".lower() in query.lower():
        webbrowser.open("https://www.chess.com")
        print("Opening Wikipedia")
        speaker.Speak("Opening Chess.com sir")
    elif "Open Instagram".lower() in query.lower():
        webbrowser.open("https://www.instagram.com")
        print("Opening Instagram")
        speaker.Speak("Opening Instagram")
    elif "Open Browser".lower() in query.lower():
        webbrowser.open("https://www.google.com")
        print("Opening Browser")
        speaker.Speak("Browser opened")
    elif "the time".lower() in query.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M:%S ")
        print(f"Sir, the time is {strfTime}")
        speaker.Speak(f"Sir, the time is {strfTime}")
    elif "Favourite Agent".lower() in query.lower():
        musicPath = r"C:\Users\Vaibhav\Downloads\RENEGADE ⧸⧸ VALORANT x 99 GOD x C103 - Official Audio.mp4"
        os.startfile(musicPath)
    elif "Open File explorer".lower() in query.lower():
        webbrowser.open("")
        print("Opening File Explorer")
        speaker.Speak("Opening File Explorer")
    elif "Open Hollow Knight".lower() in query.lower():
        musicPath = r"D:\Hollow-Knight-Steamrip.com\Hollow Knight v1.5.78.11833\Hollow Knight.exe"
        os.startfile(musicPath)
        print("Opening Hollow Knight")
        speaker.Speak("Opening Hollow Knight")
    elif "Open Valorant".lower() in query.lower():
        musicPath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk"
        os.startfile(musicPath)
        print("Opening Valorant")
        speaker.Speak("Opening Valorant")
    elif "Open Aim labs".lower() in query.lower():
        musicPath = r"C:\Users\Vaibhav\Desktop\Aimlabs.url"
        os.startfile(musicPath)
        print("Opening Aimlabs")
        speaker.Speak("Opening Aimlabs")
    elif "Play Music".lower()in query.lower():
        print("Do you want to play downloaded music or from spotify ?")
        speaker.Speak("Do you want to play downloaded music or from spotify ?")
    elif "Spotify".lower() in query.lower():
        musicPath = r"C:\Users\Vaibhav\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk"
        os.startfile(musicPath)
        print("Opening Spotify")
        speaker.Speak("Opening Spotify")
    elif "Downloaded".lower() in query.lower():
        musicPath = r"C:\Users\Vaibhav\Downloads\One Direction - Night Changes.mp3"
        os.startfile(musicPath)
        print("Playing default downloaded music")
        speaker.Speak("Playing default downloaded music")
    elif "AI mode".lower() in query.lower():
        print("AI Mode activated")
        speaker.Speak("AI Mode activated")
        client = Groq(api_key="Your API key---can't enter mine in GITHUB its not allowing me") ###Generate API key from--- https://console.groq.com
        while True:
            print("Listening...")
            query = takeCommand()

            response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": query}
            ],
            temperature=1,
            max_completion_tokens=500,
            top_p=1
        )


            print(response)


            print("\nANANT:", response.choices[0].message.content)
            speaker.speak(response.choices[0].message.content)




