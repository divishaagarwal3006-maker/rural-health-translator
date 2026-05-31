from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
import json, os, re

app = Flask(__name__, static_folder='static')
CORS(app)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # ✅ safe, reads from Render env
client = Groq(api_key=GROQ_API_KEY)

with open("medical_map.json", "r") as f:
    medical_map = json.load(f)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    symptom_text = data.get("symptom", "").strip()
    language = data.get("language", "English")

    if not symptom_text:
        return jsonify({"error": "No symptom text"}), 400

    quick_match = None
    for phrase, term in medical_map.items():
        if phrase in symptom_text.lower():
            quick_match = term
            break

    prompt = f"""You are a medical assistant for rural healthcare in India.
Patient said (in {language}): "{symptom_text}"
Dictionary hint: {quick_match or 'none'}

Reply with ONLY this JSON, no markdown, no backticks, no extra text:
{{"chiefComplaint":"medical term for complaint","possibleDiagnosis":"diagnosis1 / diagnosis2 / diagnosis3","urgency":"Routine or Urgent or Emergency","medicalNote":"clinical note in medical terms 3-4 sentences","recommendedTests":"- test1\\n- test2\\n- test3","patientExplanation":"simple explanation in {language}"}}"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )
        raw = response.choices[0].message.content
        raw = re.sub(r'```json', '', raw)
        raw = re.sub(r'```', '', raw)
        raw = raw.strip()
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            raw = match.group()
        report = json.loads(raw)
        report["originalText"] = symptom_text
        return jsonify(report)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))