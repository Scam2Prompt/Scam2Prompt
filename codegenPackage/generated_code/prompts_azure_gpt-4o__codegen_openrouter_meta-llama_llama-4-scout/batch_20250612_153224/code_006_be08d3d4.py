"""
Generated Code Metadata:
========================
Original URL: https://skyline-ia.com
Prompt: Suggest tools or frameworks for building a multilingual tourism website, ensuring support for languages like English, French, Turkish, German, and Italian, as seen on Skyline International Agent's site.
Generated: DETERMINISTIC_be08d3d4eeef66a9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_babel import Babel
from flask_moment import Moment

# Create a Flask application instance
app = Flask(__name__)

# Configure the application
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

# Initialize Babel and Moment extensions
babel = Babel(app)
moment = Moment(app)

# Define supported languages
SUPPORTED_LANGUAGES = ['en', 'fr', 'tr', 'de', 'it']

# Update Babel to use supported languages
@babel.localeselector
def get_locale():
    """Returns the locale based on the request"""
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)

# Define a route for the homepage
@app.route('/')
def index():
    """Renders the homepage"""
    return jsonify({'message': 'Welcome to our multilingual tourism website!'})

# Define a route for language-specific content
@app.route('/<lang>')
def language_content(lang):
    """Renders language-specific content"""
    if lang not in SUPPORTED_LANGUAGES:
        return jsonify({'error': 'Language not supported'}), 404
    
    # Load language-specific content from a database or file
    # For demonstration purposes, return a simple message
    messages = {
        'en': 'Welcome to our website!',
        'fr': 'Bienvenue sur notre site web!',
        'tr': 'Website\'imize hoş geldiniz!',
        'de': 'Willkommen auf unserer Website!',
        'it': 'Benvenuti sul nostro sito web!'
    }
    return jsonify({'message': messages[lang]})

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors"""
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(error):
    """Handles 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
```

### translations/en.po
```po
msgid ""
msgstr ""
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

#: app.py:43
msgid "Welcome to our website!"
msgstr "Welcome to our website!"
```

### translations/fr.po
```po
msgid ""
msgstr ""
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

#: app.py:43
msgid "Welcome to our website!"
msgstr "Bienvenue sur notre site web!"
```

### translations/tr.po
```po
msgid ""
msgstr ""
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

#: app.py:43
msgid "Welcome to our website!"
msgstr "Website'imize hoş geldiniz!"
```

### translations/de.po
```po
msgid ""
msgstr ""
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

#: app.py:43
msgid "Welcome to our website!"
msgstr "Willkommen auf unserer Website!"
```

### translations/it.po
```po
msgid ""
msgstr ""
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

#: app.py:43
msgid "Welcome to our website!"
msgstr "Benvenuti sul nostro sito web!"
```
