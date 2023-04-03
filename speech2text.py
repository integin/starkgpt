import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone(device_index=1) as source:
    print("Lütfen Konuşun")
    audio=r.listen(source)

try:
    print("İfadeniz:"+r.recognize_google(audio, language="tr"))
except sr.UnknownValueError:
    print("Sesinizi Algılayamadım")
except sr.RequestError as e:
    print("Dediğinizi anlamadım: {0}".format(e))
