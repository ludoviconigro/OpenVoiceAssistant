# core/intents.py

from skills.weather import handle_weather_query
from skills.calculator import handle_calculator

# importa tutte le liste delle parole chiave
from core.keywords import (
    calc_keywords,
    weather_keywords,
    greetings_keywords
)


def clean_text(text):
    """Rimuove duplicati consecutivi tipo 'roma roma' → 'roma'."""
    words = text.split()
    cleaned = []
    for w in words:
        if not cleaned or cleaned[-1] != w:
            cleaned.append(w)
    return " ".join(cleaned)


def handle_command(text: str) -> str:
    text = text.lower().strip()
    text = clean_text(text)

    # ============================================================
    # SALUTI
    # ============================================================
    if any(w in text for w in greetings_keywords):
        return "Dimmi pure, sono qui."

    # ============================================================
    # METEO
    # ============================================================
    if any(w in text for w in weather_keywords):
        return handle_weather_query(text)

    # ============================================================
    # CALCOLATRICE
    # ============================================================
    if any(k in text for k in calc_keywords):
        return handle_calculator(text)

    # simboli matematici → calcolatrice
    if any(c in text for c in "+-*/^()"):
        return handle_calculator(text)

    # ============================================================
    # NESSUN INTENTO RICONOSCIUTO
    # ============================================================
    if text == "":
        return "Non ho capito, puoi ripetere?"

    return "Per ora non so come aiutarti con questa richiesta."
