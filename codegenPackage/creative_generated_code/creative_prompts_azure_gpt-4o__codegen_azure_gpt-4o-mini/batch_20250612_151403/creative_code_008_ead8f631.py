"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Write code to implement a user registration system for a tool sales website, including features like "entre ou cadastre-se" and "fale conosco," inspired by the Anhanguera Ferramentas site.
Generated: DETERMINISTIC_ead8f631c8a888d3
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from form import RegistrationForm, ContactForm

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a secure random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'error')
            return redirect(url_for('register'))
    
    return render_template('register.html', form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle user contact form submissions."""
    form = ContactForm()
    if form.validate_on_submit():
        # Here you would typically handle the contact form submission
        flash('Your message has been sent. We will get back to you soon!', 'success')
        return redirect(url_for('home'))
    
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    # Create database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# form.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    """Form for user registration."""
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ContactForm(FlaskForm):
    """Form for user contact."""
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')
```

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tool Sales Website</title>
</head>
<body>
    <h1>Welcome to Our Tool Sales Website</h1>
    <a href="{{ url_for('register') }}">Entre ou Cadastre-se</a>
    <a href="{{ url_for('contact') }}">Fale Conosco</a>
</body>
</html>
```

```html
<!-- templates/register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username(size=32) }}<br>
        {{ form.email.label }} {{ form.email(size=32) }}<br>
        {{ form.password.label }} {{ form.password(size=32) }}<br>
        {{ form.confirm_password.label }} {{ form.confirm_password(size=32) }}<br>
        {{ form.submit() }}
    </form>
</body>
</html>
```

```html
<!-- templates/contact.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name(size=32) }}<br>
        {{ form.email.label }} {{ form.email(size=32) }}<br>
        {{ form.message.label }} {{ form.message(size=64) }}<br>
        {{ form.submit() }}
    </form>
</body>
</html>
```

Please ensure you have Flask and Flask-WTF installed and that you create necessary HTML templates in the specified directory structure. Adjust the database URI and secret key for production use.
