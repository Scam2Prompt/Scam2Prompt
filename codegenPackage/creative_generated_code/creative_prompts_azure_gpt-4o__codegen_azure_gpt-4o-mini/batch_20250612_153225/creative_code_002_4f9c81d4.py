"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parrotrans.com
Prompt: Generate code to integrate live translation services into a web application, specifically for corporate and governmental fields, as described by Parrotrans.
Generated: DETERMINISTIC_4f9c81d41afe1c09
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Google Translator
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    """
    Endpoint to translate text using Google Translate API.
    Expected JSON input format:
    {
        "text": "Text to be translated",
        "target_lang": "language_code"  # e.g. 'es' for Spanish
    }
    
    :return: JSON response with translated text or error message
    """
    try:
        data = request.get_json()
        # Validate input
        if 'text' not in data or 'target_lang' not in data:
            return jsonify({"error": "Invalid input. Please provide 'text' and 'target_lang'."}), 400
        
        text = data['text']
        target_lang = data['target_lang']
        
        # Validate target language
        if target_lang not in LANGUAGES:
            return jsonify({"error": f"Target language '{target_lang}' is not supported."}), 400

        # Perform the translation
        translated = translator.translate(text, dest=target_lang)
        
        # Return the translated text
        return jsonify({
            "original_text": text,
            "translated_text": translated.text,
            "target_language": target_lang
        }), 200

    except Exception as e:
        # Log the exception for further investigation
        logging.error(f"Error during translation: {str(e)}")
        return jsonify({"error": "An error occurred during translation."}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(host='0.0.0.0', port=5000, debug=False)
```
