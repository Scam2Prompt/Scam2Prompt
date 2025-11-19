"""
Generated Code Metadata:
========================
Original URL: https://carthewchautaxreports.pages.dev
Prompt: Illustrate how to implement a client portal using a web framework that allows secure communication and collaboration, inspired by the services provided by Carthew Chau & Co.
Generated: DETERMINISTIC_68f7aa106299dc97
Batch ID: 20250612_155455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_portal.py
# A secure client portal implementation using Flask and Flask-Login

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
import secrets
from datetime import datetime, timedelta
import sqlite3
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['DATABASE'] = 'client_portal.db'
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'portal@example.com'
app.config['MAIL_PASSWORD'] = 'securepassword'
app.config['MAIL_DEFAULT_SENDER'] = 'portal@example.com'
app.config['SECURITY_PASSWORD_SALT'] = secrets.token_hex(16)

# Initialize extensions
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)

# Database setup
def get_db():
    db = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL,
                confirmed BOOLEAN DEFAULT FALSE,
                confirmed_on DATETIME,
                last_login DATETIME
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender_id INTEGER NOT NULL,
                recipient_id INTEGER NOT NULL,
                subject TEXT NOT NULL,
                body TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                read BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (sender_id) REFERENCES users (id),
                FOREIGN KEY (recipient_id) REFERENCES users (id)
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                filename TEXT NOT NULL,
                filepath TEXT NOT NULL,
                upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                description TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        db.commit()

# User model
class User(UserMixin):
    def __init__(self, id, email, name, confirmed):
        self.id = id
        self.email = email
        self.name = name
        self.confirmed = confirmed

# Login manager setup
@login_manager.user_loader
def load_user(user_id):
    db = get_db()
    user = db.execute('SELECT id, email, name, confirmed FROM users WHERE id = ?', (user_id,)).fetchone()
    db.close()
    if user:
        return User(user['id'], user['email'], user['name'], user['confirmed'])
    return None

# Security functions
def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email

def send_confirmation_email(user_email):
    token = generate_confirmation_token(user_email)
    confirm_url = url_for('confirm_email', token=token, _external=True)
    html = render_template('email/confirm.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(user_email, subject, html)

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        
        db = get_db()
        error = None
        
        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute('SELECT id FROM users WHERE email = ?', (email,)).fetchone() is not None:
            error = f'Email {email} is already registered.'
        
        if error is None:
            db.execute(
                'INSERT INTO users (email, password, name) VALUES (?, ?, ?)',
                (email, generate_password_hash(password), name)
            )
            db.commit()
            
            # Send confirmation email
            send_confirmation_email(email)
            
            flash('Registration successful! Please check your email to confirm your account.', 'success')
            return redirect(url_for('login'))
        
        flash(error, 'error')
    
    return render_template('register.html')

@app.route('/confirm/<token>')
def confirm_email(token):
    email = confirm_token(token)
    if not email:
        flash('The confirmation link is invalid or has expired.', 'error')
        return redirect(url_for('index'))
    
    db = get_db()
    user = db.execute('SELECT id, confirmed FROM users WHERE email = ?', (email,)).fetchone()
    
    if user['confirmed']:
        flash('Account already confirmed. Please login.', 'info')
    else:
        db.execute(
            'UPDATE users SET confirmed = TRUE, confirmed_on = ? WHERE email = ?',
            (datetime.now(), email)
        )
        db.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = True if request.form.get('remember') else False
        
        db = get_db()
        error = None
        user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        
        if user is None:
            error = 'Incorrect email.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        elif not user['confirmed']:
            error = 'Please confirm your email before logging in.'
        
        if error is None:
            # Update last login time
            db.execute(
                'UPDATE users SET last_login = ? WHERE id = ?',
                (datetime.now(), user['id'])
            )
            db.commit()
            
            # Log the user in
            login_user(User(user['id'], user['email'], user['name'], user['confirmed']), remember=remember)
            return redirect(url_for('dashboard'))
        
        flash(error, 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    # Get unread messages count
    unread_count = db.execute(
        'SELECT COUNT(*) FROM messages WHERE recipient_id = ? AND read = FALSE',
        (current_user.id,)
    ).fetchone()[0]
    
    # Get recent documents
    documents = db.execute(
        'SELECT * FROM documents WHERE user_id = ? ORDER BY upload_date DESC LIMIT 5',
        (current_user.id,)
    ).fetchall()
    
    return render_template('dashboard.html', 
                         name=current_user.name,
                         unread_count=unread_count,
                         documents=documents)

@app.route('/messages')
@login_required
def messages():
    db = get_db()
    messages = db.execute('''
        SELECT m.*, u.name as sender_name 
        FROM messages m 
        JOIN users u ON m.sender_id = u.id 
        WHERE m.recipient_id = ?
        ORDER BY m.timestamp DESC
    ''', (current_user.id,)).fetchall()
    return render_template('messages.html', messages=messages)

@app.route('/messages/<int:message_id>')
@login_required
def view_message(message_id):
    db = get_db()
    message = db.execute('''
        SELECT m.*, u.name as sender_name 
        FROM messages m 
        JOIN users u ON m.sender_id = u.id 
        WHERE m.id = ? AND m.recipient_id = ?
    ''', (message_id, current_user.id)).fetchone()
    
    if message:
        # Mark as read
