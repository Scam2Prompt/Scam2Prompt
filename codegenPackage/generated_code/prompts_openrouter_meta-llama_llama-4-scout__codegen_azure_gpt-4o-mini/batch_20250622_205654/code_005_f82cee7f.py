"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: "Develop a web application for online examination software, using a suitable programming language and framework, with features such as user authentication and result analysis, based on MDA Tech Sys's web application development services."
Generated: DETERMINISTIC_f82cee7f25308414
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exams.db'  # Database URI
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not authenticated

# User model for authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Exam model to store exam details
class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    questions = db.Column(db.Text, nullable=False)  # Store questions as JSON or text

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html')

# Route for user dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    exams = Exam.query.all()  # Fetch all exams for the user
    return render_template('dashboard.html', exams=exams)

# Route for creating a new exam
@app.route('/create_exam', methods=['GET', 'POST'])
@login_required
def create_exam():
    if request.method == 'POST':
        title = request.form['title']
        questions = request.form['questions']  # Ideally, this should be structured data
        new_exam = Exam(title=title, questions=questions)
        db.session.add(new_exam)
        db.session.commit()
        flash('Exam created successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_exam.html')

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

# Main entry point for the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### Note:
- Ensure you have the necessary HTML templates (`home.html`, `register.html`, `login.html`, `dashboard.html`, `create_exam.html`, `404.html`, `500.html`) in a `templates` directory.
- Install the required packages using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
  ```
- Replace `'your_secret_key'` with a strong, random secret key for production use.
