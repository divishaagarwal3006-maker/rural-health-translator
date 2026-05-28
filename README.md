# 🩺 Rural Health Translator

> **AI-powered tool that converts simple patient language into structured medical reports for doctors — supporting 10+ Indian languages.**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=flat-square&logo=flask)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-orange?style=flat-square)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)

---

## 🌍 Problem It Solves

In rural India, patients describe symptoms in local languages like Hindi, Tamil, Telugu, Bengali etc. Doctors — especially those visiting from cities — often struggle to understand these descriptions accurately. This tool bridges that gap instantly.

**Patient says:** `"mera pet mein bahut dard hai aur ulti aa rahi hai"`

**Doctor sees:**
- Chief Complaint: Abdominal pain with emesis
- Possible Diagnosis: Gastroenteritis / Peptic Ulcer / Appendicitis
- Urgency: Urgent
- Full clinical note in medical English
- Recommended tests
- Patient explanation back in Hindi

---

## ✨ Features

- 🎙️ **Voice input** — patient speaks, Whisper AI transcribes
- 🌐 **10+ Indian languages** — Hindi, Bengali, Telugu, Tamil, Marathi, Gujarati, Kannada, Malayalam, Punjabi, Urdu
- 🤖 **AI medical translation** — powered by LLaMA 3.3 70B via Groq
- 📋 **Structured medical report** — chief complaint, diagnosis, urgency, clinical note, tests
- 🌙 **Dark mode UI** — clean, mobile-friendly interface
- ⚡ **Fast & Free** — Groq free tier, no credit card needed
- 📖 **Medical dictionary** — built-in symptom mapping for common terms

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Backend | Python + Flask |
| AI Model | LLaMA 3.3 70B (via Groq API) |
| Voice Transcription | OpenAI Whisper (base model) |
| Frontend | HTML + CSS + Vanilla JS |
| Medical Dictionary | Custom JSON mapping |

---

## 📁 Project Structure

```
rural_chatbot/
├── static/
│   └── index.html          # Frontend UI (dark mode)
├── app.py                  # Flask server + API routes
├── pipeline.py             # Voice → text → medical pipeline
├── voice_to_text.py        # Whisper transcription module
├── medical_map.json        # Symptom dictionary (Hindi + English)
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment config
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- ffmpeg installed ([download here](https://ffmpeg.org/download.html))
- Free Groq API key ([get here](https://console.groq.com))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/rural_chatbot.git
cd rural_chatbot

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Groq API key in app.py
# Find this line and paste your key:
# GROQ_API_KEY = "gsk_your_key_here"

# 5. Run the app
python app.py
```

### Usage

1. Open `http://127.0.0.1:5000` in your browser
2. Select the patient's language
3. Type or speak the symptoms
4. Click **Generate Medical Report**
5. Share the structured report with the doctor

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Serves the web UI |
| `/translate` | POST | Text → medical report |
| `/transcribe` | POST | Audio file → text |

### Example `/translate` request:
```json
POST /translate
{
  "symptom": "mera pet mein dard hai",
  "language": "Hindi"
}
```

### Example response:
```json
{
  "chiefComplaint": "Abdominal pain",
  "possibleDiagnosis": "Gastritis / Peptic Ulcer / Appendicitis",
  "urgency": "Urgent",
  "medicalNote": "Patient presents with abdominal pain...",
  "recommendedTests": "- Complete Blood Count\n- Urine analysis\n- Abdominal ultrasound",
  "patientExplanation": "Aapke pet mein sujan ho sakti hai...",
  "originalText": "mera pet mein dard hai"
}
```

---

## 📦 Requirements

```
flask
flask-cors
openai-whisper
groq
torch
```

---

## 🌱 Future Improvements

- [ ] Mobile app (Android) for field use
- [ ] Patient history tracking
- [ ] Offline mode with smaller AI model
- [ ] Print-ready PDF report generation
- [ ] Doctor dashboard with patient queue
- [ ] Integration with government health schemes (Ayushman Bharat)

---

## 🤝 Contributing

Pull requests are welcome! This project aims to improve healthcare access in rural India. For major changes, please open an issue first.

---

## 📄 License

MIT License — free to use, modify and distribute.

---

## 👨‍💻 Author

Built with ❤️ for rural India's healthcare workers.

> *"Technology should reach those who need it most."*