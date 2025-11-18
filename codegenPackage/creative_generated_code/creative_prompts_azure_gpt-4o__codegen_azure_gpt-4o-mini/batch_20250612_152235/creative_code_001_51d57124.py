"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prosync.online
Prompt: Recommend an API or library for implementing bilingual support (English and Spanish) in a virtual receptionist system, similar to ProSync's services.
Generated: DETERMINISTIC_51d5712471311a1f
Batch ID: 20250612_152235
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
from flask_babel import Babel, _

app = Flask(__name__)

# Configure the Babel translation service
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

# Available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish'
}

@babel.localeselector
def get_locale():
    # Attempt to guess the user's preferred language from the request
    return request.accept_languages.best_match(LANGUAGES.keys())

@app.route('/translate', methods=['POST'])
def translate():
    """
    Endpoint to translate messages based on user input.
    
    Expected JSON payload:
    {
        "message": "Your message here"
    }
    """
    # Error handling for missing or invalid input
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        
        # Get the message and the locale
        message = data['message']
        locale = get_locale()
        
        # Simulated translation logic (replace with actual translation logic)
        translated_message = _(message)  # Assuming the translation function is properly set up

        return jsonify({
            'original': message,
            'translated': translated_message,
            'language': LANGUAGE[locale]
        }), 200
    
    except Exception as e:
        # Generic error handling for unexpected issues
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```

Make sure to install the required dependencies using:
```bash
pip install Flask Flask-Babel
```

This code provides a simple Flask-based API that can translate messages between English and Spanish. It uses the Flask-Babel library for managing translations and handles errors gracefully. Adjust the translation logic as needed for your actual bilingual support implementation.
