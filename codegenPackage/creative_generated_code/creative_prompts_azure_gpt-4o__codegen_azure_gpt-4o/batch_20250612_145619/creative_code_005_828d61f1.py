"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.arbitrium.adv.br
Prompt: Recommend tools or libraries to manage multi-language support for a web-based login interface like cPanel, including handling locale selection.
Generated: DETERMINISTIC_828d61f1b69cb715
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to demonstrate managing multi-language support for a web-based login interface.

# Libraries used:
# - Flask: A lightweight web framework for Python.
# - Flask-Babel: Provides i18n and l10n support for Flask applications.

from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)

# Configure supported languages and default locale
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'
app.config['LANGUAGES'] = {
    'en': 'English',
    'es': 'Español',
    'fr': 'Français'
}

# Initialize Babel for localization
babel = Babel(app)

# Function to get the best-match locale from user or browser preference
@babel.localeselector
def get_locale():
    # Use 'lang' parameter from query string if available, otherwise fallback to browser settings
    return request.args.get('lang') or request.accept_languages.best_match(app.config['LANGUAGES'].keys())

# Error handling for missing translations
@babel.errorhandler
def babel_error_handler(error):
    app.logger.error(f"Translation error: {error}")
    return _("An error occurred while loading translations."), 500

@app.route('/')
def login():
    """
    Renders the login interface, supporting multi-language translations.
    """
    return render_template('login.html')

@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    """
    Updates the user's preferred language using the lang_code provided in the URL.
    """
    if lang_code not in app.config['LANGUAGES']:
        return _("Language not supported"), 400

    # Redirect to the homepage with the selected language as a query parameter
    return redirect(url_for('login', lang=lang_code))


# Example login.html template for demonstration
"""
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <title>{{ _('Login') }}</title>
</head>
<body>
    <h1>{{ _('Welcome to the Login Page') }}</h1>
    <form action="/login" method="post">
        <label for="username">{{ _('Username') }}</label>
        <input type="text" id="username" name="username">

        <label for="password">{{ _('Password') }}</label>
        <input type="password" id="password" name="password">

        <button type="submit">{{ _('Login') }}</button>
    </form>
    <div>
        <h3>{{ _('Change Language') }}</h3>
        <ul>
            {% for lang_code, lang_name in config['LANGUAGES'].items() %}
                <li><a href="{{ url_for('set_language', lang_code=lang_code) }}">{{ lang_name }}</a></li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

# Run the Flask application in development mode
if __name__ == '__main__':
    app.run(debug=True)
```

**Notes**
1. Run the `pybabel` commands to initialize and compile translations for Flask-Babel.
2. Place the translations (`.po` and `.mo` files) in the `./translations` directory.
3. Install Flask and Flask-Babel using `pip install flask flask-babel`.
4. Use `gettext` or `_` in your templates and Python code for translatable strings.
