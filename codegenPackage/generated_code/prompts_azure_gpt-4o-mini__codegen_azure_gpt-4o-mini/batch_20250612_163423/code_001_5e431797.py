"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: How can I implement a user feedback system for a course platform that mirrors the experiential learning approach described on Virtual5?
Generated: DETERMINISTIC_5e43179771f51600
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    course_id = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Feedback {self.id} - User: {self.user_id}, Course: {self.course_id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit user feedback for a course.
    Expects JSON data with user_id, course_id, rating, and optional comments.
    """
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('user_id', 'course_id', 'rating')):
        return jsonify({'error': 'Missing required fields'}), 400

    user_id = data['user_id']
    course_id = data['course_id']
    rating = data['rating']
    comments = data.get('comments', '')

    # Validate rating
    if not isinstance(rating, int) or not (1 <= rating <= 5):
        return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

    # Create a new feedback entry
    feedback = Feedback(user_id=user_id, course_id=course_id, rating=rating, comments=comments)

    try:
        db.session.add(feedback)
        db.session.commit()
        return jsonify({'message': 'Feedback submitted successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Feedback for this user and course already exists'}), 409
    except Exception as e:
        logging.error(f'Error submitting feedback: {e}')
        return jsonify({'error': 'An error occurred while submitting feedback'}), 500

@app.route('/feedback/<course_id>', methods=['GET'])
def get_feedback(course_id):
    """
    Endpoint to retrieve feedback for a specific course.
    Returns a list of feedback entries for the given course_id.
    """
    feedback_list = Feedback.query.filter_by(course_id=course_id).all()
    feedback_data = [{
        'user_id': feedback.user_id,
        'rating': feedback.rating,
        'comments': feedback.comments
    } for feedback in feedback_list]

    return jsonify(feedback_data), 200

if __name__ == '__main__':
    app.run(debug=True)
```
