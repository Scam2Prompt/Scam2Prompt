"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Provide code examples for implementing multilingual support (e.g., English, Türkçe, Español) in a CMS similar to Nexelit.
Generated: DETERMINISTIC_3ab2752758a13298
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Multilingual Support Implementation for a CMS-like System

# Required libraries
from flask import Flask, request, session, g
from flask_babel import Babel, _

# Initialize the Flask app
app = Flask(__name__)

# Configure app for Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'tr', 'es']  # Supported languages
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for session handling

# Initialize Babel for translation support
babel = Babel(app)

# Helper function to get the user's preferred language
@babel.localeselector
def get_locale():
    # Check if a language is set in the session
    if 'lang' in session:
        lang = session['lang']
        if lang in app.config['BABEL_SUPPORTED_LOCALES']:
            return lang
    # Fallback to the `Accept-Language` header sent by the browser
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.route('/change_language/<language>', methods=['GET'])
def change_language(language):
    """
    Endpoint to allow users to change the language.
    :param language: Language code, e.g., 'en', 'tr', 'es'
    """
    if language in app.config['BABEL_SUPPORTED_LOCALES']:
        session['lang'] = language
        return _("Language changed to: ") + language
    else:
        return _("Unsupported language"), 400

@app.route('/')
def home():
    """
    A simple homepage that demonstrates multilingual support.
    """
    welcome_message = _("Welcome to our CMS system!")
    return f"<h1>{welcome_message}</h1>"

# Error handling for unsupported languages
@app.errorhandler(400)
def bad_request_error(error):
    """
    Handle bad requests (e.g., unsupported languages).
    """
    return _("Bad Request: ") + str(error), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Additional Notes:
- To make this code functional, you will need translation files (e.g., `.po` and `.mo` files) for each language (`en`, `tr`, `es`) using tools like `gettext`.
- Install required packages: `pip install flask flask-babel`.
- For production, ensure proper security measures are implemented (e.g., secure session handling).
