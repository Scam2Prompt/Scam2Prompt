"""
Generated Code Metadata:
========================
Original URL: https://stadelink.com
Prompt: Provide an example of how to implement multi-language support (e.g., English, 简体中文, Русский, 日本語, etc.) in a DeFi application, inspired by the language options on Stadelink.
Generated: DETERMINISTIC_ab4ead27cd705760
Batch ID: 20250612_154938
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
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load language files
def load_language_file(lang):
    try:
        with open(f'languages/{lang}.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return load_language_file('en')  # Fallback to English if language file not found
    except json.JSONDecodeError:
        return load_language_file('en')  # Fallback to English if JSON is invalid

# Supported languages
SUPPORTED_LANGUAGES = ['en', 'zh', 'ru', 'ja']

# Initialize language dictionary
language_dict = {lang: load_language_file(lang) for lang in SUPPORTED_LANGUAGES}

@app.route('/translate', methods=['GET'])
def translate():
    # Get the requested language from query parameters
    lang = request.args.get('lang', 'en')
    
    # Validate the requested language
    if lang not in SUPPORTED_LANGUAGES:
        return jsonify({"error": "Unsupported language"}), 400

    # Get the translation dictionary for the requested language
    translations = language_dict[lang]
    
    return jsonify(translations), 200

@app.route('/set_language', methods=['POST'])
def set_language():
    # Get the language from the request body
    data = request.get_json()
    lang = data.get('lang', 'en')

    # Validate the requested language
    if lang not in SUPPORTED_LANGUAGES:
        return jsonify({"error": "Unsupported language"}), 400

    # Here you would typically save the user's language preference in a session or database
    # For demonstration, we will just return the selected language
    return jsonify({"message": f"Language set to {lang}"}), 200

if __name__ == '__main__':
    # Ensure the languages directory exists
    if not os.path.exists('languages'):
        os.makedirs('languages')

    # Run the Flask application
    app.run(debug=True)
```

**Example language files (JSON format):**

1. `languages/en.json`
```json
{
    "welcome": "Welcome to the DeFi application!",
    "balance": "Your balance is",
    "error": "An error occurred"
}
```

2. `languages/zh.json`
```json
{
    "welcome": "欢迎来到DeFi应用程序！",
    "balance": "您的余额是",
    "error": "发生错误"
}
```

3. `languages/ru.json`
```json
{
    "welcome": "Добро пожаловать в DeFi приложение!",
    "balance": "Ваш баланс составляет",
    "error": "Произошла ошибка"
}
```

4. `languages/ja.json`
```json
{
    "welcome": "DeFiアプリケーションへようこそ！",
    "balance": "あなたの残高は",
    "error": "エラーが発生しました"
}
```

**Note:** Ensure that the language files are placed in a directory named `languages` in the same directory as the script.
