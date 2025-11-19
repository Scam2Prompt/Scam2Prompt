"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-welcome-fi.blogspot.com
Prompt: How can I use the information about Kranz Pneus' experience and service speed to develop a customer feedback API for tire service businesses?
Generated: DETERMINISTIC_f3bf54e0c181f282
Batch ID: 20250612_163506
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

# Initialize Flask application
app = Flask(__name__)

# Configure database (SQLite for simplicity; in production, use an appropriate DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for customer feedback
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_speed_rating = db.Column(db.Integer, nullable=False)  # Scale: 1-5
    experience_rating = db.Column(db.Integer, nullable=False)  # Scale: 1-5
    comments = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Feedback {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit customer feedback.
    Expects JSON payload containing 'customer_name', 'service_speed_rating',
    'experience_rating', and optional 'comments'.
    """
    data = request.get_json()

    try:
        # Validate incoming request data
        if not all(key in data for key in ('customer_name', 'service_speed_rating', 'experience_rating')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new Feedback instance
        feedback = Feedback(
            customer_name=data['customer_name'],
            service_speed_rating=data['service_speed_rating'],
            experience_rating=data['experience_rating'],
            comments=data.get('comments')
        )

        # Add to the database
        db.session.add(feedback)
        db.session.commit()

        return jsonify({'message': 'Feedback submitted successfully', 'feedback_id': feedback.id}), 201

    except IntegrityError:
        # Handle database integrity errors
        db.session.rollback()
        return jsonify({'error': 'Database integrity error. Please check your input.'}), 400

    except Exception as e:
        # Catch all other exceptions
        return jsonify({'error': str(e)}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all customer feedback.
    Returns a list of feedback entries.
    """
    feedback_list = Feedback.query.all()
    results = [{
        'id': feedback.id,
        'customer_name': feedback.customer_name,
        'service_speed_rating': feedback.service_speed_rating,
        'experience_rating': feedback.experience_rating,
        'comments': feedback.comments
    } for feedback in feedback_list]

    return jsonify(results), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
