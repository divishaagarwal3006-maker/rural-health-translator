from flask import Flask, request, jsonify
import spacy, json

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Load dictionary
with open("medical_map.json", "r") as f:
    medical_map = json.load(f)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("symptom", "").lower()

    # Check dictionary
    for phrase, medical_term in medical_map.items():
        if phrase in text:
            return jsonify({"original": text, "medical_term": medical_term})

    # Fallback: NLP entity extraction
    doc = nlp(text)
    return jsonify({"original": text, "medical_term": [ent.text for ent in doc.ents]})

if __name__ == "__main__":
    app.run(debug=True)
