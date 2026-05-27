import whisper
import requests

# Step 1: Load Whisper model
print("Loading Whisper model...")
model = whisper.load_model("base")

# Step 2: Transcribe audio file
print("Transcribing audio...")
result = model.transcribe("patient_audio.wav")   # <-- put your audio file here
symptom_text = result["text"]
print("Patient said:", symptom_text)

# Step 3: Send text to Flask API
print("Sending to API...")
response = requests.post("http://127.0.0.1:5000/analyze",
                         json={"symptom": symptom_text})

# Step 4: Show structured medical report
print("API Response:", response.json())
