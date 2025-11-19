"""
Generated Code Metadata:
========================
Original URL: https://owy-wtf.pages.dev
Prompt: "Develop a feedback system for a memecoin project's website, incorporating user input for future development."
Generated: DETERMINISTIC_5200efe01fe21f16
Batch ID: 20250622_205404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.username}: {self.message}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit user feedback.
    Expects JSON data with 'username' and 'message'.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'username' not in data or 'message' not in data:
        return jsonify({'error': 'Invalid input. Please provide username and message.'}), 400

    username = data['username']
    message = data['message']

    # Create a new feedback entry
    new_feedback = Feedback(username=username, message=message)

    try:
        db.session.add(new_feedback)
        db.session.commit()
        return jsonify({'message': 'Feedback submitted successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to submit feedback. Please try again.'}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all feedback entries.
    Returns a JSON list of feedback.
    """
    feedback_list = Feedback.query.all()
    feedback_data = [{'username': feedback.username, 'message': feedback.message} for feedback in feedback_list]
    return jsonify(feedback_data), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
