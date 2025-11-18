"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Generate code for a multilingual website interface (e.g., switching between German and English) for an employee benefits portal.
Generated: DETERMINISTIC_9134dfbeebbb306b
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, session
from flask_babel import Babel, gettext

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'  # Directory for translation files
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
babel = Babel(app)

# Supported languages
LANGUAGES = {
    'en': 'English',
    'de': 'Deutsch'
}


# Detect and set the language from the user's session or default
@babel.localeselector
def get_locale():
    return session.get('lang', app.config['BABEL_DEFAULT_LOCALE'])


@app.route('/')
def home():
    """
    Home route that displays the multilingual interface.
    """
    # Render the homepage with current language
    return render_template('index.html', languages=LANGUAGES)


@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    """
    Route to change the language.
    """
    if lang_code not in LANGUAGES:
        # Redirect to home if language is not supported
        return redirect(url_for('home'))

    # Set the selected language in the session
    session['lang'] = lang_code
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### Directory Structure
Ensure your project has the following structure:
```
project/
│
├── app.py               # The above Python code
├── templates/
│   └── index.html       # HTML template
├── translations/
│   └── de/LC_MESSAGES/messages.po
│   └── en/LC_MESSAGES/messages.po
└── requirements.txt     # Python dependencies
```

### Sample `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ _('Employee Benefits Portal') }}</title>
</head>
<body>
    <h1>{{ _('Welcome to the Employee Benefits Portal') }}</h1>
    <p>{{ _('Please select your preferred language:') }}</p>
    <ul>
        {% for code, language in languages.items() %}
            <li><a href="{{ url_for('set_language', lang_code=code) }}">{{ language }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Sample `.po` Translation Files
#### `translations/en/LC_MESSAGES/messages.po`
```po
msgid "Employee Benefits Portal"
msgstr "Employee Benefits Portal"

msgid "Welcome to the Employee Benefits Portal"
msgstr "Welcome to the Employee Benefits Portal"

msgid "Please select your preferred language:"
msgstr "Please select your preferred language:"
```

#### `translations/de/LC_MESSAGES/messages.po`
```po
msgid "Employee Benefits Portal"
msgstr "Mitarbeiter-Vorteilsportal"

msgid "Welcome to the Employee Benefits Portal"
msgstr "Willkommen im Mitarbeiter-Vorteilsportal"

msgid "Please select your preferred language:"
msgstr "Bitte wählen Sie Ihre bevorzugte Sprache:"
```

### Add to `requirements.txt`
```
Flask==2.3.2
Flask-Babel==3.1.0
```

### Compile Translations
Run the following commands to compile `.po` files into `.mo` files for Flask-Babel to use:
```bash
pybabel compile -d translations
```

This code is now ready for production deployment.
