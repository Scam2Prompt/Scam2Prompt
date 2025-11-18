"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.gmprog.com
Prompt: Suggest best practices for designing a login interface that supports multiple languages, referencing the ENG and RUS options on the GMVCI website.
Generated: DETERMINISTIC_6f3446e1f91bf9ae
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a random secret key for session management

# Configure Flask-Babel for internationalization
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

# Supported languages
LANGUAGES = {
    'en': 'English',
    'ru': 'Русский'
}

# Function to get the language from the URL or default to English
@babel.localeselector
def get_locale():
    return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])

# Home route
@app.route('/')
def home():
    return render_template('login.html', languages=LANGUAGES)

# Login route
@app.route('/login', methods=['POST'])
def login():
    # Get username and password from the form
    username = request.form.get('username')
    password = request.form.get('password')

    # Simple error handling for missing fields
    if not username or not password:
        flash(_('Username and password are required.'))
        return redirect(url_for('home'))

    # Simulated user authentication (replace with real authentication logic)
    if username == 'user' and password == 'pass':
        session['username'] = username
        flash(_('Login successful!'))
        return redirect(url_for('dashboard'))
    else:
        flash(_('Invalid username or password.'))
        return redirect(url_for('home'))

# Dashboard route (protected)
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash(_('You need to log in first.'))
        return redirect(url_for('home'))
    return render_template('dashboard.html', username=session['username'])

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash(_('You have been logged out.'))
    return redirect(url_for('home'))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': _('Page not found')}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': _('Internal server error')}), 500

# Main execution
if __name__ == '__main__':
    app.run(debug=True)
```

### login.html
```html
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ _('Login') }}</title>
</head>
<body>
    <h1>{{ _('Login') }}</h1>
    <form method="POST" action="{{ url_for('login') }}">
        <input type="text" name="username" placeholder="{{ _('Username') }}" required>
        <input type="password" name="password" placeholder="{{ _('Password') }}" required>
        <button type="submit">{{ _('Submit') }}</button>
    </form>
    <div>
        <a href="{{ url_for('home', lang='en') }}">English</a>
        <a href="{{ url_for('home', lang='ru') }}">Русский</a>
    </div>
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

### dashboard.html
```html
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ _('Dashboard') }}</title>
</head>
<body>
    <h1>{{ _('Welcome, ') }}{{ username }}</h1>
    <a href="{{ url_for('logout') }}">{{ _('Logout') }}</a>
</body>
</html>
```

### Notes:
- Ensure that the Flask-Babel package is installed for internationalization support.
- Replace the placeholder authentication logic with a secure implementation.
- Use a proper session management strategy in a production environment.
