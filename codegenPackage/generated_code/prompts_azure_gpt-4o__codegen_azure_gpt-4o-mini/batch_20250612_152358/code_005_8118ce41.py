"""
Generated Code Metadata:
========================
Original URL: https://startupsadvisory.com
Prompt: Write code to design a restaurant feedback form that ties into reputation management systems, using the insights provided by StartUp Advisory.
Generated: DETERMINISTIC_8118ce41ced5b1c4
Batch ID: 20250612_152358
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
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Feedback {self.id} - {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to submit feedback
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ('name', 'email', 'rating')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new feedback entry
        feedback = Feedback(
            name=data['name'],
            email=data['email'],
            rating=data['rating'],
            comments=data.get('comments', '')
        )

        # Add feedback to the database
        db.session.add(feedback)
        db.session.commit()

        logging.info(f'Feedback submitted: {feedback}')
        return jsonify({'message': 'Feedback submitted successfully!'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Feedback submission failed due to integrity error.'}), 500
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        return jsonify({'error': 'An unexpected error occurred.'}), 500

# Route to retrieve all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    try:
        feedback_list = Feedback.query.all()
        return jsonify([{
            'id': feedback.id,
            'name': feedback.name,
            'email': feedback.email,
            'rating': feedback.rating,
            'comments': feedback.comments
        } for feedback in feedback_list]), 200
    except Exception as e:
        logging.error(f'Error occurred while retrieving feedback: {e}')
        return jsonify({'error': 'An unexpected error occurred.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
