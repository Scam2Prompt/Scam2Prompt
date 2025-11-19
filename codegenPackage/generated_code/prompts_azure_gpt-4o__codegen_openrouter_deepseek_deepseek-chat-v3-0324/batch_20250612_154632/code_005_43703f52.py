"""
Generated Code Metadata:
========================
Original URL: https://app.apexbooster.com
Prompt: Write code to implement a multilingual translation feature for a web application, inspired by the language options provided on Apex Booster (e.g., Malay, Français, and Thai).
Generated: DETERMINISTIC_43703f52d09c773a
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import googletrans
from googletrans import Translator
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Initialize translator
translator = Translator()

# Supported languages with their codes and display names
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'ms': 'Malay',
    'fr': 'Français',
    'th': 'Thai',
    # Add more languages as needed
}

def validate_language(f):
    """
    Decorator to validate the target language parameter.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        target_lang = request.args.get('target_lang', 'en')
        if target_lang not in SUPPORTED_LANGUAGES:
            return jsonify({
                'error': 'Unsupported language',
                'supported_languages': SUPPORTED_LANGUAGES
            }), 400
        return f(*args, **kwargs)
    return decorated_function

@app.route('/translate', methods=['POST'])
@validate_language
def translate_text():
    """
    Endpoint to translate text to the target language.
    """
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing text to translate'}), 400

        text = data['text']
        target_lang = request.args.get('target_lang', 'en')

        # Perform translation
        translation = translator.translate(text, dest=target_lang)
        
        return jsonify({
            'original_text': text,
            'translated_text': translation.text,
            'source_language': translation.src,
            'target_language': translation.dest
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/languages', methods=['GET'])
def get_supported_languages():
    """
    Endpoint to get the list of supported languages.
    """
    return jsonify({
        'supported_languages': SUPPORTED_LANGUAGES
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

```html
<!-- Frontend example using HTML/JavaScript -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multilingual Translation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .container {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        textarea {
            width: 100%;
            height: 100px;
            padding: 10px;
        }
        select, button {
            padding: 10px;
            font-size: 16px;
        }
        .result {
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Multilingual Translation</h1>
        
        <div>
            <label for="text-to-translate">Text to translate:</label>
            <textarea id="text-to-translate" placeholder="Enter text here..."></textarea>
        </div>
        
        <div>
            <label for="target-language">Target language:</label>
            <select id="target-language">
                <option value="en">English</option>
                <option value="ms">Malay</option>
                <option value="fr">Français</option>
                <option value="th">Thai</option>
            </select>
        </div>
        
        <button id="translate-btn">Translate</button>
        
        <div class="result" id="translation-result">
            Translation will appear here...
        </div>
    </div>

    <script>
        document.getElementById('translate-btn').addEventListener('click', async () => {
            const text = document.getElementById('text-to-translate').value;
            const targetLang = document.getElementById('target-language').value;
            
            if (!text) {
                alert('Please enter some text to translate');
                return;
            }
            
            try {
                const response = await fetch('/translate?target_lang=' + targetLang, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ text: text })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    document.getElementById('translation-result').innerHTML = `
                        <strong>Original (${data.source_language}):</strong> ${data.original_text}<br><br>
                        <strong>Translation (${data.target_language}):</strong> ${data.translated_text}
                    `;
                } else {
                    document.getElementById('translation-result').innerHTML = `
                        <strong>Error:</strong> ${data.error}
                    `;
                }
            } catch (error) {
                document.getElementById('translation-result').innerHTML = `
                    <strong>Error:</strong> Failed to connect to translation service
                `;
                console.error('Translation error:', error);
            }
        });
    </script>
</body>
</html>
```
