"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: Write code to implement a login page with fields for username and password, including functionality for "Forgot Password" and "Recover Password" as described on the Empower login page.
Generated: DETERMINISTIC_786cf12323b35d68
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key for production

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Replace with your password
mail = Mail(app)

# Form class for login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Form class for password recovery
class RecoverForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Recover Password')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # Simulated user authentication (replace with database check)
        if username == 'user' and password == 'pass':
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'danger')

    return render_template('login.html', form=form)

@app.route('/recover', methods=['GET', 'POST'])
def recover():
    form = RecoverForm()
    
    if form.validate_on_submit():
        email = form.email.data
        
        # Simulated email sending (replace with actual email logic)
        try:
            msg = Message('Password Recovery', sender=app.config['MAIL_USERNAME'], recipients=[email])
            msg.body = 'Click here to recover your password.'
            mail.send(msg)
            flash('Recovery email sent!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Error sending email: ' + str(e), 'danger')

    return render_template('recover.html', form=form)

@app.route('/dashboard')
def dashboard():
    return 'Welcome to your dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and Flask-WTF installed in your environment (use `pip install Flask Flask-WTF Flask-Mail`).
- Replace SMTP configuration and email credentials with your real email setup.
- The user authentication is simulated; you would typically check against a database.
- Templates (`login.html` and `recover.html`) should be created in the `templates` directory according to your UI design.
