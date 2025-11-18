"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-tradegptapp.com
Prompt: Develop a multilingual user interface for a trading app like TradeGPT, supporting languages such as English, Spanish, French, Dutch, and Italian.
Generated: DETERMINISTIC_28ed8185b57c8ccf
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load language files
def load_language_file(language):
    try:
        with open(f'languages/{language}.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Supported languages
SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'nl', 'it']

# Default language
DEFAULT_LANGUAGE = 'en'

@app.route('/')
def index():
    # Determine the user's preferred language
    lang = request.args.get('lang', DEFAULT_LANGUAGE)
    if lang not in SUPPORTED_LANGUAGES:
        lang = DEFAULT_LANGUAGE

    # Load the corresponding language file
    translations = load_language_file(lang)
    if translations is None:
        return jsonify({"error": "Language not supported"}), 400

    return render_template('index.html', translations=translations)

@app.route('/api/translate', methods=['POST'])
def translate():
    data = request.get_json()
    
    # Validate input data
    if not data or 'lang' not in data or 'text' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    lang = data['lang']
    if lang not in SUPPORTED_LANGUAGES:
        return jsonify({"error": "Language not supported"}), 400
    
    # Load translations for the requested language
    translations = load_language_file(lang)
    if translations is None:
        return jsonify({"error": "Language not found"}), 404
    
    # Translate the text if available
    translated_text = translations.get(data['text'], data['text'])  # Fallback to original text
    return jsonify({"translated_text": translated_text}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Language JSON Files Structure
#### Example - languages/en.json
```json
{
    "welcome": "Welcome to TradeGPT!",
    "buy": "Buy",
    "sell": "Sell",
    "error": "An error occurred"
}
```

#### Example - languages/es.json
```json
{
    "welcome": "¡Bienvenido a TradeGPT!",
    "buy": "Comprar",
    "sell": "Vender",
    "error": "Ocurrió un error"
}
```

### Note
- To run the code, make sure to create the `languages` folder and add the respective JSON files for each language.
- Install Flask using `pip install flask` to run the application.
