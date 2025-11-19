"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neami.shop
Prompt: Illustrate how to implement a feedback system for a business collaboration platform, where users can rate their experiences and build a community of trust.
Generated: DETERMINISTIC_afbbcee1f5e92a57
Batch ID: 20250612_155159
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    """Model representing user feedback."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Rating from 1 to 5
    comment = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Feedback {self.id}: User {self.user_id}, Rating {self.rating}>'

@app.before_first_request
def create_tables():
    """Create the database tables before the first request."""
    db.create_all()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """Submit user feedback.

    Returns:
        JSON response with feedback submission result.
    """
    data = request.get_json()

    # Validate input data
    user_id = data.get('user_id')
    rating = data.get('rating')
    comment = data.get('comment')

    if not user_id or not isinstance(rating, int) or not (1 <= rating <= 5):
        return jsonify({"error": "Invalid input data"}), 400

    feedback = Feedback(user_id=user_id, rating=rating, comment=comment)

    try:
        db.session.add(feedback)
        db.session.commit()
        return jsonify({"message": "Feedback submitted successfully"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Error submitting feedback"}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Get all submitted feedback.

    Returns:
        JSON containing all feedback entries.
    """
    feedback_list = Feedback.query.all()
    feedback_data = [{
        "id": feedback.id,
        "user_id": feedback.user_id,
        "rating": feedback.rating,
        "comment": feedback.comment
    } for feedback in feedback_list]

    return jsonify(feedback_data), 200

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages using:
```bash
pip install Flask Flask-SQLAlchemy
```

To initialize the database, run the application, and send a `POST` request to `/feedback` to submit feedback, and a `GET` request to `/feedback` to retrieve all feedback entries.
