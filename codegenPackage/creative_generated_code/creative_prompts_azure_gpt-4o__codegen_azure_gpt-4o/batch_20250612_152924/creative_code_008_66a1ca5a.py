"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Recommend tools or libraries to facilitate multilingual communication (English, French, Arabic, Spanish) in a legal consultancy platform for immigration services.
Generated: DETERMINISTIC_66a1ca5a8eae69ed
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code for a Python implementation using the `googletrans` library and Flask for facilitating multilingual communication.

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES

# Create a Flask application instance
app = Flask(__name__)

# Initialize Google Translator
translator = Translator()

# Define supported languages for the legal consultancy platform
SUPPORTED_LANGUAGES = ['en', 'fr', 'ar', 'es']  # English, French, Arabic, Spanish

@app.route('/translate', methods=['POST'])
def translate_text():
    """
    Endpoint for translating text messages between supported languages.
    Expects JSON payload with keys 'text' and 'target_language'.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        text = data.get('text')
        target_language = data.get('target_language')

        # Input validation
        if not text or not target_language:
            return jsonify({'error': 'Invalid input. Please provide both "text" and "target_language".'}), 400
        
        if target_language not in SUPPORTED_LANGUAGES:
            return jsonify({'error': f'Target language "{target_language}" is not supported. Supported languages: {SUPPORTED_LANGUAGES}'}), 400

        # Perform translation
        translated = translator.translate(text, dest=target_language)
        return jsonify({
            'original_text': text,
            'translated_text': translated.text,
            'source_language': translated.src,
            'target_language': target_language
        })

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': str(e)}), 500

@app.route('/languages', methods=['GET'])
def get_supported_languages():
    """
    Endpoint for retrieving the list of supported languages.
    """
    return jsonify({'supported_languages': SUPPORTED_LANGUAGES})

# Run the Flask application
if __name__ == '__main__':
    # Start the server in debug mode (not recommended for production)
    app.run(debug=True)
```

### Setup:
1. Install required dependencies:
   ```bash
   pip install flask googletrans==4.0.0-rc1
   ```
2. Save the code to a file named, for example, `app.py`.
3. Run the application:
   ```bash
   python app.py
   ```
4. Use the `/translate` endpoint to translate text and `/languages` endpoint to get supported languages.

### Notes:
- This code leverages `googletrans` for translation, which uses Google Translate under the hood.
- For production, ensure that rate-limiting, user authentication, and SSL/TLS are properly configured.
