"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holders.sellpass.io
Prompt: Develop a dashboard for customers to access previous orders and manage on-site balances using Sellpass features.
Generated: DETERMINISTIC_6b2095bbd45324fb
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sellpass.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Database model for orders
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    user = db.relationship('User', backref=db.backref('orders', lazy=True))

# Function to create the database (run once)
@app.before_first_request
def create_tables():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        # Error handling for existing usernames
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Error handling for login credentials
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        flash('Login failed. Check your username and/or password.')
        return redirect(url_for('login'))
    return render_template('login.html')

# Route for user dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access your dashboard.')
        return redirect(url_for('login'))

    # Fetch user orders
    user_orders = Order.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', orders=user_orders)

# Route for managing balances (stub)
@app.route('/balance', methods=['GET', 'POST'])
def manage_balance():
    if 'user_id' not in session:
        flash('Please log in to manage your balance.')
        return redirect(url_for('login'))

    # This stub can be expanded to include actual balance management
    if request.method == 'POST':
        # Handle balance management logic here
        flash('Balance updated successfully.')
        return redirect(url_for('dashboard'))
    
    return render_template('balance.html')

# Route for user logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Debug mode should be off in production
```

### Notes
- Make sure to create the HTML templates (`register.html`, `login.html`, `dashboard.html`, `balance.html`, `404.html`) as needed to display the appropriate views.
- For production, consider using a more robust database such as PostgreSQL or MySQL instead of SQLite.
- Always turn off debug mode when deploying to a production environment.
