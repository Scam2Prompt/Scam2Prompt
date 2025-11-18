"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Write Python code to create a basic educational platform similar to the "Notebook" platform mentioned on the Del Sol Montessori website, allowing students and parents to track academic progress and communicate with teachers.
Generated: DETERMINISTIC_2224d19c172ae1f2
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Educational Platform Code
This Python application provides a basic platform to track academic progress and facilitate communication
between students, parents, and teachers. It uses Flask for the web framework and SQLite for the database.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure, random key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///educational_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    """
    Represents a user in the system (students, parents, teachers).
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Role: 'student', 'parent', 'teacher'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Grade(db.Model):
    """
    Represents a grade record associated with a student.
    """
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Message(db.Model):
    """
    Represents a message exchanged between users.
    """
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/')
def home():
    """
    Home route displaying a welcome message.
    """
    return render_template('home.html')  # Create a corresponding HTML template

@app.route('/users', methods=['GET', 'POST'])
def users():
    """
    Route to manage users. Supports viewing all users and adding new ones.
    """
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            role = request.form['role']
            new_user = User(name=name, email=email, role=role)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    users = User.query.all()
    return render_template('users.html', users=users)  # Create a corresponding HTML template

@app.route('/grades', methods=['GET', 'POST'])
def grades():
    """
    Route to manage grades. Supports viewing grades and adding new ones.
    """
    if request.method == 'POST':
        try:
            student_id = request.form['student_id']
            course = request.form['course']
            grade = request.form['grade']
            new_grade = Grade(student_id=student_id, course=course, grade=grade)
            db.session.add(new_grade)
            db.session.commit()
            flash('Grade added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    grades = Grade.query.all()
    users = User.query.filter_by(role='student').all()
    return render_template('grades.html', grades=grades, users=users)  # Create a corresponding HTML template

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    """
    Route to manage messages. Supports viewing messages and sending new ones.
    """
    if request.method == 'POST':
        try:
            sender_id = request.form['sender_id']
            recipient_id = request.form['recipient_id']
            content = request.form['content']
            new_message = Message(sender_id=sender_id, recipient_id=recipient_id, content=content)
            db.session.add(new_message)
            db.session.commit()
            flash('Message sent successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    messages = Message.query.all()
    users = User.query.all()
    return render_template('messages.html', messages=messages, users=users)  # Create corresponding HTML template

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully.
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors gracefully.
    """
    return render_template('500.html'), 500

# Database Initialization
@app.before_first_request
def create_tables():
    """
    Create the database tables before the first request.
    """
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**Note:** This code assumes the use of HTML templates (`home.html`, `users.html`, `grades.html`, `messages.html`, `404.html`, and `500.html`) for rendering views, which you would need to create separately. The `educational_platform.db` SQLite database will be generated in the project's directory when the application runs.
