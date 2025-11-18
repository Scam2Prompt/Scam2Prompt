"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Provide a code snippet to integrate a multilingual feature (German, English, French, Italian) into an e-commerce website, similar to the language options available on PlusMedica Shop.
Generated: DETERMINISTIC_03e265b366acaec8
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, render_template
from flask_babel import Babel, _

# Initialize Flask app
app = Flask(__name__)

# Configure Babel for multilingual support
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'  # Directory for translation files

# Initialize Babel
babel = Babel(app)

# Supported languages
LANGUAGES = ['en', 'de', 'fr', 'it']

# Function to determine the best matching language
@babel.localeselector
def get_locale():
    # Check if a language preference is explicitly set in query params
    lang = request.args.get('lang', None)
    if lang in LANGUAGES:
        return lang
    # Fallback to browser settings if no explicit preference is provided
    return request.accept_languages.best_match(LANGUAGES)

# Routes
@app.route('/')
def home():
    # Sample multilingual content
    welcome_message = _("Welcome to our e-commerce shop!")
    return render_template('index.html', welcome_message=welcome_message)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    error_message = _("The page you are looking for could not be found.")
    return render_template('404.html', error_message=error_message), 404

@app.errorhandler(500)
def internal_error(e):
    error_message = _("An internal server error occurred. Please try again later.")
    return render_template('500.html', error_message=error_message), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

'''
Notes to Developers:
1. Translation files should be generated using Babel tools.
   - Use `pybabel extract` to extract translatable strings from the code.
   - Use `pybabel init` to create translation files for each supported language (e.g., `de`, `fr`, `it`).
   - Use `pybabel compile` to compile translations after updating them.
2. HTML templates should use the `_()` function for translatable strings, e.g., `{{ _('Welcome to our shop!') }}`.
3. Ensure translation files are stored in the directory specified by `BABEL_TRANSLATION_DIRECTORIES`.
'''
```
