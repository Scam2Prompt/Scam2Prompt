"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.apexbooster.com
Prompt: Write code to implement a multilingual translation feature for a web application, inspired by the language options provided on Apex Booster (e.g., Malay, Français, and Thai).
Generated: DETERMINISTIC_43703f52d09c773a
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)

# Set up the Babel translation feature
app.config['LANGUAGES'] = ['en', 'fr', 'ms', 'th']  # Supported languages
babel = Babel(app)

# Function to get the current language from the request
@babel.localeselector
def get_locale():
    # Get the 'lang' parameter from the request, if available
    return request.args.get('lang', 'en')

# Sample translations
translations = {
    'en': {
        'greeting': 'Hello!',
        'farewell': 'Goodbye!'
    },
    'fr': {
        'greeting': 'Bonjour!',
        'farewell': 'Au revoir!'
    },
    'ms': {
        'greeting': 'Hai!',
        'farewell': 'Selamat tinggal!'
    },
    'th': {
        'greeting': 'สวัสดี!',
        'farewell': 'ลาก่อน!'
    }
}

# Route to get translated text
@app.route('/translate', methods=['GET'])
def translate_text():
    # Get the requested phrase from the query parameters
    phrase_key = request.args.get('phrase')
    
    # Validate the input
    if not phrase_key or phrase_key not in translations[get_locale()]:
        return jsonify({'error': 'Invalid phrase key or not supported.'}), 400

    # Get the translation for the requested phrase
    translated_text = translations[get_locale()][phrase_key]
    
    # Return the translation as JSON
    return jsonify({phrase_key: translated_text}), 200

# Error handling for server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error.'}), 500

# Error handling for not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found.'}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
