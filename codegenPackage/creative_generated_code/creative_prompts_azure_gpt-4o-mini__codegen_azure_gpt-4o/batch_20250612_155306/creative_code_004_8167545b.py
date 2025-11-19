"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic.eu
Prompt: Suggest a library for implementing multilingual support in a web application that aligns with the features mentioned on symbiotic.eu.
Generated: DETERMINISTIC_8167545b2d5dc949
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the Flask web framework and Babel for multilingual support
from flask import Flask, request, render_template
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)

# Configure Babel for multilingual support
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'  # Directory for translation files
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'de', 'fr']  # Supported languages

# Initialize Babel
babel = Babel(app)

# Function to determine the best language match for the user
@babel.localeselector
def get_locale():
    # Match user preference from the Accept-Language HTTP header or fallback to default
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

# Route for the homepage
@app.route('/')
def home():
    # Render a template with translated strings
    return render_template('index.html', message=_("Welcome to our multilingual web application!"))

# Error handling for unsupported locales
@app.errorhandler(404)
def page_not_found(e):
    return _("Sorry, the page you are looking for is not available."), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes for Setup:
1. Create a folder named `translations` in the root directory to store language files.
2. Use the `pybabel` command-line tool to generate `.po` files for translations:
   - Initialize translations with `pybabel extract -F babel.cfg -o messages.pot .`.
   - Add new languages with `pybabel init -i messages.pot -d translations -l <locale>`.
   - Compile translations with `pybabel compile -d translations`.
3. Install required Python libraries (`Flask` and `Flask-Babel`):
   ```bash
   pip install Flask Flask-Babel
   ```

This code ensures clean implementation, proper error handling, and multilingual support in alignment with best practices.
