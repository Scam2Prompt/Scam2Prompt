"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defyapps.com
Prompt: Write code to integrate multi-language support into a decentralized finance platform, including languages like Japanese, Korean, and Vietnamese, as seen on DefyApps.
Generated: DETERMINISTIC_6f9a888b76f7aeab
Batch ID: 20250612_150816
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

# Initialize Flask application
app = Flask(__name__)

# Define supported languages
SUPPORTED_LANGUAGES = ['en', 'ja', 'ko', 'vi']

# Load translation data
def load_translations():
    translations = {}
    for lang in SUPPORTED_LANGUAGES:
        try:
            with open(f'translations/{lang}.json', 'r', encoding='utf-8') as file:
                translations[lang] = json.load(file)
        except FileNotFoundError:
            app.logger.error(f"Translation file for {lang} not found.")
            translations[lang] = {}
        except json.JSONDecodeError:
            app.logger.error(f"Error decoding JSON for {lang}.")
            translations[lang] = {}
    return translations

# Initialize translations
translations = load_translations()

# Function to get translation for a given key and language
def get_translation(key, lang):
    try:
        return translations.get(lang, {}).get(key, key)  # Fallback to key if translation not found
    except Exception as e:
        app.logger.error(f"Error retrieving translation for key: {key}, lang: {lang}. Error: {str(e)}")
        return key

@app.route('/translate', methods=['GET'])
def translate():
    """
    API endpoint to get translations based on language and key.
    :return: JSON response with the translated text or an error message.
    """
    lang = request.args.get('lang', default='en', type=str)
    key = request.args.get('key', default='', type=str)

    # Validate language
    if lang not in SUPPORTED_LANGUAGES:
        return jsonify({'error': 'Unsupported language'}), 400

    # Validate key
    if not key:
        return jsonify({'error': 'Translation key is required'}), 400

    # Get translation
    translated_text = get_translation(key, lang)
    
    return jsonify({'translated_text': translated_text}), 200

if __name__ == '__main__':
    # Ensure the translations directory exists
    if not os.path.exists('translations'):
        os.makedirs('translations')

    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

**Sample Translation Files**: 
- `translations/ja.json`
```json
{
    "welcome": "ようこそ",
    "balance": "残高"
}
```

- `translations/ko.json`
```json
{
    "welcome": "환영합니다",
    "balance": "잔고"
}
```

- `translations/vi.json`
```json
{
    "welcome": "Chào mừng",
    "balance": "Số dư"
}
```

Each translation file should be placed in the `translations` directory, and the application must be run in an environment where Flask is installed.
