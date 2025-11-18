"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stadelink.com
Prompt: Provide an example of how to implement multi-language support (e.g., English, 简体中文, Русский, 日本語, etc.) in a DeFi application, inspired by the language options on Stadelink.
Generated: DETERMINISTIC_ab4ead27cd705760
Batch ID: 20250612_154938
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

# Load language files
def load_language_file(lang):
    try:
        with open(f'languages/{lang}.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return load_language_file('en')  # Fallback to English

# Supported languages
SUPPORTED_LANGUAGES = ['en', 'zh', 'ru', 'ja']

# Store translations for the selected language
translations = {}

@app.route('/set_language/<lang>', methods=['GET'])
def set_language(lang):
    """
    Set the preferred language for the user.

    :param lang: Language code (e.g., 'en', 'zh', 'ru', 'ja')
    :return: JSON response with success message or error
    """
    if lang not in SUPPORTED_LANGUAGES:
        return jsonify({'error': 'Unsupported language'}), 400

    global translations
    translations = load_language_file(lang)
    return jsonify({'message': f'Language set to {lang}'}), 200

@app.route('/translate/<key>', methods=['GET'])
def translate(key):
    """
    Retrieve the translation for a given key in the selected language.

    :param key: Translation key (e.g., 'welcome_message')
    :return: JSON response with translation or error
    """
    if key not in translations:
        return jsonify({'error': 'Translation key not found'}), 404
    
    return jsonify({'translation': translations[key]}), 200

if __name__ == '__main__':
    # Ensure the languages directory exists
    import os
    os.makedirs('languages', exist_ok=True)

    # Run the Flask application
    app.run(debug=True)
```

### Example Language Files
Create a directory named `languages` and add the following JSON files:

**languages/en.json**
```json
{
  "welcome_message": "Welcome to our DeFi application!"
}
```

**languages/zh.json**
```json
{
  "welcome_message": "欢迎来到我们的DeFi应用程序！"
}
```

**languages/ru.json**
```json
{
  "welcome_message": "Добро пожаловать в наше DeFi приложение!"
}
```

**languages/ja.json**
```json
{
  "welcome_message": "私たちのDeFiアプリケーションへようこそ！"
}
```

### Running the Application
1. Ensure you have Flask installed: `pip install Flask`.
2. Save the main code in a `.py` file and the JSON files in the `languages` directory.
3. Run the application using `python your_script.py`.
4. Access endpoints to set the language and retrieve translations.
