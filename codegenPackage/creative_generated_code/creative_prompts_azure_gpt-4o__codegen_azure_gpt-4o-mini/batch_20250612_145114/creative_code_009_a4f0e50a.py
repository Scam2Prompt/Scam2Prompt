"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finprofm.com
Prompt: Write code to integrate multilingual support (e.g., English and Français) into a trading platform, similar to FinProfm's language options.
Generated: DETERMINISTIC_a4f0e50af904b934
Batch ID: 20250612_145114
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

# Load localization data from JSON files
def load_localization_data():
    try:
        with open('locales/en.json', 'r', encoding='utf-8') as file:
            english = json.load(file)
        
        with open('locales/fr.json', 'r', encoding='utf-8') as file:
            french = json.load(file)
        
        return {
            'en': english,
            'fr': french
        }
    except FileNotFoundError as e:
        app.logger.error(f"Localization file not found: {e}")
        return {}
    except json.JSONDecodeError as e:
        app.logger.error(f"Error decoding JSON: {e}")
        return {}

# Initialize localization data
localization_data = load_localization_data()

@app.route('/')
def index():
    # Get the user's preferred language, defaulting to English
    language = request.args.get('lang', 'en')
    
    # Validate the language option
    if language not in localization_data:
        language = 'en'
    
    # Render the index template with localized strings
    return render_template('index.html', strings=localization_data[language])

@app.route('/api/translate', methods=['POST'])
def translate():
    """
    Endpoint for translating strings based on user input
    """
    data = request.get_json()

    # Check for language and text to translate
    if 'lang' not in data or 'text' not in data:
        return jsonify({'error': 'Missing language or text parameter'}), 400
    
    language = data['lang']
    text = data['text']
    
    # Validate the language option
    if language not in localization_data:
        return jsonify({'error': 'Unsupported language'}), 400
    
    # Return the translated string
    translated_text = localization_data[language].get(text, text)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**Example JSON files (locales/en.json and locales/fr.json):**

**en.json**
```json
{
    "welcome": "Welcome to the Trading Platform",
    "logout": "Logout",
    "balance": "Your balance is"
}
```

**fr.json**
```json
{
    "welcome": "Bienvenue sur la plateforme de trading",
    "logout": "Déconnexion",
    "balance": "Votre solde est"
}
```

**Template (templates/index.html):**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Trading Platform</title>
</head>
<body>
    <h1>{{ strings.welcome }}</h1>
    <p>{{ strings.balance }}: $1000</p>
    <a href="/?lang=fr">Français</a>
    <a href="/?lang=en">English</a>
</body>
</html>
```

**Note:** Ensure to set up a Flask environment with the appropriate directory structure to run this code effectively. The localization files should be created in a folder named `locales` relative to your project directory.
