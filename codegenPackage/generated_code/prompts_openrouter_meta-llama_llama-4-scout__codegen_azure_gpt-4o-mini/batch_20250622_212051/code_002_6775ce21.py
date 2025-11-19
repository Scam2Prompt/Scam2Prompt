"""
Generated Code Metadata:
========================
Original URL: https://volatilityindexlimited.com
Prompt: Design a simple user interface for a cryptocurrency investment website with features like registration, login, and investment tracking, inspired by the Volatility Index Limited website.
Generated: DETERMINISTIC_6775ce21570cdbf0
Batch ID: 20250622_212051
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
from datetime import timedelta

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=7)

# Initialize the database
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Investment model for tracking investments
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    cryptocurrency = db.Column(db.String(50), nullable=False)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        # Hash the password and create a new user
        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')
    
    return render_template('login.html')

# Dashboard route for tracking investments
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('You need to log in first!', 'danger')
        return redirect(url_for('login'))
    
    user_investments = Investment.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', investments=user_investments)

# Add investment route
@app.route('/add_investment', methods=['POST'])
def add_investment():
    if 'user_id' not in session:
        flash('You need to log in first!', 'danger')
        return redirect(url_for('login'))
    
    amount = request.form['amount']
    cryptocurrency = request.form['cryptocurrency']
    
    # Create a new investment
    new_investment = Investment(user_id=session['user_id'], amount=float(amount), cryptocurrency=cryptocurrency)
    db.session.add(new_investment)
    db.session.commit()
    flash('Investment added successfully!', 'success')
    
    return redirect(url_for('dashboard'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```

### HTML Templates
You will need to create the following HTML templates in a `templates` directory:

1. `index.html`
2. `register.html`
3. `login.html`
4. `dashboard.html`
5. `404.html`

Make sure to include forms for registration, login, and adding investments in the respective HTML files.
