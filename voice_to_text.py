import whisper

model = whisper.load_model("base")
result = model.transcribe("patient_audio.wav")  # record audio first
print("Patient said:", result["text"])
