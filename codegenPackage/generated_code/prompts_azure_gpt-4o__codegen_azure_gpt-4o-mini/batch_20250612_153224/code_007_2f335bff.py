"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Provide sample code for integrating a customer feedback system into a computer repair service website, inspired by Geeks On Repair’s emphasis on customer satisfaction.
Generated: DETERMINISTIC_2f335bff464fee1d
Batch ID: 20250612_153224
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
from datetime import datetime
import logging

# Initialize Flask application
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
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Feedback {self.id} from {self.customer_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to submit feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if not data or not all(key in data for key in ('customer_name', 'email', 'message')):
            return jsonify({'error': 'Invalid input data'}), 400

        # Create a new Feedback instance
        feedback = Feedback(
            customer_name=data['customer_name'],
            email=data['email'],
            message=data['message']
        )

        # Add feedback to the database
        db.session.add(feedback)
        db.session.commit()

        logging.info(f'Feedback submitted by {feedback.customer_name}')
        return jsonify({'message': 'Feedback submitted successfully!'}), 201

    except Exception as e:
        logging.error(f'Error submitting feedback: {e}')
        return jsonify({'error': 'An error occurred while submitting feedback'}), 500

# Route to get all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    try:
        # Retrieve all feedback from the database
        feedback_list = Feedback.query.all()
        feedback_data = [
            {
                'id': feedback.id,
                'customer_name': feedback.customer_name,
                'email': feedback.email,
                'message': feedback.message,
                'created_at': feedback.created_at.isoformat()
            } for feedback in feedback_list
        ]

        return jsonify(feedback_data), 200

    except Exception as e:
        logging.error(f'Error retrieving feedback: {e}')
        return jsonify({'error': 'An error occurred while retrieving feedback'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
