"""
Generated Code Metadata:
========================
Original URL: https://bridgestoprofessions.com
Prompt: Generate code for a web application that simulates mock interviews, incorporating key interview techniques and feedback mechanisms inspired by the interview preparation services offered by Bridges to Professions.
Generated: DETERMINISTIC_7e04f28347e5cd56
Batch ID: 20250612_145444
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import random
import os
from functools import wraps

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interview_simulator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    interviews = db.relationship('Interview', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    interview_type = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    feedback = db.relationship('Feedback', backref='interview', lazy=True)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    interview_id = db.Column(db.Integer, db.ForeignKey('interview.id'), nullable=False)
    question = db.Column(db.String(500), nullable=False)
    user_response = db.Column(db.String(1000))
    feedback_text = db.Column(db.String(1000))
    score = db.Column(db.Integer)

# Interview questions database
INTERVIEW_QUESTIONS = {
    'technical': [
        "Explain the concept of object-oriented programming.",
        "What are the differences between SQL and NoSQL databases?",
        "How would you optimize a slow-running database query?",
        "Explain the SOLID principles in software development.",
        "Describe your approach to debugging complex issues."
    ],
    'behavioral': [
        "Tell me about a time you faced a difficult challenge and how you overcame it.",
        "Describe a situation where you had to work with a difficult team member.",
        "Give an example of how you handled a mistake you made at work.",
        "How do you prioritize tasks when working on multiple projects?",
        "Tell me about a time you demonstrated leadership skills."
    ],
    'case_study': [
        "How would you design a ride-sharing app like Uber?",
        "Estimate the number of gas stations in New York City.",
        "A client reports declining sales. How would you approach this problem?",
        "Design a recommendation system for an e-commerce platform.",
        "How would you improve user engagement for a social media app?"
    ]
}

# Decorator for login required
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error='Username already exists')
        if User.query.filter_by(email=email).first():
            return render_template('register.html', error='Email already exists')
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    interviews = Interview.query.filter_by(user_id=user.id).order_by(Interview.date.desc()).all()
    return render_template('dashboard.html', user=user, interviews=interviews)

@app.route('/start_interview', methods=['GET', 'POST'])
@login_required
def start_interview():
    if request.method == 'POST':
        interview_type = request.form['interview_type']
        new_interview = Interview(
            user_id=session['user_id'],
            interview_type=interview_type
        )
        db.session.add(new_interview)
        db.session.commit()
        return redirect(url_for('conduct_interview', interview_id=new_interview.id))
    return render_template('start_interview.html')

@app.route('/interview/<int:interview_id>', methods=['GET', 'POST'])
@login_required
def conduct_interview(interview_id):
    interview = Interview.query.get_or_404(interview_id)
    if interview.user_id != session['user_id']:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        question = request.form['question']
        user_response = request.form['response']
        
        # Simple feedback generation (in a real app, this would be more sophisticated)
        feedback_text = generate_feedback(question, user_response)
        score = random.randint(3, 5)  # Random score for demo
        
        new_feedback = Feedback(
            interview_id=interview_id,
            question=question,
            user_response=user_response,
            feedback_text=feedback_text,
            score=score
        )
        db.session.add(new_feedback)
        db.session.commit()
        
        return jsonify({
            'feedback': feedback_text,
            'score': score,
            'next_question': get_next_question(interview.interview_type)
        })
    
    first_question = get_next_question(interview.interview_type)
    return render_template('conduct_interview.html', interview=interview, question=first_question)

def get_next_question(interview_type):
    questions = INTERVIEW_QUESTIONS.get(interview_type, [])
    return random.choice(questions) if questions else "No questions available for this interview type."

def generate_feedback(question, response):
    # This is a simplified feedback generator
    # In a real application, this would use NLP or more sophisticated rules
    feedback = []
    
    if len(response.split()) < 20:
        feedback.append("Your answer could be more detailed. Try to elaborate with specific examples.")
    else:
        feedback.append("Good job providing a detailed response!")
    
    if '?' not in response and 'I' in response:
        feedback.append("Consider framing your answer more confidently by avoiding overuse of 'I'.")
    
    if len(response) > 0:
        feedback.append("Remember to structure your answer using the STAR method (Situation, Task, Action, Result) for behavioral questions.")
    
    return " ".join(feedback)

@app.route('/interview/<int:interview_id>/results')
@login_required
def interview_results(interview_id):
    interview = Interview.query.get_or_404(interview_id)
    if interview.user_id != session['user_id']:
        return redirect(url_for('dashboard'))
    
    feedbacks = Feedback.query.filter_by(interview_id=interview_id).all()
    avg_score = sum(f.score for f in feedbacks) / len(feedbacks) if feedbacks else 0
    
    return render_template('interview_results.html', 
                         interview=interview, 
                         feedbacks=feedbacks,
                         avg_score=round(avg_score, 1))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interview Simulator - {% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css
