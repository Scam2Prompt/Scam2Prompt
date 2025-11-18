"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.gmprog.com
Prompt: Generate code for a web application login page that includes multilingual options (English and Russian) and uses a database for storing user credentials securely.
Generated: DETERMINISTIC_766e58419a65ac8d
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from forms import LoginForm
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secure session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and bcrypt for hashing
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
babel = Babel(app)

# Configure supported languages
LANGUAGES = {
    'en': 'English',
    'ru': 'Russian'
}

# User model for storing user credentials
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Initialize the database (only needed for the first run)
@app.before_first_request
def create_tables():
    db.create_all()

# Language selection function
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():  # Validate form
        user = User.query.filter_by(username=form.username.data).first()
        
        # Check if user exists and password is valid
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id  # Store user ID in session
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html', form=form)

# Dashboard route (protected)
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Clear user session
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

```html
<!-- login.html -->
<!DOCTYPE html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% trans %}Login{% endtrans %}</title>
</head>
<body>
    <h1>{% trans %}Login{% endtrans %}</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            <label for="username">{% trans %}Username{% endtrans %}</label>
            {{ form.username(size=32) }}
        </div>
        <div>
            <label for="password">{% trans %}Password{% endtrans %}</label>
            {{ form.password(size=32) }}
        </div>
        <button type="submit">{% trans %}Login{% endtrans %}</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

```python
# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

# Define login form structure
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=80)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
```
