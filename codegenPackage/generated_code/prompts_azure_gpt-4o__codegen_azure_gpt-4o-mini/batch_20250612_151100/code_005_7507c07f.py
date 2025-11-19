"""
Generated Code Metadata:
========================
Original URL: https://nvidiatechnologies.com
Prompt: Suggest tools and frameworks for designing a Learning Management System (LMS) with audio and quiz features, referencing Nvidia Technologies' IELTS Tutor project.
Generated: DETERMINISTIC_7507c07f5c7a255e
Batch ID: 20250612_151100
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
from flask_migrate import Migrate
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Quiz model
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    questions = db.relationship('Question', backref='quiz', lazy=True)

# Define the Question model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    options = db.Column(db.JSON, nullable=False)  # Store options as JSON
    correct_answer = db.Column(db.String(100), nullable=False)

# Define the Audio model
class Audio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)

# API endpoint to create a new quiz
@app.route('/quizzes', methods=['POST'])
def create_quiz():
    try:
        data = request.get_json()
        new_quiz = Quiz(title=data['title'])
        db.session.add(new_quiz)
        db.session.commit()
        return jsonify({'message': 'Quiz created successfully!', 'quiz_id': new_quiz.id}), 201
    except Exception as e:
        logging.error(f"Error creating quiz: {e}")
        return jsonify({'error': 'Failed to create quiz'}), 500

# API endpoint to add a question to a quiz
@app.route('/quizzes/<int:quiz_id>/questions', methods=['POST'])
def add_question(quiz_id):
    try:
        data = request.get_json()
        new_question = Question(
            quiz_id=quiz_id,
            text=data['text'],
            options=data['options'],
            correct_answer=data['correct_answer']
        )
        db.session.add(new_question)
        db.session.commit()
        return jsonify({'message': 'Question added successfully!', 'question_id': new_question.id}), 201
    except Exception as e:
        logging.error(f"Error adding question: {e}")
        return jsonify({'error': 'Failed to add question'}), 500

# API endpoint to upload audio
@app.route('/audio', methods=['POST'])
def upload_audio():
    try:
        data = request.get_json()
        new_audio = Audio(title=data['title'], file_path=data['file_path'])
        db.session.add(new_audio)
        db.session.commit()
        return jsonify({'message': 'Audio uploaded successfully!', 'audio_id': new_audio.id}), 201
    except Exception as e:
        logging.error(f"Error uploading audio: {e}")
        return jsonify({'error': 'Failed to upload audio'}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
