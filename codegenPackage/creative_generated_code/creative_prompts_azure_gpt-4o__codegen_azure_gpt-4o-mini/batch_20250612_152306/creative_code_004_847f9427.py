"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Suggest a framework for developing a student login portal that integrates with the vocational training courses offered by RSP Bharat.
Generated: DETERMINISTIC_847f9427451a048f
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key and database URI
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

# Initialize the database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not authenticated

# User model for the student
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Callback function to load user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    
    return render_template('login.html')

# Route for the student dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))
        
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Function to create the database
def create_db():
    with app.app_context():
        db.create_all()

# Entry point of the application
if __name__ == '__main__':
    create_db()  # Create the database tables
    app.run(debug=True)  # Run the application in debug mode
```

**Note**: This code requires Flask, Flask-SQLAlchemy, and Flask-Login libraries. Make sure to install them via pip before running the application:

```bash
pip install Flask Flask-SQLAlchemy Flask-Login
``` 

Ensure that you implement the corresponding HTML templates (`index.html`, `login.html`, `dashboard.html`, `register.html`, `404.html`, and `500.html`) in a "templates" directory for full functionality.
