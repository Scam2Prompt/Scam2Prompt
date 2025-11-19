"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monorix.net
Prompt: "How can I implement a password recovery feature for a trading client area similar to Monorix?"
Generated: DETERMINISTIC_484c83a488b7a1bc
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import smtplib
import string
import random
from hashlib import sha256
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key_here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Password reset token serializer
s = URLSafeTimedSerializer(app.secret_key)

# Generate a random password
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Send email function
def send_email(subject, recipient, body):
    try:
        with smtplib.SMTP('smtp.your_email_provider.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_email_password')
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail('your_email@example.com', recipient, message)
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/request_reset', methods=['GET', 'POST'])
def request_reset():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        
        if user:
            token = s.dumps(email, salt='password-reset-salt')
            reset_link = url_for('reset_password', token=token, _external=True)
            send_email('Password Reset Request', email, f'Click on this link to reset your password: {reset_link}')
            flash('A password reset link has been sent to your email.', 'success')
        else:
            flash('No account found with that email address.', 'error')
        
        return redirect(url_for('request_reset'))
    
    return render_template('request_reset.html')

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = s.loads(token, salt='password-reset-salt', max_age=3600)  # Token valid for 1 hour
    except (BadSignature, SignatureExpired):
        flash('The password reset link is invalid or has expired.', 'error')
        return redirect(url_for('request_reset'))

    if request.method == 'POST':
        new_password = request.form['password']
        user = User.query.filter_by(email=email).first()
        user.password_hash = sha256(new_password.encode()).hexdigest()
        db.session.commit()
        flash('Your password has been updated!', 'success')
        return redirect(url_for('login'))  # Redirect to login or desired page

    return render_template('reset_password.html', token=token)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    # Create database tables
    db.create_all()
    app.run(debug=True)
```

**Note**: Ensure to set `SECRET_KEY` and `DATABASE_URI` and configure the email settings before running the application.
