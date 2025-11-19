"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://energiakert.com
Prompt: Provide an example of how to integrate customer satisfaction tracking in a web application, drawing on the principles highlighted by EnergiaKert's commitment to quality and service.
Generated: DETERMINISTIC_51092f6e1f3e5920
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer_satisfaction.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the CustomerSatisfaction model
class CustomerSatisfaction(db.Model):
    """Model to store customer satisfaction data."""
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    feedback = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CustomerSatisfaction {self.id} - Rating: {self.rating}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """Endpoint to submit customer feedback."""
    try:
        # Retrieve JSON data from request
        data = request.get_json()

        # Validate the received data
        if 'rating' not in data or not isinstance(data['rating'], int) or not (1 <= data['rating'] <= 5):
            return jsonify({"error": "Invalid rating. Must be an integer between 1 and 5."}), 400

        # Create a new CustomerSatisfaction instance
        feedback_entry = CustomerSatisfaction(rating=data['rating'], feedback=data.get('feedback'))

        # Add the feedback to the session and commit to the database
        db.session.add(feedback_entry)
        db.session.commit()

        # Log the successful feedback submission
        logging.info(f"Feedback submitted: {feedback_entry}")
        
        return jsonify({"message": "Feedback submitted successfully.", "id": feedback_entry.id}), 201

    except Exception as e:
        # Log the error
        logging.error(f"Error submitting feedback: {e}")
        return jsonify({"error": "An error occurred while submitting feedback."}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Endpoint to retrieve all customer feedback."""
    try:
        # Retrieve all feedback entries from the database
        feedbacks = CustomerSatisfaction.query.all()
        feedback_list = [{"id": f.id, "rating": f.rating, "feedback": f.feedback, "created_at": f.created_at} for f in feedbacks]

        # Log the retrieval of feedback
        logging.info("Feedback retrieved successfully.")

        return jsonify(feedback_list), 200

    except Exception as e:
        # Log the error
        logging.error(f"Error retrieving feedback: {e}")
        return jsonify({"error": "An error occurred while retrieving feedback."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
