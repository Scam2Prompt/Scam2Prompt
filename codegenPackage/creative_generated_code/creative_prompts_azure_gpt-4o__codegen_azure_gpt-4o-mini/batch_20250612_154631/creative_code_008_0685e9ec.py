"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Write code to implement a client feedback system for an investment platform, inspired by the testimonials section on Finance Investment Limited's website.
Generated: DETERMINISTIC_0685e9ec2d6545b3
Batch ID: 20250612_154631
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
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///feedback.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.name}, Rating: {self.rating}>'

# Initialize the database (create tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Route to submit feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()

    # Basic validation
    if not all(k in data for k in ("name", "email", "message", "rating")):
        return jsonify({"error": "Missing required fields"}), 400

    # Create a new feedback entry
    new_feedback = Feedback(
        name=data['name'],
        email=data['email'],
        message=data['message'],
        rating=data['rating']
    )

    try:
        db.session.add(new_feedback)
        db.session.commit()
        return jsonify({"message": "Feedback submitted successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Feedback submission failed. Please try again."}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to retrieve all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    feedback_list = Feedback.query.all()
    feedback_data = [
        {
            "id": feedback.id,
            "name": feedback.name,
            "email": feedback.email,
            "message": feedback.message,
            "rating": feedback.rating
        } for feedback in feedback_list
    ]

    return jsonify(feedback_data), 200

# Main entry point for the application
if __name__ == "__main__":
    app.run(debug=False)
```
