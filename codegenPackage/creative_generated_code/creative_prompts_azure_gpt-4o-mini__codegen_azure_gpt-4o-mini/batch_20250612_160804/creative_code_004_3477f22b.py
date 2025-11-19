"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pufferr.pages.dev
Prompt: How can I create a leaderboard feature for a community rewards program, based on the concepts presented in the Puffer website?
Generated: DETERMINISTIC_3477f22b3bb22910
Batch ID: 20250612_160804
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

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a User model for the leaderboard
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, default=0)

    def to_dict(self):
        """Convert User object to dictionary format for easy JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'points': self.points
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST'])
def add_user():
    """Add a new user to the leaderboard."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'Name is required'}), 400
    
    new_user = User(name=data['name'])
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database Error', 'message': str(e)}), 500

@app.route('/users/<int:user_id>/points', methods=['PUT'])
def update_points(user_id):
    """Update points for an existing user."""
    data = request.get_json()
    if not data or 'points' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'Points are required'}), 400
    
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'Not Found', 'message': 'User not found'}), 404

    user.points += data['points']

    try:
        db.session.commit()
        return jsonify(user.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database Error', 'message': str(e)}), 500

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Retrieve the leaderboard sorted by points in descending order."""
    try:
        users = User.query.order_by(User.points.desc()).all()
        return jsonify([user.to_dict() for user in users]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database Error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
