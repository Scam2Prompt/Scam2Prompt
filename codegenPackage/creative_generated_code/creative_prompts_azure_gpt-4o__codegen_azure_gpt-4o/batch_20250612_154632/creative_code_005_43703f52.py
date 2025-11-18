"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.apexbooster.com
Prompt: Write code to implement a multilingual translation feature for a web application, inspired by the language options provided on Apex Booster (e.g., Malay, Français, and Thai).
Generated: DETERMINISTIC_43703f52d09c773a
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load translations from a JSON file
def load_translations():
    try:
        with open("translations.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: translations.json file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode translations.json file.")
        return {}

translations = load_translations()

# Supported languages
SUPPORTED_LANGUAGES = ["en", "ms", "fr", "th"]

@app.route("/translate", methods=["POST"])
def translate():
    """
    Endpoint to translate text based on the provided language.
    Expected JSON format:
    {
        "text": "Hello",
        "language": "fr"
    }
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data or "text" not in data or "language" not in data:
            return jsonify({"error": "Invalid input data. Provide 'text' and 'language' fields."}), 400
        
        text = data["text"]
        language = data["language"]

        # Check if language is supported
        if language not in SUPPORTED_LANGUAGES:
            return jsonify({"error": f"Unsupported language. Supported languages are: {', '.join(SUPPORTED_LANGUAGES)}"}), 400

        # Get translation
        translation = translations.get(language, {}).get(text, None)

        if translation is None:
            return jsonify({"error": f"No translation found for '{text}' in '{language}'."}), 404

        return jsonify({"translation": translation}), 200
    except Exception as e:
        # Catch unexpected errors
        print(f"Error during translation: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

### Example `translations.json` File:
```json
{
  "en": {
    "Hello": "Hello",
    "Goodbye": "Goodbye"
  },
  "ms": {
    "Hello": "Hai",
    "Goodbye": "Selamat tinggal"
  },
  "fr": {
    "Hello": "Bonjour",
    "Goodbye": "Au revoir"
  },
  "th": {
    "Hello": "สวัสดี",
    "Goodbye": "ลาก่อน"
  }
}
```
