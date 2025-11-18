"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Create a web application for downloading medical concepts related to occupational health, similar to the platform described on Medicid IPS's website, with user authentication and secure data access.
Generated: DETERMINISTIC_e619e5de604ae488
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an implementation in Python using the Flask web framework, with SQLite for the database and proper authentication for secure data access. The code is syntactically correct, well-commented, and follows best practices.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize Flask-Login for user authentication
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class MedicalConcept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    file_path = db.Column(db.String(300), nullable=False)  # Path to downloadable files

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
            flash('Email or Username already exists!', 'error')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'error')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    concepts = MedicalConcept.query.all()
    return render_template('dashboard.html', concepts=concepts)

@app.route('/download/<int:concept_id>')
@login_required
def download(concept_id):
    concept = MedicalConcept.query.get(concept_id)
    if not concept or not os.path.exists(concept.file_path):
        flash('File not found!', 'error')
        return redirect(url_for('dashboard'))

    return send_file(concept.file_path, as_attachment=True)

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Main Execution
if __name__ == '__main__':
    if not os.path.exists('database.db'):
        db.create_all()  # Create database if it doesn't exist
    app.run(debug=True)
```

### Notes:
1. This code assumes you have Flask and its dependencies installed (`Flask`, `Flask-SQLAlchemy`, `Flask-Login`, `Werkzeug`).
2. Replace `'your_secret_key'` with a secure secret key.
3. Create templates (`index.html`, `register.html`, `login.html`, `dashboard.html`, `404.html`, `500.html`) and ensure proper UI design.
4. Add downloadable files to the appropriate file paths and ensure permissions are configured securely.
