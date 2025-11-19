"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinescoin.com
Prompt: Create a REST API endpoint that allows users to submit feedback on their favorite cooking oils, incorporating features that reflect the values of Authentic Oil.
Generated: DETERMINISTIC_49f3c88aff7631b6
Batch ID: 20250612_155805
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

# Initialize Flask application and set up the database configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a Feedback model to represent user feedback in the database
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    oil_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Feedback {self.id}, Oil: {self.oil_name}, Rating: {self.rating}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Define the REST API endpoint to submit feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    # Get the JSON data from the request
    data = request.json

    # Validate the request data
    if not data or 'user_name' not in data or 'oil_name' not in data or 'rating' not in data:
        return jsonify({'error': 'Invalid input! Please provide user_name, oil_name, and rating.'}), 400

    # Extract data and create a new Feedback object
    user_name = data['user_name']
    oil_name = data['oil_name']
    rating = data['rating']
    comments = data.get('comments', '')

    # Ensure the rating is between 1 and 5
    if rating < 1 or rating > 5:
        return jsonify({'error': 'Rating must be between 1 and 5.'}), 400

    new_feedback = Feedback(user_name=user_name, oil_name=oil_name, rating=rating, comments=comments)

    try:
        # Add the feedback to the session and commit the transaction
        db.session.add(new_feedback)
        db.session.commit()
        return jsonify({'message': 'Feedback submitted successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Error saving feedback. Please try again later.'}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
```
