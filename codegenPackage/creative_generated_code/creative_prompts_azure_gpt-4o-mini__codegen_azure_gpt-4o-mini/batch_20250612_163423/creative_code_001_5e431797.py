"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: How can I implement a user feedback system for a course platform that mirrors the experiential learning approach described on Virtual5?
Generated: DETERMINISTIC_5e43179771f51600
Batch ID: 20250612_163423
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
from flask_migrate import Migrate
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///feedback.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Feedback model
class Feedback(db.Model):
    __tablename__ = 'feedback'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Feedback {self.id} for Course {self.course_id}>'

# Route to submit feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    try:
        data = request.json
        
        # Validate input data
        if not all(key in data for key in ('user_id', 'course_id', 'rating')):
            return jsonify({"error": "Missing data."}), 400
        
        # Create a new feedback record
        new_feedback = Feedback(
            user_id=data['user_id'],
            course_id=data['course_id'],
            rating=data['rating'],
            comment=data.get('comment')
        )
        
        # Add to the session and commit to the database
        db.session.add(new_feedback)
        db.session.commit()
        
        return jsonify({"message": "Feedback submitted successfully."}), 201

    except Exception as e:
        # Rollback in case of error and return error message
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to retrieve feedback for a course
@app.route('/feedback/<int:course_id>', methods=['GET'])
def get_feedback(course_id):
    try:
        # Query feedback records for the specified course
        feedback_records = Feedback.query.filter_by(course_id=course_id).all()
        
        # Serialize feedback records
        results = [{"id": feedback.id, "user_id": feedback.user_id, 
                    "rating": feedback.rating, "comment": feedback.comment, 
                    "created_at": feedback.created_at} for feedback in feedback_records]
        
        return jsonify(results), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point of the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables for the model
    app.run(debug=True)  # Note: Set debug=False in production
```

### Notes:
- This code sets up a simple user feedback system using Flask and SQLAlchemy.
- It includes routes to submit feedback and retrieve feedback for a specific course.
- Error handling is incorporated to manage missing data and exceptions.
- Replace the database URI with your production database settings.
- Ensure the environment variable `DATABASE_URL` is set correctly for deployment.
