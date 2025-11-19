"""
Generated Code Metadata:
========================
Original URL: https://energiakert.com
Prompt: Provide an example of how to integrate customer satisfaction tracking in a web application, drawing on the principles highlighted by EnergiaKert's commitment to quality and service.
Generated: DETERMINISTIC_51092f6e1f3e5920
Batch ID: 20250612_155446
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer_satisfaction.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the CustomerSatisfaction model
class CustomerSatisfaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    feedback = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CustomerSatisfaction {self.id}: Rating {self.rating}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to submit customer satisfaction feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if 'rating' not in data or not (1 <= data['rating'] <= 5):
            return jsonify({'error': 'Rating must be an integer between 1 and 5.'}), 400

        # Create a new CustomerSatisfaction record
        feedback = CustomerSatisfaction(
            rating=data['rating'],
            feedback=data.get('feedback')
        )

        # Add the record to the database
        db.session.add(feedback)
        db.session.commit()

        # Log the successful submission
        logging.info(f'Feedback submitted: {feedback}')

        return jsonify({'message': 'Feedback submitted successfully!'}), 201

    except Exception as e:
        # Log the error
        logging.error(f'Error submitting feedback: {e}')
        return jsonify({'error': 'An error occurred while submitting feedback.'}), 500

# Route to retrieve all feedback
@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    try:
        # Query all feedback records
        feedback_list = CustomerSatisfaction.query.all()
        feedback_data = [
            {
                'id': feedback.id,
                'rating': feedback.rating,
                'feedback': feedback.feedback,
                'created_at': feedback.created_at.isoformat()
            } for feedback in feedback_list
        ]

        return jsonify(feedback_data), 200

    except Exception as e:
        # Log the error
        logging.error(f'Error retrieving feedback: {e}')
        return jsonify({'error': 'An error occurred while retrieving feedback.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
