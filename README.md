# 📘 OpenVoiceAssistant

Assistente Vocale Locale con Moduli Espandibili

## 🧠 Cos’è OpenVoiceAssistant

**OpenVoiceAssistant** è un assistente vocale modulare e completamente locale sviluppato in Python.
È progettato per rispondere a comandi in linguaggio naturale, funzionare in tempo reale e garantire la massima privacy possibile.
Il sistema permette di aggiungere facilmente nuove funzionalità tramite moduli dedicati (“skills”).

---

## 💻 Ambiente di Sviluppo

Il progetto viene attualmente sviluppato su:

* **MacBook Air**
* macOS
* Python (in ambiente virtuale `venv`)
* Sistema audio integrato (microfono + output vocale)

Funziona correttamente anche su macchine leggere, senza GPU, grazie all’uso di librerie offline per voce e parsing.

---

## 🎯 Cosa può fare l’assistente

L’assistente è basato su un sistema di **intenti**: ogni richiesta viene interpretata e instradata verso la “skill” più adatta.

Attualmente sono disponibili:

### 🔢 Modulo **Calcolatrice Avanzata**

Gestisce operazioni matematiche di varia complessità, usando linguaggio naturale o simbolico.
Include funzioni matematiche, conversioni, costanti e combinatoria.
➡️ Questo modulo è progettato per essere espandibile con facilità.

### 🌦️ Modulo **Meteo**

Il modulo meteo fornisce informazioni meteorologiche attuali:

* nella tua **posizione geografica automatica**, ottenuta localmente
* oppure per una città indicata nella richiesta

➡️ Anche questo modulo è estendibile (previsioni, allerte, ecc.).

### 🗣️ Sistema **Vocale**

* riconoscimento vocale locale
* sintesi vocale delle risposte
* interazione continua

---

## 🧪 Sistema di Test Integrato

Il progetto include un sistema automatico di test per verificare ogni skill.

### 📁 File di test

I file si trovano nella cartella:

```
tests/
   tests_calcolatrice.txt
   tests_meteo.txt
```

Ogni file contiene una lista di frasi, una per riga.

### 🔧 Script di test

Lo script è:

```
run_tests.py
```

ed è nella stessa directory di `main.py`.

### ▶️ Come eseguire i test

Puoi eseguire i test in base al modulo che vuoi verificare:

```
python main.py --test calcolatrice
```

oppure:

```
python main.py --test meteo
```

Il programma selezionerà automaticamente il file nella cartella `tests/`.

---

## 🚀 Come si avvia l’assistente

### ▶️ Modalità Assistente Vocale

```
python main.py
```

Avvierà l’ascolto tramite microfono e risponderà vocalmente.

### ▶️ Modalità Test

```
python main.py --test <nome_test>
```

Esempi:

* `python main.py --test calcolatrice`
* `python main.py --test meteo`

---

## 📂 Struttura del progetto

```
core/
   intents.py          → sistema di riconoscimento degli intenti
   keywords.py         → parole chiave per la classificazione
   voice.py            → input/output vocale
skills/
   calculator.py       → modulo calcolatrice
   weather.py          → modulo meteo
   location.py         → gestione posizione
tests/
   tests_calcolatrice.txt
   tests_meteo.txt
config.py
main.py
run_tests.py
```

---

## 🏁 Stato del progetto

✔ Architettura modulare
✔ Skills principali funzionanti
✔ Gestione vocale stabile
✔ Sistema test configurato
✔ Facilmente espandibile

---

