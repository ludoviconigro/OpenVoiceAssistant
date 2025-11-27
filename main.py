from core.voice import listen, speak
from core.intents import handle_command

def main():
    speak("Ciao, sono il tuo assistente. Chiedimi pure")

    while True:
        text = listen()

        if not text:
            continue

        # Comandi per uscire
        if any(word in text for word in ["esci", "stop", "basta", "chiudi", "termina"]):
            speak("Ok, chiudo. A presto!")
            break

        # Gestione generale dei comandi (meteo + altro)
        response = handle_command(text)

        if response:
            speak(response)
        else:
            speak("Non ho capito, puoi ripetere?")

if __name__ == "__main__":
    main()
