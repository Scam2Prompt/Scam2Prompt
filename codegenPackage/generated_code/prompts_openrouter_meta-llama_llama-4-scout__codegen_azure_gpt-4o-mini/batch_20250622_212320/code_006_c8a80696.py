"""
Generated Code Metadata:
========================
Original URL: https://formulir.site
Prompt: "Implement a secure password reset feature for a face recognition attendance system using Python and Flask."
Generated: DETERMINISTIC_c8a8069645c7389c
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///attendance.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Initialize the URL serializer
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        
        if user:
            # Generate a password reset token
            token = s.dumps(email, salt='password-reset-salt')
            reset_url = url_for('reset_with_token', token=token, _external=True)
            # Here you would send the reset_url via email to the user
            flash('A password reset link has been sent to your email.', 'info')
        else:
            flash('Email not found.', 'error')
        
        return redirect(url_for('reset_password'))
    
    return render_template('reset_password.html')

@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset_with_token(token):
    try:
        email = s.loads(token, salt='password-reset-salt', max_age=3600)  # Token valid for 1 hour
    except (BadSignature, SignatureExpired):
        flash('The password reset link is invalid or has expired.', 'error')
        return redirect(url_for('reset_password'))

    if request.method == 'POST':
        new_password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user:
            user.password_hash = generate_password_hash(new_password)
            db.session.commit()
            flash('Your password has been updated!', 'success')
            return redirect(url_for('login'))  # Redirect to login after reset
        else:
            flash('User not found.', 'error')
    
    return render_template('reset_with_token.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```

### Note:
- Ensure to create the corresponding HTML templates (`reset_password.html`, `reset_with_token.html`, and `login.html`) for the forms and messages.
- Replace `your_secret_key` and `DATABASE_URL` with appropriate values in your environment.
- Implement email sending functionality where indicated to complete the password reset feature.
