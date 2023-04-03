import gtts
from playsound import playsound

tts=gtts.gTTS("Merhaba Arif, sana nasıl yardımcı olabilirim", lang="tr", slow=False)
tts.save("ses.mp3")
playsound("ses.mp3")
