"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.com
Prompt: Provide an example of a secure login system using Flask and SQLAlchemy, ensuring compatibility with multi-language interfaces like those on HELPGM.
Generated: DETERMINISTIC_fe52c91fd287c6af
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, gettext as _
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Using SQLite for simplicity
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
babel = Babel(app)

# Initialize the database
db = SQLAlchemy(app)

# Database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    username = db.Column(db.String(150), unique=True, nullable=False)  # Username
    password_hash = db.Column(db.String(256), nullable=False)  # Hashed password

# Endpoint to change the language dynamically
@babel.localeselector
def get_locale():
    return request.args.get('lang', 'en')  # Change based on query parameter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Input validation
        if not username or not password:
            flash(_('All fields are required!'), 'error')
            return redirect(url_for('register'))

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash(_('Username already exists. Please choose another one.'), 'error')
            return redirect(url_for('register'))

        # Create new user with hashed password
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash(_('Registration successful! Please login.'), 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Input validation
        if not username or not password:
            flash(_('All fields are required!'), 'error')
            return redirect(url_for('login'))

        # Authenticate user
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            flash(_('Login successful!'), 'success')
            return redirect(url_for('dashboard'))
        else:
            flash(_('Invalid username or password.'), 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash(_('Please log in to access the dashboard.'), 'error')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', username=user.username)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash(_('You have been logged out.'), 'success')
    return redirect(url_for('login'))

# Initialize the database (run once before using the app)
@app.before_first_request
def create_tables():
    db.create_all()  # Create the database tables if they don't exist

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

---

### Templates (HTML layout):
Below are the basic templates needed for the code above.

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ _('Home') }}</title>
</head>
<body>
    <h1>{{ _('Welcome to the Secure Login System') }}</h1>
    <nav>
        <a href="{{ url_for('register') }}">{{ _('Register') }}</a>
        <a href="{{ url_for('login') }}">{{ _('Login') }}</a>
    </nav>
</body>
</html>
```

#### `register.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ _('Register') }}</title>
</head>
<body>
    <h1>{{ _('Register') }}</h1>
    <form method="POST" action="{{ url_for('register') }}">
        <label for="username">{{ _('Username') }}</label>
        <input type="text" name="username" id="username" required>
        <label for="password">{{ _('Password') }}</label>
        <input type="password" name="password" id="password" required>
        <button type="submit">{{ _('Register') }}</button>
    </form>
    <a href="{{ url_for('login') }}">{{ _('Already have an account? Login') }}</a>
</body>
</html>
```

#### `login.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ _('Login') }}</title>
</head>
<body>
    <h1>{{ _('Login') }}</h1>
    <form method="POST" action="{{ url_for('login') }}">
        <label for="username">{{ _('Username') }}</label>
        <input type="text" name="username" id="username" required>
        <label for="password">{{ _('Password') }}</label>
        <input type="password" name="password" id="password" required>
        <button type="submit">{{ _('Login') }}</button>
    </form>
    <a href="{{ url_for('register') }}">{{ _('Don\'t have an account? Register') }}</a>
</body>
</html>
```

#### `dashboard.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ _('Dashboard') }}</title>
</head>
<body>
    <h1>{{ _('Welcome,') }} {{ username }}!</h1>
    <a href="{{ url_for('logout') }}">{{ _('Logout') }}</a>
</body>
</html>
```
