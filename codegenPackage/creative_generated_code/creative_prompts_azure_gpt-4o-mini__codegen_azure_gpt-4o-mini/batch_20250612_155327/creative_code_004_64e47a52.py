"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: How can I design a user-friendly interface for an employee portal that allows easy navigation and access to features like timesheet submission, as seen in the Socrates GM portal?
Generated: DETERMINISTIC_64e47a52a7e7a3b5
Batch ID: 20250612_155327
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
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a strong secret key
db = SQLAlchemy(app)

# Database model for Employee
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Database model for Timesheet
class Timesheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    hours_worked = db.Column(db.Float, nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)

# Route for the home page
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

        # Error handling for existing username
        if Employee.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another one.')
            return redirect(url_for('register'))

        new_user = Employee(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Employee.query.filter_by(username=username).first()

        # Error handling for invalid credentials
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful.')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))
    return render_template('login.html')

# Route for the user dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.')
        return redirect(url_for('login'))
    
    employee_id = session['user_id']
    timesheets = Timesheet.query.filter_by(employee_id=employee_id).all()
    return render_template('dashboard.html', timesheets=timesheets)

# Route for submitting a timesheet
@app.route('/submit_timesheet', methods=['POST'])
def submit_timesheet():
    if 'user_id' not in session:
        flash('Please log in to submit a timesheet.')
        return redirect(url_for('login'))

    employee_id = session['user_id']
    hours_worked = request.form['hours_worked']
    
    try:
        hours_worked = float(hours_worked)
        new_timesheet = Timesheet(employee_id=employee_id, hours_worked=hours_worked)
        db.session.add(new_timesheet)
        db.session.commit()
        flash('Timesheet submitted successfully.')
    except ValueError:
        flash('Invalid hours worked. Please enter a numeric value.')
    except Exception as e:
        flash(f'An error occurred: {str(e)}')
    
    return redirect(url_for('dashboard'))

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('home'))

# Function to create the database
def create_db():
    with app.app_context():
        db.create_all()

# Entry point for the application
if __name__ == '__main__':
    create_db()  # Initialize the database
    app.run(debug=True)  # Run the application in debug mode
```

### HTML Templates
You will also need to create the following HTML templates in a directory named `templates`:

1. `home.html`
2. `register.html`
3. `login.html`
4. `dashboard.html`

Make sure to include appropriate forms for registering and logging in, as well as for submitting timesheets in your HTML files.
