"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rb.itsmeplabon.xyz
Prompt: Create an API endpoint for fetching user earnings and task statistics, similar to the data structure used on https://rb.itsmeplabon.xyz.
Generated: DETERMINISTIC_d1e0b88e577be6e7
Batch ID: 20250612_160246
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    earnings = db.Column(db.Float, default=0.0)
    tasks_completed = db.Column(db.Integer, default=0)

    def to_dict(self):
        """Convert User instance to dictionary format for JSON response."""
        return {
            'id': self.id,
            'username': self.username,
            'earnings': self.earnings,
            'tasks_completed': self.tasks_completed
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/user_statistics/<int:user_id>', methods=['GET'])
def get_user_statistics(user_id):
    """
    API endpoint to fetch user earnings and task statistics.

    Args:
        user_id (int): The ID of the user to fetch statistics for.

    Returns:
        JSON response containing user statistics or an error message.
    """
    try:
        user = User.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify(user.to_dict()), 200

    except SQLAlchemyError as e:
        # Log the error (could be enhanced with logging)
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
