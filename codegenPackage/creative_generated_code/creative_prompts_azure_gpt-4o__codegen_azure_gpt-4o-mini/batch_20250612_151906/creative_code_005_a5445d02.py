"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rickster.pages.dev
Prompt: Suggest APIs or libraries for implementing multilingual support (English, Deutsch, Français, Italiano) in a cryptocurrency investment app similar to Relai.
Generated: DETERMINISTIC_a5445d023f4db15e
Batch ID: 20250612_151906
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

# Initialize the Flask application
app = Flask(__name__)

# Configure supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALS'] = ['en', 'de', 'fr', 'it']

# Initialize Babel for multilingual support
babel = Babel(app)

# Function to determine the best language
@babel.localeselector
def get_locale():
    # Use the 'Accept-Language' header to determine the client's preferred language
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALS'])

# Sample route to demonstrate multilingual support
@app.route('/api/message', methods=['GET'])
def get_message():
    try:
        # Example messages in different languages
        messages = {
            'en': 'Welcome to the cryptocurrency investment app!',
            'de': 'Willkommen in der Kryptowährungs-Investitions-App!',
            'fr': 'Bienvenue dans l\'application d\'investissement en cryptomonnaie!',
            'it': 'Benvenuti nell\'app di investimento in criptovalute!'
        }

        # Get the user's preferred language
        locale = get_locale()
        
        # Return the message in the selected language
        response_message = messages.get(locale, messages['en'])
        return jsonify({'message': response_message}), 200
        
    except Exception as e:
        # Handle any unexpected errors and return a 500 status
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the app on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```

### Requirements:
- To run this code, you need to install Flask and Flask-Babel:
```bash
pip install Flask Flask-Babel
```
