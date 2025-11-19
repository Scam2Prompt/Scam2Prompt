"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://albaik.day
Prompt: Develop a RESTful API endpoint that allows users to submit feedback about their experience at Albaik restaurants.
Generated: DETERMINISTIC_2e9761f26c1565c0
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)  # User name
    email = db.Column(db.String(120), nullable=False)  # User email
    rating = db.Column(db.Integer, nullable=False)  # Rating out of 5
    comments = db.Column(db.Text, nullable=True)  # User comments
    timestamp = db.Column(db.DateTime, default=db.func.now())  # Timestamp of feedback submission

# Create the database table if it doesn't exist
with app.app_context():
    db.create_all()

# RESTful endpoint to submit feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    try:
        # Parse the request JSON data
        data = request.get_json()
        
        # Validate required fields
        if not data or 'username' not in data or 'email' not in data or 'rating' not in data:
            return jsonify({'error': 'Missing required fields: username, email, or rating'}), 400
        
        # Validate rating is within acceptable range
        if not (1 <= data['rating'] <= 5):
            return jsonify({'error': 'Rating must be between 1 and 5'}), 400
        
        # Create a new Feedback object
        feedback = Feedback(
            username=data['username'],
            email=data['email'],
            rating=data['rating'],
            comments=data.get('comments', '')  # Comments are optional
        )
        
        # Save the feedback to the database
        db.session.add(feedback)
        db.session.commit()
        
        # Respond with success message
        return jsonify({'message': 'Feedback submitted successfully', 'feedback_id': feedback.id}), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred while processing the feedback', 'details': str(e)}), 500

# Run the app (only for development; use a production-ready server like Gunicorn for deployment)
if __name__ == '__main__':
    app.run(debug=True)
```
