"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Create a feedback system for parents to communicate directly with school administrators via a mobile app, inspired by Him Saral's Communication/Feedback feature.
Generated: DETERMINISTIC_979bdec4d3b69354
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# feedback_system.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Feedback model to store parent feedback
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Feedback {self.id} from {self.parent_name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to submit feedback
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        # Extract data from request
        data = request.get_json()
        parent_name = data.get('parent_name')
        message = data.get('message')
        
        # Validate input
        if not parent_name or not message:
            return jsonify({"error": "Parent name and message are required!"}), 400
        
        # Create new feedback entry
        new_feedback = Feedback(parent_name=parent_name, message=message)
        db.session.add(new_feedback)
        db.session.commit()

        logging.info(f'Feedback submitted by {parent_name}: {message}')
        
        return jsonify({"message": "Feedback submitted successfully!"}), 201

    except Exception as e:
        logging.error(f'Error submitting feedback: {str(e)}')
        return jsonify({"error": "Failed to submit feedback. Please try again later."}), 500

# Route to retrieve all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    try:
        feedbacks = Feedback.query.all()
        feedback_list = [{"id": fb.id, "parent_name": fb.parent_name, "message": fb.message, "created_at": fb.created_at} for fb in feedbacks]

        return jsonify(feedback_list), 200

    except Exception as e:
        logging.error(f'Error retrieving feedback: {str(e)}')
        return jsonify({"error": "Failed to retrieve feedback."}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)
```

### Requirements:
- Install `Flask` and `Flask-SQLAlchemy` if not already installed:
```bash
pip install Flask Flask-SQLAlchemy
```

### Usage:
1. Run the script to start the server.
2. Submit feedback via a POST request to `/submit_feedback` with JSON body:
   ```json
   {
     "parent_name": "John Doe",
     "message": "Great school, very helpful!"
   }
   ```
3. Retrieve all feedback via a GET request to `/feedback`.
