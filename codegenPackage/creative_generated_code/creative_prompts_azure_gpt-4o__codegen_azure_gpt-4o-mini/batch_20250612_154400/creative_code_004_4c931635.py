"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appsuiteplus.com
Prompt: Write code to create a FAQ section for a file-sharing service, including support for multiple languages, as seen on Wayme.cc.
Generated: DETERMINISTIC_4c9316355adc4ac9
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_babel import Babel, gettext as _

# Initialize Flask application
app = Flask(__name__)

# Configure supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'es', 'fr', 'de']

# Initialize Babel for internationalization
babel = Babel(app)

# Sample FAQ data with translations
faq_data = {
    "en": [
        {"question": "What is file sharing?", "answer": "File sharing is the practice of distributing or providing access to digital media."},
        {"question": "Is my data secure?", "answer": "Yes, we use encryption to protect your data."}
    ],
    "es": [
        {"question": "¿Qué es el intercambio de archivos?", "answer": "El intercambio de archivos es la práctica de distribuir o proporcionar acceso a medios digitales."},
        {"question": "¿Es segura mi información?", "answer": "Sí, utilizamos cifrado para proteger sus datos."}
    ],
    "fr": [
        {"question": "Qu'est-ce que le partage de fichiers?", "answer": "Le partage de fichiers est la pratique de distribuer ou d'accéder à des médias numériques."},
        {"question": "Mes données sont-elles en sécurité?", "answer": "Oui, nous utilisons le cryptage pour protéger vos données."}
    ],
    "de": [
        {"question": "Was ist Filesharing?", "answer": "Filesharing ist die Praxis, digitale Medien zu verteilen oder den Zugriff darauf zu ermöglichen."},
        {"question": "Sind meine Daten sicher?", "answer": "Ja, wir verwenden Verschlüsselung, um Ihre Daten zu schützen."}
    ]
}

# Function to determine the user's preferred language
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.route('/faq', methods=['GET'])
def get_faq():
    """Retrieve FAQ based on the user's language preference."""
    locale = get_locale()
    
    # Check if the requested language is supported
    if locale not in faq_data:
        return jsonify({"error": _("Language not supported")}), 400

    # Return the FAQ data in the requested language
    return jsonify(faq_data[locale])

# Error handling for unexpected issues
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return a standardized error response."""
    return jsonify({"error": _("An unexpected error occurred.")}), 500

# Main entry point of the application
if __name__ == "__main__":
    try:
        app.run(debug=False)  # Set to True for development, False for production
    except Exception as e:
        print(f"Error starting the server: {e}")
```
