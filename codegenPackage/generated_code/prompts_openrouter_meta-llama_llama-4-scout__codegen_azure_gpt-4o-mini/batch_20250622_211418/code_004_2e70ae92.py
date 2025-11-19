"""
Generated Code Metadata:
========================
Original URL: https://phainton.com
Prompt: Explain how to configure Ispmanager for multi-language support, considering the greetings in multiple languages on the webpage.
Generated: DETERMINISTIC_2e70ae92c771a2e2
Batch ID: 20250622_211418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)

# Configure Babel for multi-language support
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

# Define supported languages
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
}

# Function to select the best language based on the request
@babel.localeselector
def get_locale():
    # Get the 'lang' parameter from the request, if available
    lang = request.args.get('lang')
    if lang in LANGUAGES:
        return lang
    # Fallback to the default locale
    return request.accept_languages.best_match(LANGUAGES.keys())

# Route for the homepage
@app.route('/')
def index():
    # Render the index template with a greeting
    return render_template('index.html')

# Route to get greetings in different languages
@app.route('/greet', methods=['GET'])
def greet():
    # Get the current locale
    locale = get_locale()
    # Define greetings in multiple languages
    greetings = {
        'en': _('Hello!'),
        'es': _('¡Hola!'),
        'fr': _('Bonjour!'),
        'de': _('Hallo!'),
    }
    # Return the greeting based on the selected language
    return jsonify(greeting=greetings.get(locale, greetings['en']))

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify(error=str(error)), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify(error="Internal Server Error"), 500

# Main entry point for the application
if __name__ == '__main__':
    try:
        # Run the application
        app.run(debug=True)
    except Exception as e:
        # Log the exception and exit
        print(f"An error occurred: {e}")
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ _('Greeting Page') }}</title>
</head>
<body>
    <h1>{{ _('Welcome to the Multi-Language Greeting Page') }}</h1>
    <button onclick="fetchGreeting('en')">English</button>
    <button onclick="fetchGreeting('es')">Spanish</button>
    <button onclick="fetchGreeting('fr')">French</button>
    <button onclick="fetchGreeting('de')">German</button>
    <p id="greeting"></p>

    <script>
        function fetchGreeting(lang) {
            fetch(`/greet?lang=${lang}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('greeting').innerText = data.greeting;
                })
                .catch(error => {
                    console.error('Error fetching greeting:', error);
                });
        }
    </script>
</body>
</html>
```
