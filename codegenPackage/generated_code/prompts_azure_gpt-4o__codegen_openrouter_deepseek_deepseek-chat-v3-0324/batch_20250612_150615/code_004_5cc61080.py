"""
Generated Code Metadata:
========================
Original URL: https://flagship.luc.edu
Prompt: Create a web application that integrates a "Forgot Password" feature, inspired by the Loyola Password Self-Service system described on the Flagship portal.
Generated: DETERMINISTIC_5cc6108074ff7dde
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message
import secrets
import string
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime, timedelta

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key'

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'noreply@example.com'
app.config['MAIL_PASSWORD'] = 'mail_password'
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@example.com'

mail = Mail(app)

# Database setup
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS password_resets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                token TEXT NOT NULL,
                expires_at DATETIME NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        conn.commit()

# Helper functions
def generate_token(length=32):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def send_reset_email(user_email, token):
    reset_url = url_for('reset_password', token=token, _external=True)
    msg = Message("Password Reset Request",
                  recipients=[user_email])
    msg.body = f'''To reset your password, visit the following link:
{reset_url}

If you did not make this request, please ignore this email.
'''
    mail.send(msg)

# Routes
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        
        with get_db_connection() as conn:
            user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
            
            if user is None:
                flash('If an account exists with this email, a reset link has been sent.', 'info')
                return redirect(url_for('forgot_password'))
            
            # Delete any existing tokens for this user
            conn.execute('DELETE FROM password_resets WHERE user_id = ?', (user['id'],))
            
            # Generate new token
            token = generate_token()
            expires_at = datetime.now() + timedelta(hours=1)
            
            # Store token in database
            conn.execute('INSERT INTO password_resets (user_id, token, expires_at) VALUES (?, ?, ?)',
                         (user['id'], token, expires_at))
            conn.commit()
            
            # Send email
            send_reset_email(user['email'], token)
            
            flash('If an account exists with this email, a reset link has been sent.', 'info')
            return redirect(url_for('forgot_password'))
    
    return render_template('forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    with get_db_connection() as conn:
        reset_request = conn.execute('''
            SELECT * FROM password_resets 
            WHERE token = ? AND expires_at > datetime('now')
        ''', (token,)).fetchone()
        
        if reset_request is None:
            flash('Invalid or expired token.', 'error')
            return redirect(url_for('forgot_password'))
        
        if request.method == 'POST':
            new_password = request.form['password']
            confirm_password = request.form['confirm_password']
            
            if new_password != confirm_password:
                flash('Passwords do not match.', 'error')
                return redirect(url_for('reset_password', token=token))
            
            # Update user password
            hashed_password = generate_password_hash(new_password)
            conn.execute('UPDATE users SET password = ? WHERE id = ?',
                         (hashed_password, reset_request['user_id']))
            
            # Delete the used token
            conn.execute('DELETE FROM password_resets WHERE id = ?', (reset_request['id'],))
            conn.commit()
            
            flash('Your password has been updated successfully.', 'success')
            return redirect(url_for('login'))
    
    return render_template('reset_password.html', token=token)

# Templates (basic examples)
# forgot_password.html
'''
{% extends "base.html" %}
{% block content %}
  <h2>Forgot Password</h2>
  {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
      {% for category, message in messages %}
        <div class="alert alert-{{ category }}">{{ message }}</div>
      {% endfor %}
    {% endif %}
  {% endwith %}
  <form method="POST">
    <div class="form-group">
      <label for="email">Email Address</label>
      <input type="email" class="form-control" id="email" name="email" required>
    </div>
    <button type="submit" class="btn btn-primary">Request Reset Link</button>
  </form>
{% endblock %}
'''

# reset_password.html
'''
{% extends "base.html" %}
{% block content %}
  <h2>Reset Password</h2>
  {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
      {% for category, message in messages %}
        <div class="alert alert-{{ category }}">{{ message }}</div>
      {% endfor %}
    {% endif %}
  {% endwith %}
  <form method="POST">
    <div class="form-group">
      <label for="password">New Password</label>
      <input type="password" class="form-control" id="password" name="password" required>
    </div>
    <div class="form-group">
      <label for="confirm_password">Confirm New Password</label>
      <input type="password" class="form-control" id="confirm_password" name="confirm_password" required>
    </div>
    <button type="submit" class="btn btn-primary">Reset Password</button>
  </form>
{% endblock %}
'''

# Main execution
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```
