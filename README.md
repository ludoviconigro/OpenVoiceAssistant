# 📘 **README.md** — *OpenVoiceAssistant*

```markdown
# 🎤 OpenVoiceAssistant  
Un assistente vocale modulare, open-source e completamente locale.  
Gestisce comandi vocali, meteo, automazioni e nuove skill personalizzate.



## 🧩 Aggiungere nuove skill

1. Crea un file in `/skills/`:

```python
def handle_timer(text):
    return "Timer avviato!"
```

2. Importalo in `core/intents.py`:

```python
from skills.timer import handle_timer
```

3. Associa le parole chiave:

```python
if "timer" in text:
    return handle_timer(text)
```

Ed è subito attiva 🔥

---

## 🌍 API e Servizi Gratuiti Utilizzati

* **Open-Meteo Geocoding API**
* **MET Norway Weather API**
* **ipapi.co + ipwho.is** per localizzazione IP
* **SpeechRecognition + sounddevice**
* **pyttsx3** per TTS locale

Tutto totalmente gratuito e senza limiti.

---

## 💡 Perché OpenVoiceAssistant?

✔ 100% gratuito
✔ Modulare come Alexa
✔ Estendibile con nuove skill
✔ Ottimizzato per Mac ARM
✔ Nessun servizio a pagamento
✔ Nessun cloud obbligatorio

---

## 🤝 Contributi

Pull-request, idee e nuove skill sono benvenute!

---

## 📜 Licenza

MIT License — libero uso, modifica e distribuzione.

---

## 👤 Autore

**Ludovico Nigro**
Etical Hacker & Developer

