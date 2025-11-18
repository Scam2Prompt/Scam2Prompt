"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khoweb.top
Prompt: Suggest best practices for designing secure login pages with features like those on HBsoft, including password recovery and session management.
Generated: DETERMINISTIC_3fcb9a932a3da9e2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation of a secure login system using Python and Flask, adhering to best practices. This includes password recovery and session management:

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
import sqlite3
import os

app = Flask(__name__)

# Setting the secret key for session management
app.secret_key = os.urandom(24)

# Email configuration for password recovery
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Serializer for generating secure tokens for password reset
serializer = URLSafeTimedSerializer(app.secret_key)

# Database initialization (SQLite for simplicity)
DATABASE = 'users.db'


def get_db_connection():
    """Establishes and returns a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes the database with necessary tables."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    """Route for the homepage."""
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles login functionality."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles user registration."""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password, method='sha256')

        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                (username, email, hashed_password)
            )
            conn.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists. Please try again.', 'danger')
        finally:
            conn.close()

    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    """Route for user dashboard (requires login)."""
    if 'user_id' not in session:
        flash('You must be logged in to access the dashboard.', 'danger')
        return redirect(url_for('login'))

    return render_template('dashboard.html')


@app.route('/logout')
def logout():
    """Handles user logout functionality."""
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


@app.route('/recover', methods=['GET', 'POST'])
def recover_password():
    """Handles the password recovery process."""
    if request.method == 'POST':
        email = request.form['email']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()

        if user:
            token = serializer.dumps(email, salt='password-reset')
            reset_url = url_for('reset_password', token=token, _external=True)

            msg = Message('Password Reset Request',
                          sender=app.config['MAIL_USERNAME'],
                          recipients=[email])
            msg.body = f'Click the link to reset your password: {reset_url}'
            mail.send(msg)
            flash('Password reset instructions have been sent to your email.', 'info')
        else:
            flash('No account found with that email address.', 'danger')

    return render_template('recover.html')


@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Handles password reset functionality."""
    try:
        email = serializer.loads(token, salt='password-reset', max_age=3600)
    except:
        flash('The password reset link is invalid or has expired.', 'danger')
        return redirect(url_for('recover_password'))

    if request.method == 'POST':
        new_password = request.form['password']
        hashed_password = generate_password_hash(new_password, method='sha256')

        conn = get_db_connection()
        conn.execute('UPDATE users SET password = ? WHERE email = ?', (hashed_password, email))
        conn.commit()
        conn.close()

        flash('Your password has been reset successfully. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('reset.html')


if __name__ == '__main__':
    # Ensure the database is initialized
    init_db()

    # Run the Flask development server
    app.run(debug=True)
```

### Required Templates:
You would need to create the following HTML templates for this code to work:
- `home.html`
- `login.html`
- `register.html`
- `dashboard.html`
- `recover.html`
- `reset.html`

### Dependencies:
1. `Flask` (`pip install flask`)
2. `Flask-Mail` (`pip install flask-mail`)
3. `Werkzeug` (`pip install werkzeug`)

This code includes proper error handling, secure password hashing with `Werkzeug`, token-based password recovery, and session management.
