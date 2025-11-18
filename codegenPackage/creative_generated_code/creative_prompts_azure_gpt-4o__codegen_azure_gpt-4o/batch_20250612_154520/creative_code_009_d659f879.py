"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danceanatolia.com
Prompt: Write code to create a multilingual website (German, Turkish, English) for promoting Anatolian folk dance courses, similar to the language usage on danceanatolia.com.
Generated: DETERMINISTIC_d659f879eee8c8c6
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel, gettext

app = Flask(__name__)

# Configuration for Babel (Localization settings)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'de', 'tr']
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

babel = Babel(app)

# Helper function to determine the best language match
@babel.localeselector
def get_locale():
    # Match the user's preferred language if supported
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html', title=gettext('Welcome to Anatolian Folk Dance Courses'))

# Route for switching language
@app.route('/change_lang/<language>')
def change_language(language):
    if language in app.config['BABEL_SUPPORTED_LOCALES']:
        response = redirect(url_for('index'))
        response.set_cookie('preferred_language', language)
        return response
    return redirect(url_for('index'))

# Error handling for unsupported routes
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title=gettext('Page Not Found')), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', title=gettext('Internal Server Error')), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Directory Structure:
```
project/
├── app.py
├── translations/
│   ├── en/
│   │   └── LC_MESSAGES/
│   │       ├── messages.po
│   │       └── messages.mo
│   ├── de/
│   │   └── LC_MESSAGES/
│   │       ├── messages.po
│   │       └── messages.mo
│   ├── tr/
│       └── LC_MESSAGES/
│           ├── messages.po
│           └── messages.mo
├── templates/
│   ├── index.html
│   ├── 404.html
│   └── 500.html
```

### Example Template: `templates/index.html`
```html
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ gettext("Welcome to Anatolian Folk Dance Courses!") }}</h1>
    <p>{{ gettext("Learn traditional dances from Turkey with expert instructors.") }}</p>
    <div>
        <p>{{ gettext("Choose your language:") }}</p>
        <a href="/change_lang/en">{{ gettext("English") }}</a> |
        <a href="/change_lang/de">{{ gettext("German") }}</a> |
        <a href="/change_lang/tr">{{ gettext("Turkish") }}</a>
    </div>
</body>
</html>
```

### Explanation of Translation Files:
- `messages.po`: Source file containing translatable strings.
- `messages.mo`: Binary file generated from `messages.po` using `msgfmt`.
