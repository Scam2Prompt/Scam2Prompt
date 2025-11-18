"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter.graphy.com
Prompt: Recommend libraries or APIs to implement a feature for tracking user performance in live tests and quizzes, as described on Jupiter Swap™.
Generated: DETERMINISTIC_c78a8abe2ec619c1
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation in Python for tracking user performance in live tests and quizzes using `Flask` for the API backend and `SQLAlchemy` for database handling.

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///performance_tracking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the UserPerformance model
class UserPerformance(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the table
    user_id = db.Column(db.String(50), nullable=False)  # Unique identifier for the user
    quiz_id = db.Column(db.String(50), nullable=False)  # Unique identifier for the quiz/test
    score = db.Column(db.Float, nullable=False)  # User's score
    total_questions = db.Column(db.Integer, nullable=False)  # Total number of questions in the quiz
    correct_answers = db.Column(db.Integer, nullable=False)  # Number of correct answers
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp when the entry is created

    def to_dict(self):
        """Converts the model instance to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "quiz_id": self.quiz_id,
            "score": self.score,
            "total_questions": self.total_questions,
            "correct_answers": self.correct_answers,
            "timestamp": self.timestamp.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to record user performance
@app.route('/api/performance', methods=['POST'])
def record_performance():
    """
    Record user performance in a quiz or test.
    Expects JSON payload with user_id, quiz_id, score, total_questions, and correct_answers.
    """
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input, JSON payload required"}), 400

        # Validate required fields
        required_fields = ['user_id', 'quiz_id', 'score', 'total_questions', 'correct_answers']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Create a new UserPerformance record
        performance = UserPerformance(
            user_id=data['user_id'],
            quiz_id=data['quiz_id'],
            score=data['score'],
            total_questions=data['total_questions'],
            correct_answers=data['correct_answers']
        )
        db.session.add(performance)
        db.session.commit()

        # Return success response
        return jsonify({"message": "Performance recorded successfully", "performance": performance.to_dict()}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while recording performance", "details": str(e)}), 500

# Route to retrieve user performance
@app.route('/api/performance/<user_id>', methods=['GET'])
def get_user_performance(user_id):
    """
    Retrieve user performance data based on the user_id.
    """
    try:
        # Query the database for performance records for the given user ID
        performances = UserPerformance.query.filter_by(user_id=user_id).all()
        if not performances:
            return jsonify({"message": "No performance records found for this user"}), 404

        # Return the performance records as a JSON response
        return jsonify({"performances": [p.to_dict() for p in performances]}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while retrieving performance", "details": str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Features:
- RESTful API endpoints for recording (`POST /api/performance`) and retrieving (`GET /api/performance/<user_id>`) user performance.
- SQLite database for lightweight, persistent storage.
- Proper error handling for missing data and unexpected exceptions.
- Follows Python's PEP 8 style guide for clean and maintainable code.

To run the code:
1. Install required libraries: `pip install flask flask-sqlalchemy`.
2. Save the code in a Python file (e.g., `app.py`).
3. Run the application using `python app.py`.
