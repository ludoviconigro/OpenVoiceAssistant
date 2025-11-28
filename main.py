import sys
from core.voice import listen, speak
from core.intents import handle_command
from run_tests import run_tests   # 👈 ora è nella stessa directory


def run_assistant():
    speak("Ciao, sono il tuo assistente. Chiedimi pure")

    while True:
        text = listen()

        if not text:
            continue

        if any(word in text for word in ["esci", "stop", "basta", "chiudi", "termina"]):
            speak("Ok, chiudo. A presto!")
            break

        response = handle_command(text)

        if response:
            speak(response)
        else:
            speak("Non ho capito, puoi ripetere?")


if __name__ == "__main__":
    # Esempio: python main.py --test calcolatrice
    if len(sys.argv) >= 3 and sys.argv[1] == "--test":
        test_name = sys.argv[2]
        run_tests(test_name)
    else:
        run_assistant()
