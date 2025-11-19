"""
Generated Code Metadata:
========================
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: How can I integrate a password reset feature, similar to the one on the Vertiv GmbH Mitarbeiterangebote page, into my web application?
Generated: DETERMINISTIC_13b931fd7c018ee6
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Password Reset Feature Implementation
# Requires Flask, Flask-Mail, itsdangerous, and a database ORM (SQLAlchemy shown here)

from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.example.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@example.com')

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    reset_token = db.Column(db.String(200))
    reset_token_expires = db.Column(db.DateTime)

    def generate_reset_token(self):
        self.reset_token = serializer.dumps(self.email, salt='password-reset-salt')
        self.reset_token_expires = datetime.utcnow() + timedelta(hours=1)
        db.session.commit()
        return self.reset_token

# Routes
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        
        if user:
            token = user.generate_reset_token()
            reset_url = url_for('reset_password', token=token, _external=True)
            
            msg = Message(
                "Password Reset Request",
                recipients=[user.email],
                body=f"To reset your password, visit the following link: {reset_url}\n"
                     f"This link will expire in 1 hour."
            )
            
            try:
                mail.send(msg)
                flash('Password reset link has been sent to your email.', 'success')
            except Exception as e:
                app.logger.error(f"Failed to send email: {str(e)}")
                flash('Failed to send password reset email. Please try again later.', 'error')
        
        flash('If your email exists in our system, you will receive a password reset link.', 'info')
        return redirect(url_for('forgot_password'))
    
    return render_template('forgot_password.html')

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)
    except:
        flash('The password reset link is invalid or has expired.', 'error')
        return redirect(url_for('forgot_password'))
    
    user = User.query.filter_by(email=email).first()
    if not user or user.reset_token != token or user.reset_token_expires < datetime.utcnow():
        flash('The password reset link is invalid or has expired.', 'error')
        return redirect(url_for('forgot_password'))
    
    if request.method == 'POST':
        new_password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if new_password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(request.url)
        
        # In a real app, you would hash the password here
        user.password = new_password
        user.reset_token = None
        user.reset_token_expires = None
        db.session.commit()
        
        flash('Your password has been updated successfully.', 'success')
        return redirect(url_for('login'))
    
    return render_template('reset_password.html', token=token)

# HTML Templates (basic examples)
"""
forgot_password.html:
<form method="POST">
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <button type="submit">Reset Password</button>
</form>

reset_password.html:
<form method="POST">
    <input type="hidden" name="token" value="{{ token }}">
    <label for="password">New Password:</label>
    <input type="password" id="password" name="password" required>
    <label for="confirm_password">Confirm Password:</label>
    <input type="password" id="confirm_password" name="confirm_password" required>
    <button type="submit">Update Password</button>
</form>
"""

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
