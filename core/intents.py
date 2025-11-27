# core/intents.py

from skills.weather import handle_weather_query


def clean_text(text):
    """
    Rimuove parole duplicate consecutive tipo:
    'roma roma' → 'roma'
    """
    words = text.split()
    cleaned = []
    for w in words:
        if not cleaned or cleaned[-1] != w:
            cleaned.append(w)
    return " ".join(cleaned)


def handle_command(text: str) -> str:
    """
    Analisi base dell'intento.
    """
    text = text.lower().strip()
    text = clean_text(text)

    # Intent saluti
    if any(k in text for k in ["ciao", "grazie", "ok", "ehi", "hey"]):
        return "Dimmi pure, sono qui."

    # Intent METEO
    if any(k in text for k in [
        "tempo", "meteo", "clima",
        "piove", "pioggia",
        "neve", "nevica",
        "vento", "ventoso",
        "fa caldo", "fa freddo",
        "percepita"
    ]):
        return handle_weather_query(text)

    if text == "":
        return "Non ho capito, puoi ripetere?"

    return "Per ora non so come aiutarti con questa richiesta."
