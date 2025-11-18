"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgestoprofessions.com
Prompt: Generate code for a web application that simulates mock interviews, incorporating key interview techniques and feedback mechanisms inspired by the interview preparation services offered by Bridges to Professions.
Generated: DETERMINISTIC_7e04f28347e5cd56
Batch ID: 20250612_145444
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.6.0.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# mock_interview_app.py

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing interview questions
class InterviewQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(250), nullable=False)

# Model for storing user feedback
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('interview_question.id'), nullable=False)
    feedback = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to render the main interview simulation page
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch a random interview question
@app.route('/api/question', methods=['GET'])
def get_question():
    try:
        question = InterviewQuestion.query.order_by(db.func.random()).first()
        if question:
            return jsonify({"question": question.question}), 200
        else:
            return jsonify({"error": "No questions available"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to submit feedback for a question
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    try:
        new_feedback = Feedback(
            question_id=data['question_id'],
            feedback=data['feedback']
        )
        db.session.add(new_feedback)
        db.session.commit()
        return jsonify({"message": "Feedback submitted successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Sample data creation
def create_sample_data():
    if InterviewQuestion.query.count() == 0:
        sample_questions = [
            "Tell me about yourself.",
            "What are your greatest strengths?",
            "What is your greatest weakness?",
            "Why do you want to work here?",
            "Where do you see yourself in five years?"
        ]
        for question in sample_questions:
            db.session.add(InterviewQuestion(question=question))
        db.session.commit()

# Run sample data creator on application start
@app.before_first_request
def setup_sample_data():
    create_sample_data()

# Main execution point
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mock Interview Simulator</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>Mock Interview Simulator</h1>
    <div>
        <button id="get-question">Get Random Question</button>
    </div>
    <div id="question-container"></div>
    <div id="feedback-container" style="display:none;">
        <h2>Feedback</h2>
        <textarea id="feedback" rows="4" cols="50"></textarea><br>
        <button id="submit-feedback">Submit Feedback</button>
    </div>
    <script>
        $(document).ready(function(){
            $('#get-question').click(function(){
                $.get('/api/question', function(data) {
                    $('#question-container').html('<p>' + data.question + '</p>');
                    $('#feedback-container').show();
                }).fail(function(err) {
                    alert("Error: " + err.responseJSON.error);
                });
            });

            $('#submit-feedback').click(function(){
                const feedbackText = $('#feedback').val();
                const questionId = $('#question-container').find('p').data('id'); // Assuming question ID is set in data-id attribute
                $.post('/api/feedback', JSON.stringify({question_id: questionId, feedback: feedbackText}), function(data) {
                    alert(data.message);
                    $('#feedback').val('');
                }, 'json').fail(function(err) {
                    alert("Error: " + err.responseJSON.error);
                });
            });
        });
    </script>
</body>
</html>
```

### Note
- Make sure to have Flask and Flask-SQLAlchemy installed in your environment. Use `pip install Flask Flask-SQLAlchemy`.
- The SQLite database will be created automatically, and sample questions will be inserted when the app starts.
- The application is set to run in debug mode for development; switch to production mode for live deployments.
