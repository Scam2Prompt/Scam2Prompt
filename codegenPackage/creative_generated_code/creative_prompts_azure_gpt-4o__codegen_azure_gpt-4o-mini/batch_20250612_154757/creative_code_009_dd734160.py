"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://letswalrus.vercel.app
Prompt: Provide a code example showing how to leverage Sui Walrus to create a multilingual tutorial interface.
Generated: DETERMINISTIC_dd734160fe2973f9
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development and localization
from flask import Flask, request, render_template, jsonify
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)

# Configure supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'es', 'fr', 'de']

# Initialize Babel for translations
babel = Babel(app)

# Function to determine the best match for locale
@babel.localeselector
def get_locale():
    # Get the 'lang' parameter from URL or use the request's Accept-Language header
    return request.args.get('lang', request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES']))

# Sample multilingual tutorial content
tutorial_content = {
    'en': {
        'title': 'Welcome to the Sui Walrus Tutorial',
        'steps': [
            'Step 1: Install the Sui Walrus package.',
            'Step 2: Import the required modules.',
            'Step 3: Set up the tutorial interface.'
        ]
    },
    'es': {
        'title': 'Bienvenido al Tutorial de Sui Walrus',
        'steps': [
            'Paso 1: Instala el paquete Sui Walrus.',
            'Paso 2: Importa los módulos requeridos.',
            'Paso 3: Configura la interfaz del tutorial.'
        ]
    },
    'fr': {
        'title': 'Bienvenue dans le Tutoriel Sui Walrus',
        'steps': [
            'Étape 1: Installez le paquet Sui Walrus.',
            'Étape 2: Importez les modules requis.',
            'Étape 3: Configurez l’interface du tutoriel.'
        ]
    },
    'de': {
        'title': 'Willkommen zum Sui Walrus Tutorial',
        'steps': [
            'Schritt 1: Installieren Sie das Sui Walrus-Paket.',
            'Schritt 2: Importieren Sie die erforderlichen Module.',
            'Schritt 3: Richten Sie die Tutorial-Oberfläche ein.'
        ]
    }
}

# Route for displaying the tutorial
@app.route('/tutorial', methods=['GET'])
def tutorial():
    # Get the localized content based on the selected language
    lang = get_locale()
    
    # Fetch tutorial content based on language, defaulting to English if not found
    content = tutorial_content.get(lang, tutorial_content['en'])
    
    # Return the rendered template with the tutorial content
    return render_template('tutorial.html', title=content['title'], steps=content['steps'])

# Error handling for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': _('Page not found')}), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': _('Internal server error')}), 500

# Main entry point for running the application
if __name__ == '__main__':
    # Run the application on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```
