"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omninetwork.org
Prompt: What are the steps to integrate multilingual support in a project using OMNI NETWORK's language features?
Generated: DETERMINISTIC_aa42e1f7e594f08e
Batch ID: 20250612_155752
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
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)

# Configure Flask-Babel for multilingual support
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

# Define available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French'
}

# Function to select the best language
@babel.localeselector
def get_locale():
    # Attempt to get the user's preferred language from request headers
    return request.accept_languages.best_match(LANGUAGES.keys())

# Sample translations dictionary
translations = {
    'en': {
        'greeting': 'Hello, World!'
    },
    'es': {
        'greeting': '¡Hola, Mundo!'
    },
    'fr': {
        'greeting': 'Bonjour, le monde!'
    }
}

# Route for getting a greeting message
@app.route('/greet', methods=['GET'])
def greet():
    try:
        # Get the current language based on the request
        lang = get_locale()
        # Retrieve the greeting message according to the selected language
        greeting_message = translations[lang]['greeting']
        return jsonify({'message': greeting_message})
    except KeyError:
        # Handle the case where the language is not supported
        return jsonify({'error': _('Language not supported')}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
