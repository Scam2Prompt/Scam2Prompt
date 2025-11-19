"""
Generated Code Metadata:
========================
Original URL: https://neami.shop
Prompt: Illustrate how to implement a feedback system for a business collaboration platform, where users can rate their experiences and build a community of trust.
Generated: DETERMINISTIC_afbbcee1f5e92a57
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# feedback_system.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Feedback {self.id} - User: {self.user_id}, Rating: {self.rating}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback.
    Expects JSON with user_id, rating, and optional comment.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'user_id' not in data or 'rating' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    user_id = data['user_id']
    rating = data['rating']
    comment = data.get('comment', '')

    # Validate rating
    if rating < 1 or rating > 5:
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400

    # Create a new feedback entry
    new_feedback = Feedback(user_id=user_id, rating=rating, comment=comment)

    try:
        db.session.add(new_feedback)
        db.session.commit()
        return jsonify({'message': 'Feedback submitted successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to submit feedback'}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all feedback.
    Returns a list of feedback entries.
    """
    feedback_list = Feedback.query.all()
    return jsonify([{
        'id': feedback.id,
        'user_id': feedback.user_id,
        'rating': feedback.rating,
        'comment': feedback.comment
    } for feedback in feedback_list]), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following installed:
- Flask
- Flask-SQLAlchemy

You can install them using pip:
```bash
pip install Flask Flask-SQLAlchemy
```

### Running the Application
1. Save the code in a file named `feedback_system.py`.
2. Run the application using:
   ```bash
   python feedback_system.py
   ```
3. Use a tool like Postman or curl to interact with the API.
