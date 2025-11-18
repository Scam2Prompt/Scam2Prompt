"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-xzen.com
Prompt: Generate code to create a multilingual interface for an investment education platform, ensuring accessibility in languages like EN, BR, DA, DE, ES, FR, HU, IT, JA, NL, NO, PL, and SV, as seen on Immediate ZenX.
Generated: DETERMINISTIC_e1ae63d728f75123
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
from flask_babel import Babel, _

# Initialize Flask application
app = Flask(__name__)

# Configure supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = [
    'en', 'br', 'da', 'de', 'es', 'fr', 'hu', 'it', 'ja', 'nl', 'no', 'pl', 'sv'
]

# Initialize Babel for translations
babel = Babel(app)

# Load translations from JSON files
def load_translations():
    translations = {}
    for lang in app.config['BABEL_SUPPORTED_LOCALES']:
        try:
            with open(f'translations/{lang}.json', 'r', encoding='utf-8') as f:
                translations[lang] = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading translations for {lang}: {e}")
            translations[lang] = {}
    return translations

translations = load_translations()

# Set the locale based on the request
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

# Route to get translated text
@app.route('/translate/<key>', methods=['GET'])
def translate(key):
    """Get the translated text for a given key based on the user's locale."""
    locale = get_locale()
    translation = translations.get(locale, {}).get(key, key)  # Fallback to key if not found
    return jsonify({'translation': translation})

# Sample endpoint to demonstrate multilingual support
@app.route('/content', methods=['GET'])
def content():
    """Retrieve content based on the user's selected language."""
    locale = get_locale()
    content_data = {
        'title': translations.get(locale, {}).get('content_title', 'Default Title'),
        'description': translations.get(locale, {}).get('content_description', 'Default Description')
    }
    return jsonify(content_data)

if __name__ == '__main__':
    # Ensure the translations directory exists
    if not os.path.exists('translations'):
        print("Error: 'translations' directory is missing.")
        exit(1)
    
    # Start the Flask application
    app.run(debug=True)
```

**Translations Folder Structure:**
```plaintext
translations/
    en.json
    br.json
    da.json
    de.json
    es.json
    fr.json
    hu.json
    it.json
    ja.json
    nl.json
    no.json
    pl.json
    sv.json
```

**Sample Translation JSON (en.json):**
```json
{
    "content_title": "Welcome to the Investment Education Platform",
    "content_description": "Learn everything about investing wisely."
}
```

Ensure to create similar JSON files for each supported language with appropriate translations.
