"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-206--nervous-kare-6f3c45.netlify.app
Prompt: Generate a RESTful API endpoint in Python to handle user requests for refuse and recycling collection schedules, assuming a municipal database schema.
Generated: DETERMINISTIC_aab5d1f94f4a86d1
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///municipal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the UserSchedule model
class UserSchedule(db.Model):
    __tablename__ = 'user_schedules'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    refuse_collection = db.Column(db.String(50), nullable=False)
    recycling_collection = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the UserSchedule object to a dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'refuse_collection': self.refuse_collection,
            'recycling_collection': self.recycling_collection
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/schedules/<int:user_id>', methods=['GET'])
def get_collection_schedule(user_id):
    """
    Retrieve the refuse and recycling collection schedule for a specific user.

    Args:
        user_id (int): The ID of the user for whom to retrieve the schedule.

    Returns:
        JSON response containing the collection schedule or an error message.
    """
    try:
        schedule = UserSchedule.query.filter_by(user_id=user_id).first()
        if schedule:
            return jsonify(schedule.to_dict()), 200
        else:
            return jsonify({'error': 'Schedule not found for the given user ID.'}), 404
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/schedules', methods=['POST'])
def create_collection_schedule():
    """
    Create a new refuse and recycling collection schedule for a user.

    Returns:
        JSON response containing the created schedule or an error message.
    """
    data = request.get_json()
    
    if not data or 'user_id' not in data or 'refuse_collection' not in data or 'recycling_collection' not in data:
        return jsonify({'error': 'Invalid input data.'}), 400

    new_schedule = UserSchedule(
        user_id=data['user_id'],
        refuse_collection=data['refuse_collection'],
        recycling_collection=data['recycling_collection']
    )

    try:
        db.session.add(new_schedule)
        db.session.commit()
        return jsonify(new_schedule.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
