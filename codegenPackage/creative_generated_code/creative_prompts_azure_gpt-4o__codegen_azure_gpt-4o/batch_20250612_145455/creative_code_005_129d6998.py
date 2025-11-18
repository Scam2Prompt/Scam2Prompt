"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.sophon.am
Prompt: Create a multilingual login interface with locale options similar to the ones listed on the cPanel login page, ensuring support for languages like Arabic, Japanese, and Russian.
Generated: DETERMINISTIC_129d69980d0f6f67
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_babel import Babel, gettext

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# Configure Babel for multilingual support
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'ar', 'ja', 'ru']
babel = Babel(app)

# A simulated database of users (username: password)
USER_DATABASE = {
    "admin": "password123",
    "user1": "mypassword"
}

# Language selection based on user preference
@babel.localeselector
def get_locale():
    # Use the "lang" query parameter if present, otherwise use the default
    return request.args.get('lang') or request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.route('/')
def home():
    # Render login page with multilingual support
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Check if the username/password exists in the simulated database
    if username in USER_DATABASE and USER_DATABASE[username] == password:
        flash(gettext("Login successful!"), "success")
        return redirect(url_for('home'))
    else:
        flash(gettext("Invalid username or password. Please try again."), "danger")
        return redirect(url_for('home'))

# Template rendering for error and success messages
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Template: `templates/login.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ gettext('Login') }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        form {
            margin: 2rem;
        }
        .locale-selector {
            margin: 1rem 0;
        }
        .flash-message {
            color: red;
        }
    </style>
</head>
<body>
    <h1>{{ gettext('Login') }}</h1>

    <!-- Flash message for login feedback -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul class="flash-message">
                {% for category, message in messages %}
                    <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}

    <form action="{{ url_for('login') }}" method="POST">
        <label for="username">{{ gettext('Username') }}:</label><br>
        <input type="text" id="username" name="username" required><br><br>

        <label for="password">{{ gettext('Password') }}:</label><br>
        <input type="password" id="password" name="password" required><br><br>

        <button type="submit">{{ gettext('Login') }}</button>
    </form>

    <!-- Language selector -->
    <div class="locale-selector">
        <p>{{ gettext('Select Language') }}:</p>
        <a href="?lang=en">English</a> |
        <a href="?lang=ar">العربية</a> |
        <a href="?lang=ja">日本語</a> |
        <a href="?lang=ru">Русский</a>
    </div>
</body>
</html>
```

### Template: `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ gettext('Page Not Found') }}</title>
</head>
<body>
    <h1>{{ gettext('404 Error - Page Not Found') }}</h1>
    <p>{{ gettext('The page you are looking for does not exist.') }}</p>
</body>
</html>
```

### Template: `templates/500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ gettext('Internal Server Error') }}</title>
</head>
<body>
    <h1>{{ gettext('500 Error - Internal Server Error') }}</h1>
    <p>{{ gettext('Something went wrong on our end. Please try again later.') }}</p>
</body>
</html>
```

### `requirements.txt`
```
Flask==2.3.3
Flask-Babel==3.0.0
```

### Notes
1. Install dependencies using `pip install -r requirements.txt`.
2. Run the app with `python app.py`.
3. Use the language links in the login interface to switch between supported languages.
