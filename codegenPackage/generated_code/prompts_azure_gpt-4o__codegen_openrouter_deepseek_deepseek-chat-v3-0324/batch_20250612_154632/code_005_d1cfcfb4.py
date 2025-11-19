"""
Generated Code Metadata:
========================
Original URL: https://uembark.org
Prompt: Write code to implement a "mentor helpline" feature where users can submit questions to a database and receive responses from mentors, as outlined on uEmbark.
Generated: DETERMINISTIC_d1cfcfb4a9e9e643
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///mentor_helpline.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_mentor = db.Column(db.Boolean, default=False)
    
    questions = db.relationship('Question', backref='asker', lazy=True)
    responses = db.relationship('Response', backref='mentor', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    responses = db.relationship('Response', backref='question', lazy=True, cascade='all, delete-orphan')

class Response(db.Model):
    __tablename__ = 'responses'
    
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# API routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    user = User(
        username=data['username'],
        email=data['email'],
        is_mentor=data.get('is_mentor', False)
    )
    user.set_password(data['password'])
    
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing username or password'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401
    
    return jsonify({
        'message': 'Login successful',
        'user_id': user.id,
        'is_mentor': user.is_mentor
    }), 200

@app.route('/api/questions', methods=['GET', 'POST'])
def handle_questions():
    if request.method == 'GET':
        questions = Question.query.order_by(Question.timestamp.desc()).all()
        return jsonify([{
            'id': q.id,
            'title': q.title,
            'body': q.body,
            'timestamp': q.timestamp.isoformat(),
            'user_id': q.user_id
        } for q in questions]), 200
    
    elif request.method == 'POST':
        data = request.get_json()
        
        if not data or 'title' not in data or 'body' not in data or 'user_id' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
        
        user = User.query.get(data['user_id'])
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        question = Question(
            title=data['title'],
            body=data['body'],
            user_id=data['user_id']
        )
        
        try:
            db.session.add(question)
            db.session.commit()
            return jsonify({'message': 'Question submitted successfully'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

@app.route('/api/questions/<int:question_id>', methods=['GET', 'DELETE'])
def handle_question(question_id):
    question = Question.query.get_or_404(question_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': question.id,
            'title': question.title,
            'body': question.body,
            'timestamp': question.timestamp.isoformat(),
            'user_id': question.user_id,
            'responses': [{
                'id': r.id,
                'body': r.body,
                'timestamp': r.timestamp.isoformat(),
                'mentor_id': r.mentor_id
            } for r in question.responses]
        }), 200
    
    elif request.method == 'DELETE':
        try:
            db.session.delete(question)
            db.session.commit()
            return jsonify({'message': 'Question deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

@app.route('/api/questions/<int:question_id>/responses', methods=['GET', 'POST'])
def handle_responses(question_id):
    question = Question.query.get_or_404(question_id)
    
    if request.method == 'GET':
        return jsonify([{
            'id': r.id,
            'body': r.body,
            'timestamp': r.timestamp.isoformat(),
            'mentor_id': r.mentor_id,
            'question_id': r.question_id
        } for r in question.responses]), 200
    
    elif request.method == 'POST':
        data = request.get_json()
        
        if not data or 'body' not in data or 'mentor_id' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
        
        mentor = User.query.get(data['mentor_id'])
        if not mentor or not mentor.is_mentor:
            return jsonify({'error': 'Only mentors can respond to questions'}), 403
        
        response = Response(
            body=data['body'],
            mentor_id=data['mentor_id'],
            question_id=question_id
        )
        
        try:
            db.session.add(response)
            db.session.commit()
            return jsonify({'message': 'Response submitted successfully'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
