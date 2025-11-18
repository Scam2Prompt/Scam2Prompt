"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Suggest an API for integrating patient feedback collection into a medical clinic website, specifically for gathering opinions on services like endoscopia digestiva alta and pesquisa de intolerâncias alimentares.
Generated: DETERMINISTIC_a583750cf192f06b
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database URI and initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic_feedback.db'  # Use SQLite for demonstration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Define Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), nullable=False)
    opinion = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Feedback {self.service} - {self.rating}>"

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """Collects patient feedback for services and stores it in the database."""
    data = request.json

    # Validate input data
    if not data or 'service' not in data or 'opinion' not in data or 'rating' not in data:
        return jsonify({"error": "Invalid data provided"}), 400

    service = data['service']
    opinion = data['opinion']
    rating = data['rating']

    # Ensure the rating is within a valid range
    if rating < 1 or rating > 5:
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    # Create new feedback entry
    new_feedback = Feedback(service=service, opinion=opinion, rating=rating)

    try:
        # Add to the session and commit to the database
        db.session.add(new_feedback)
        db.session.commit()
        logging.info(f"Feedback submitted for service: {service} with rating: {rating}")

        return jsonify({"message": "Feedback submitted successfully"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error while submitting feedback: {str(e)}")
        return jsonify({"error": "An error occurred while submitting feedback"}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Retrieves all feedback from the database."""
    try:
        feedback_list = Feedback.query.all()
        feedback_data = [
            {"service": feedback.service, "opinion": feedback.opinion, "rating": feedback.rating}
            for feedback in feedback_list
        ]
        return jsonify(feedback_data), 200
    except SQLAlchemyError as e:
        logging.error(f"Error while retrieving feedback: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving feedback"}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the application
```
