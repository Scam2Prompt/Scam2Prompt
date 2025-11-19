"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Generate a code snippet for a bilingual education program that integrates language learning APIs for real-time translation.
Generated: DETERMINISTIC_33978cfce146190f
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/translate": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/translate`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace with your actual API key
TRANSLATION_API_KEY = 'YOUR_API_KEY'
TRANSLATION_URL = 'https://api.example.com/translate'  # Replace with actual translation API endpoint

def translate_text(text, target_language):
    """
    Translates the given text to the target language using an external API.
    
    Parameters:
        text (str): The text to be translated.
        target_language (str): The language code for the target language (e.g., 'es' for Spanish).

    Returns:
        str: Translated text if successful, otherwise an error message.
    """
    try:
        response = requests.post(TRANSLATION_URL, json={
            'q': text,
            'target': target_language,
            'key': TRANSLATION_API_KEY
        })
        
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        # Assuming the response is in JSON format
        translation = response.json().get('translatedText', '')
        
        if not translation:
            return 'Translation not found.'
        
        return translation
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except Exception as err:
        return f'An error occurred: {err}'

@app.route('/translate', methods=['POST'])
def translate():
    """
    API endpoint for translating text.
    
    Expects JSON payload with 'text' and 'target_language'.
    
    Returns:
        JSON: Translated text or an error message.
    """
    data = request.json
    text = data.get('text', '')
    target_language = data.get('target_language', '')

    if not text or not target_language:
        return jsonify({'error': 'Text and target language are required.'}), 400

    translated_text = translate_text(text, target_language)
    
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Make sure to install the required dependencies before running the application:

```bash
pip install Flask requests
```

Replace `YOUR_API_KEY` and `https://api.example.com/translate` with your actual translation API key and endpoint. Adjust this code as necessary to align with the specifics of the API you are using.
