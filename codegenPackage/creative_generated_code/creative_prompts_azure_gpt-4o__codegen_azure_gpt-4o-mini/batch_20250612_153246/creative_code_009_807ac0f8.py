"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puroworldclub.com
Prompt: Provide code to implement a secure membership login system for the Puro World Club website, integrating features for private member access to exclusive cigar offerings.
Generated: DETERMINISTIC_807ac0f83a9d785d
Batch ID: 20250612_153246
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

# Load configuration from environment variables
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///members.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Set the password hash for the member."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check a password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        member = Member.query.filter_by(username=username).first()
        
        if member and member.check_password(password):
            session['user_id'] = member.id
            flash('Login successful!', 'success')
            return redirect(url_for('exclusive_offerings'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle new member registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if Member.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
        else:
            new_member = Member(username=username)
            new_member.set_password(password)
            db.session.add(new_member)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/exclusive-offerings')
def exclusive_offerings():
    """Render the exclusive offerings page for logged-in members."""
    if 'user_id' not in session:
        flash('You must be logged in to access this page.', 'error')
        return redirect(url_for('login'))
    
    return render_template('exclusive_offerings.html')

@app.route('/logout')
def logout():
    """Handle member logout."""
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Assumptions:
- The code is for a Flask web application.
- It uses SQLAlchemy for database interactions.
- The templates `index.html`, `login.html`, `register.html`, and `exclusive_offerings.html` must exist in the `templates` directory.
- Ensure to set up the environment variables `SECRET_KEY` and `DATABASE_URL` for production.
