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
# Import necessary libraries
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_babel import Babel, _

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a strong secret key

# Initialize Flask-Babel for localization support
babel = Babel(app)

# Supported languages
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    # Add more languages as needed
}

# Function to select the language based on user preference or default
@babel.localeselector
def get_locale():
    # Get the user's locale from the request or use default
    return request.accept_languages.best_match(LANGUAGES.keys())

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Basic validation for username and password
        if not username or not password:
            flash(_('Username and password are required.'))
            return redirect(url_for('login'))

        # TODO: Add authentication logic here (e.g., check against a database)

        # If authentication fails, flash an error message
        flash(_('Invalid username or password.'))
        return redirect(url_for('login'))

    # Render the login template
    return render_template('login.html', languages=LANGUAGES)

# Route for changing language
@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in LANGUAGES:
        # Store the selected language in the session
        session['lang'] = lang
        flash(_('Language changed to %s') % LANGUAGES[lang])
    else:
        flash(_('Language not supported.'))
    return redirect(url_for('login'))

# Main entry point
if __name__ == '__main__':
    # Run the app in debug mode for development only
    app.run(debug=True)
```

### Template: `login.html`
```html
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <title>{{ _('Login') }}</title>
</head>
<body>
    <h1>{{ _('Login') }}</h1>
    <form method="POST" action="{{ url_for('login') }}">
        <label for="username">{{ _('Username') }}</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">{{ _('Password') }}</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">{{ _('Submit') }}</button>
    </form>

    <h2>{{ _('Select Language') }}</h2>
    <ul>
        {% for lang, language in languages.items() %}
            <li><a href="{{ url_for('set_language', lang=lang) }}">{{ language }}</a></li>
        {% endfor %}
    </ul>

    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

### Requirements
To run this application, make sure to install the following dependencies:

```bash
pip install Flask Flask-Babel
```

### Note
- Ensure to create appropriate locale files for each language in the `translations` directory.
- Implement the authentication logic in the `login` route as per your application's requirements.
