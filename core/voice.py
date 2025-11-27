import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import soundfile as sf
import tempfile
from config import LANGUAGE

engine = pyttsx3.init()

def speak(text: str):
    print(f"[ASSISTENTE]: {text}")
    engine.say(text)
    engine.runAndWait()


def record_audio(duration=7, samplerate=16000):
    print("Parla...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    # salva audio temporaneo
    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    sf.write(tmpfile.name, audio, samplerate)
    return tmpfile.name


def listen() -> str:
    recognizer = sr.Recognizer()

    # registra audio usando sounddevice
    audio_path = record_audio()

    # converti a oggetto SpeechRecognition
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language=LANGUAGE)
        print(f"[TU]: {text}")
        return text.lower()
    except Exception as e:
        print("Errore riconoscimento:", e)
        return ""
