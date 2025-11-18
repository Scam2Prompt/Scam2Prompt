"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica17.vercel.app
Prompt: Create a web application that allows users to log in and select between Solana, Ethereum, and Polygon networks, similar to the functionality described on Matrica17.
Generated: DETERMINISTIC_67f3926c6a2f0fe3
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('select_network'))
        else:
            flash('Login failed. Check your username and password', 'danger')
    return render_template('login.html', form=form)

# Network selection route
@app.route('/select_network')
def select_network():
    if 'user_id' not in session:
        flash('Please log in to access this page', 'warning')
        return redirect(url_for('login'))
    return render_template('select_network.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# Error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Run the app
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### HTML Templates (index.html, register.html, login.html, select_network.html)

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Network Selector</h1>
    <a href="{{ url_for('register') }}">Register</a> |
    <a href="{{ url_for('login') }}">Login</a>
</body>
</html>
```

#### register.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username() }}<br>
        {{ form.password.label }} {{ form.password() }}<br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

#### login.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username() }}<br>
        {{ form.password.label }} {{ form.password() }}<br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

#### select_network.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Select Network</title>
</head>
<body>
    <h1>Select Your Network</h1>
    <ul>
        <li><a href="#">Solana</a></li>
        <li><a href="#">Ethereum</a></li>
        <li><a href="#">Polygon</a></li>
    </ul>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```

### Forms (forms.py)
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=150)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
```

Make sure you have Flask, Flask-WTF, and Flask-SQLAlchemy installed in your Python environment. You can install these packages using:

```bash
pip install Flask Flask-WTF Flask-SQLAlchemy
```
