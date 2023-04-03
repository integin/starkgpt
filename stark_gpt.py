import openai
import speech_recognition as sr
import pygame
import gtts
from api_secret import API_KEY

### Api keyinizi "api_secret.py" dosyasından çeker
openai.api_key = API_KEY
pygame.mixer.init()

## device_index = 1 yazan yere kend icihaz numaranızı girin
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
print(sr.Microphone.list_microphone_names())



conversation = ""
user_name = "Sahip"

while True:
    with mic as source:
        print("Dinliyor...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("Dinleme beklemede.")

    try:
        user_input = r.recognize_google(audio, language="tr")
        print("Sahibin ifadesi:", user_input)
    except Exception as e:
        print(e)
        continue

    prompt = user_name+": "+user_input+"\nBot:"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    response_str = response["choices"][0]["text"].strip()

    print(response_str)

    tts = gtts.gTTS(str(response_str), lang="tr")
    tts.save("ses.mp3")

    pygame.mixer.music.load("ses.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue
