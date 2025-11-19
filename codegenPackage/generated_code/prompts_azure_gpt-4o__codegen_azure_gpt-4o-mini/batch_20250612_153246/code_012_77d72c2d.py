"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: Write code to implement multilingual marketing strategies for a website, using vernacular language support as described by Rankraze.
Generated: DETERMINISTIC_77d72c2d7be78357
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from flask import Flask, request, jsonify, render_template
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)

# Configure supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'es', 'fr', 'de', 'zh']

# Initialize Babel for language support
babel = Babel(app)

# Load translations from JSON files
def load_translations():
    translations = {}
    for lang in app.config['BABEL_SUPPORTED_LOCALES']:
        try:
            with open(f'translations/{lang}.json', 'r', encoding='utf-8') as file:
                translations[lang] = json.load(file)
        except FileNotFoundError:
            print(f"Warning: Translation file for '{lang}' not found.")
        except json.JSONDecodeError:
            print(f"Error: JSON decoding failed for '{lang}' translation file.")
    return translations

# Store translations in a global variable
translations = load_translations()

# Function to get the user's preferred language
@babel.localeselector
def get_locale():
    # Check if the user has specified a language in the request
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

# Route for the homepage
@app.route('/')
def home():
    # Render the homepage with the appropriate translations
    return render_template('index.html', translations=translations[get_locale()])

# API endpoint to get marketing content in the user's language
@app.route('/api/marketing-content', methods=['GET'])
def get_marketing_content():
    try:
        lang = get_locale()
        content = translations.get(lang, translations['en'])  # Fallback to English if language not found
        return jsonify(content), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Ensure the translations directory exists
    if not os.path.exists('translations'):
        os.makedirs('translations')
    app.run(debug=True)
```

### Example Translation Files
- Create a directory named `translations` and add JSON files for each language, e.g., `en.json`, `es.json`, etc.

#### Example `en.json`
```json
{
    "welcome": "Welcome to our website!",
    "description": "We offer a variety of products to suit your needs."
}
```

#### Example `es.json`
```json
{
    "welcome": "¡Bienvenido a nuestro sitio web!",
    "description": "Ofrecemos una variedad de productos para satisfacer sus necesidades."
}
```

### Note
- Ensure Flask and Flask-Babel are installed in your environment. You can install them using:
```bash
pip install Flask Flask-Babel
```
