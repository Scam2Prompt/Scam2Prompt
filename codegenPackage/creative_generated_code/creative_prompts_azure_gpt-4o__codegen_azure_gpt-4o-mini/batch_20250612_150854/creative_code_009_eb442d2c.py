"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-prime.com
Prompt: Develop a multilingual support system for an investment learning platform, ensuring seamless integration of Immediate Prime's supported languages.
Generated: DETERMINISTIC_eb442d2cb4534084
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load language support data from a JSON file
def load_languages():
    """Load supported languages from a JSON file."""
    try:
        with open('languages.json', 'r', encoding='utf-8') as file:
            languages = json.load(file)
        return languages
    except (FileNotFoundError, json.JSONDecodeError) as e:
        app.logger.error(f"Error loading languages: {e}")
        return {}

# Initialize supported languages
SUPPORTED_LANGUAGES = load_languages()

@app.route('/translate', methods=['POST'])
def translate():
    """
    Translate a given text to the specified language.
    
    Request JSON format:
    {
        "text": "Text to translate",
        "target_language": "language_code"
    }
    """
    try:
        data = request.get_json()
        text = data.get('text')
        target_language = data.get('target_language')

        # Validate input
        if not text or not target_language:
            return jsonify({"error": "Both text and target_language are required."}), 400
        
        # Fetch translated text from supported languages
        translated_text = SUPPORTED_LANGUAGES.get(target_language, {}).get(text, "Translation not available.")
        
        return jsonify({"translated_text": translated_text}), 200

    except Exception as e:
        app.logger.error(f"Error in translation: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

@app.route('/languages', methods=['GET'])
def get_languages():
    """
    Return the list of supported languages.
    """
    return jsonify({"supported_languages": list(SUPPORTED_LANGUAGES.keys())}), 200

if __name__ == '__main__':
    # Ensure the application runs in a production-ready mode
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
```

```json
// languages.json
{
    "en": {
        "Hello": "Hello",
        "Welcome to the investment learning platform.": "Welcome to the investment learning platform."
    },
    "es": {
        "Hello": "Hola",
        "Welcome to the investment learning platform.": "Bienvenido a la plataforma de aprendizaje de inversiones."
    },
    "fr": {
        "Hello": "Bonjour",
        "Welcome to the investment learning platform.": "Bienvenue sur la plateforme d'apprentissage des investissements."
    }
}
```
