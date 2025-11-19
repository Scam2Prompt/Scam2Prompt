"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes-missions.pages.dev
Prompt: How do I implement a feature to display mission status and rewards in a Nyan Heroes application?
Generated: DETERMINISTIC_8d5f7886b12b7bc1
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nyan_heroes.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Mission model
class Mission(db.Model):
    """Model representing a mission in the Nyan Heroes application."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'active', 'completed', 'failed'
    rewards = db.Column(db.String(200), nullable=True)  # Rewards as a comma-separated string

    def to_dict(self):
        """Convert Mission object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'rewards': self.rewards.split(',') if self.rewards else []
        }

# Endpoint to retrieve mission status and rewards
@app.route('/missions/<int:mission_id>', methods=['GET'])
def get_mission_status(mission_id):
    """Retrieve the status and rewards of a specific mission by ID."""
    try:
        mission = Mission.query.get(mission_id)
        if mission is None:
            return jsonify({'error': 'Mission not found'}), 404
        return jsonify(mission.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error (logging setup not shown here)
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

# Initialize the database and create some sample missions
@app.before_first_request
def create_tables():
    """Create database tables and seed with sample data if empty."""
    db.create_all()
    if Mission.query.count() == 0:
        sample_missions = [
            Mission(name='Collect Nyan Coins', status='active', rewards='100 coins,5 gems'),
            Mission(name='Defeat the Dark Nyan', status='completed', rewards='500 coins,1 rare item'),
            Mission(name='Rescue the Lost Kittens', status='failed', rewards=None)
        ]
        db.session.bulk_save_objects(sample_missions)
        db.session.commit()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production use
```
