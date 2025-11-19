"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://namestajnovidom.com
Prompt: Generate a code snippet for a betting application that integrates user reviews and ratings for 토토사이트, ensuring it includes a secure login system with SSL encryption.
Generated: DETERMINISTIC_42f26dbb817bae86
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_sslify import SSLify
import os

# Initialize the Flask application
app = Flask(__name__)
sslify = SSLify(app)

# Configure the application
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model for secure login
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Define the Review model for 토토사이트 reviews
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    site_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

# Create all database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    """Home page showing all reviews."""
    reviews = Review.query.all()
    return render_template('home.html', reviews=reviews)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password for secure storage
        hashed_password = generate_password_hash(password, method='sha256')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Try a different one!', 'error')
            return redirect(url_for('register'))
        
        # Create and store the new user
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login route."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate user credentials
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'error')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Log out the user."""
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    """Route to add a new review."""
    if 'username' not in session:
        flash('You must be logged in to add a review.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        site_name = request.form['site_name']
        rating = int(request.form['rating'])
        comment = request.form['comment']
        
        # Validate rating
        if rating < 1 or rating > 5:
            flash('Rating must be between 1 and 5.', 'error')
            return redirect(url_for('add_review'))
        
        # Add the review to the database
        new_review = Review(username=session['username'], site_name=site_name, rating=rating, comment=comment)
        db.session.add(new_review)
        db.session.commit()
        flash('Review added successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('add_review.html')

# Run the application
if __name__ == '__main__':
    # Ensure the application runs securely with SSL
    app.run(ssl_context=('cert.pem', 'key.pem'))
```

Please ensure you replace `'cert.pem'` and `'key.pem'` with paths to your actual SSL certificate files.
