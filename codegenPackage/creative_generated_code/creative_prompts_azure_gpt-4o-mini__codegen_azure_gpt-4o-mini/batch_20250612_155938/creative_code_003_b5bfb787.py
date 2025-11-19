"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmynetwork.org
Prompt: Create a code snippet that demonstrates how to integrate user ratings for web content within the Stumble! application framework.
Generated: DETERMINISTIC_b5bfb787c47f84cc
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Rating model
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    content_id = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Rating {self.user_id} for {self.content_id}: {self.score}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/rate', methods=['POST'])
def rate_content():
    """
    Endpoint to submit a user rating for content.
    Expects a JSON body with user_id, content_id, and score.
    """
    # Parse the request data
    data = request.get_json()

    # Validate request data
    if not data or not all(key in data for key in ('user_id', 'content_id', 'score')):
        abort(400, description="Missing user_id, content_id, or score in the request")

    user_id = data['user_id']
    content_id = data['content_id']
    score = data['score']

    # Validate score range
    if not (1 <= score <= 5):
        abort(400, description="Score must be between 1 and 5")

    # Create a new rating instance
    new_rating = Rating(user_id=user_id, content_id=content_id, score=score)

    try:
        # Add the new rating to the database
        db.session.add(new_rating)
        db.session.commit()
        return jsonify({'message': 'Rating submitted successfully!'}), 201
    except Exception as e:
        # Rollback in case of error
        db.session.rollback()
        abort(500, description=f"An error occurred while submitting the rating: {str(e)}")

@app.route('/ratings/<content_id>', methods=['GET'])
def get_ratings(content_id):
    """
    Endpoint to retrieve all ratings for a specific content ID.
    Returns a list of ratings in JSON format.
    """
    try:
        ratings = Rating.query.filter_by(content_id=content_id).all()
        return jsonify([{'user_id': rating.user_id, 'score': rating.score} for rating in ratings]), 200
    except Exception as e:
        abort(500, description=f"An error occurred while retrieving ratings: {str(e)}")

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
