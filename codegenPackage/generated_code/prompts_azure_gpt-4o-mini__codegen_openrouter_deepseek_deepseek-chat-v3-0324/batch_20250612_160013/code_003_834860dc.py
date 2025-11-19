"""
Generated Code Metadata:
========================
Original URL: https://prohappyfamily.com
Prompt: Develop a simple web application that allows users to track their personal growth and relationship improvements, utilizing the strategies outlined in the "Счастливая жена - счастливая семья" program.
Generated: DETERMINISTIC_834860dc320e768c
Batch ID: 20250612_160013
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
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///growth_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    entries = db.relationship('GrowthEntry', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class GrowthEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'communication', 'trust', 'intimacy'
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-10 scale
    action_plan = db.Column(db.Text)

# Create database tables
with app.app_context():
    db.create_all()

# Helper functions
def get_current_user():
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    return None

# Routes
@app.route('/')
def index():
    user = get_current_user()
    if user:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return redirect(url_for('register'))
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        flash('Logged in successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    
    entries = GrowthEntry.query.filter_by(user_id=user.id).order_by(GrowthEntry.date.desc()).all()
    return render_template('dashboard.html', user=user, entries=entries)

@app.route('/add_entry', methods=['GET', 'POST'])
def add_entry():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        category = request.form['category']
        description = request.form['description']
        rating = int(request.form['rating'])
        action_plan = request.form.get('action_plan', '')
        
        new_entry = GrowthEntry(
            user_id=user.id,
            category=category,
            description=description,
            rating=rating,
            action_plan=action_plan
        )
        
        db.session.add(new_entry)
        db.session.commit()
        
        flash('Entry added successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_entry.html')

@app.route('/edit_entry/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    
    entry = GrowthEntry.query.get_or_404(entry_id)
    
    if entry.user_id != user.id:
        flash('You are not authorized to edit this entry', 'error')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        entry.category = request.form['category']
        entry.description = request.form['description']
        entry.rating = int(request.form['rating'])
        entry.action_plan = request.form.get('action_plan', '')
        
        db.session.commit()
        flash('Entry updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('edit_entry.html', entry=entry)

@app.route('/delete_entry/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    
    entry = GrowthEntry.query.get_or_404(entry_id)
    
    if entry.user_id != user.id:
        flash('You are not authorized to delete this entry', 'error')
        return redirect(url_for('dashboard'))
    
    db.session.delete(entry)
    db.session.commit()
    flash('Entry deleted successfully', 'success')
    return redirect(url_for('dashboard'))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
