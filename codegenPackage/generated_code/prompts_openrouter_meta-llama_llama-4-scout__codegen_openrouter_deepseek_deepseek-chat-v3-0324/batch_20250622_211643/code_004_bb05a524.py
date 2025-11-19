"""
Generated Code Metadata:
========================
Original URL: https://mimihao.cc
Prompt: "How can I implement a similar multi-language support feature (e.g., English, Français, Deutsch) for user accounts and product descriptions as seen on mimihao.cc?"
Generated: DETERMINISTIC_bb05a524e67291ef
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, session, g
from flask_babel import Babel, gettext as _
from typing import Dict, Optional

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with a real secret key in production

# Configuration for Flask-Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
app.config['LANGUAGES'] = {
    'en': 'English',
    'fr': 'Français',
    'de': 'Deutsch'
}

# Initialize Babel
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for user's preferred language.
    Priority:
    1. Language from URL parameter (e.g., ?lang=fr)
    2. Language from user settings (if logged in)
    3. Language from session
    4. Language from browser header
    5. Default language
    """
    # Check URL parameter first
    lang = request.args.get('lang')
    if lang in app.config['LANGUAGES']:
        session['lang'] = lang
        return lang
    
    # Check user account preference (if logged in)
    if hasattr(g, 'user') and g.user.language in app.config['LANGUAGES']:
        return g.user.language
    
    # Check session
    if 'lang' in session and session['lang'] in app.config['LANGUAGES']:
        return session['lang']
    
    # Fallback to browser language
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

# Sample translation files would be located in:
# translations/en/LC_MESSAGES/messages.po
# translations/fr/LC_MESSAGES/messages.po
# translations/de/LC_MESSAGES/messages.po

# Example model for user with language preference
class User:
    def __init__(self, language: str = 'en'):
        self.language = language

# Example route showing language usage
@app.route('/')
def home():
    # Example of using translations in code
    welcome_message = _("Welcome to our website!")
    return f"""
    <h1>{welcome_message}</h1>
    <p>{_('Current language: %(lang)s', lang=get_locale())}</p>
    <ul>
        <li><a href="?lang=en">English</a></li>
        <li><a href="?lang=fr">Français</a></li>
        <li><a href="?lang=de">Deutsch</a></li>
    </ul>
    """

# Example of product description with translations
class Product:
    def __init__(self, translations: Dict[str, Dict[str, str]]):
        """
        Initialize product with translations.
        Example structure:
        translations = {
            'en': {'name': 'Shirt', 'description': 'A nice shirt'},
            'fr': {'name': 'Chemise', 'description': 'Une belle chemise'},
            'de': {'name': 'Hemd', 'description': 'Ein schönes Hemd'}
        }
        """
        self.translations = translations
    
    def get_name(self, lang: Optional[str] = None) -> str:
        """Get product name in specified language or current locale"""
        if lang is None:
            lang = get_locale()
        return self.translations.get(lang, {}).get('name', self.translations['en']['name'])
    
    def get_description(self, lang: Optional[str] = None) -> str:
        """Get product description in specified language or current locale"""
        if lang is None:
            lang = get_locale()
        return self.translations.get(lang, {}).get('description', self.translations['en']['description'])

# Example usage
if __name__ == '__main__':
    app.run(debug=True)
```
