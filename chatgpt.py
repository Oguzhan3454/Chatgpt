import openai
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
import pyttsx3
import pyaudio
import time

language = "tr"

def speak(string):
    speech = gTTS(text=string, lang="tr", slow=False)
    file= "answer.mp3"
    speech.save(file)
    playsound(file)
    os.remove(file)

openai.api_key = ""

r = sr.Recognizer()

def record(ask=False):
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
            print(voice)
        except sr.UnknownValueError:
            print("Anlaşılamadı.")
        except sr.RequestError as e:
            print("Hata:", e)
        return voice

# Google Asistan'ın cevap vereceği metni almak için:


def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while 1:
    assistant_response = record()
    print(assistant_response)

    if("cik" in assistant_response):
        break

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": assistant_response}],
        max_tokens=1024,
    )

    

    response = completion.choices[0].message["content"]

    print(response)
    speak(response)