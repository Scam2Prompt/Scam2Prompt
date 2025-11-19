"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zushi.shop
Prompt: How can I implement a password-protected access feature for an online store like ZUSHI WAVE SHOP?
Generated: DETERMINISTIC_62180a4579635266
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, render_template, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model to store user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Decorator to require login for certain routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You need to log in first.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for displaying the login form
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
            return redirect(url_for('protected_area'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
    return render_template('login.html')

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Protected route that requires login
@app.route('/protected')
@login_required
def protected_area():
    return render_template('protected.html')

# Route to register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password before storing it
        hashed_password = generate_password_hash(password, method='sha256')
        
        # Create a new user instance
        new_user = User(username=username, password=hashed_password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'error')
            print(f"Error occurred: {e}")  # Log the error for debugging purposes
    return render_template('register.html')

# Initialize the database
with app.app_context():
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
