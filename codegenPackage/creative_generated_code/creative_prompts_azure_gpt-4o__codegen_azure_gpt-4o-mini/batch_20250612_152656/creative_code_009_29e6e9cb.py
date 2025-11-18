"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smog-tokens-en.pages.dev
Prompt: Develop a roadmap tracker for the $SMOG token project, displaying milestones such as airdrop research, Ethereum LP & staking, and multichain token expansion.
Generated: DETERMINISTIC_29e6e9cbe7083a02
Batch ID: 20250612_152656
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roadmap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Milestone model for the database
class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S')
        }

# Create the database
with app.app_context():
    db.create_all()

# Route to get all milestones
@app.route('/milestones', methods=['GET'])
def get_milestones():
    """Fetch all roadmap milestones."""
    try:
        milestones = Milestone.query.all()
        return jsonify([milestone.to_dict() for milestone in milestones]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new milestone
@app.route('/milestones', methods=['POST'])
def add_milestone():
    """Add a new milestone to the roadmap."""
    data = request.get_json()
    
    # Validate request data
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({'error': 'Title and description are required.'}), 400
    
    try:
        new_milestone = Milestone(title=data['title'], description=data['description'])
        db.session.add(new_milestone)
        db.session.commit()
        return jsonify(new_milestone.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to update an existing milestone
@app.route('/milestones/<int:id>', methods=['PUT'])
def update_milestone(id):
    """Update an existing milestone."""
    data = request.get_json()
    
    # Validate request data
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({'error': 'Title and description are required.'}), 400

    try:
        milestone = Milestone.query.get_or_404(id)
        milestone.title = data['title']
        milestone.description = data['description']
        db.session.commit()
        return jsonify(milestone.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to delete a milestone
@app.route('/milestones/<int:id>', methods=['DELETE'])
def delete_milestone(id):
    """Delete a milestone from the roadmap."""
    try:
        milestone = Milestone.query.get_or_404(id)
        db.session.delete(milestone)
        db.session.commit()
        return jsonify({'message': 'Milestone deleted successfully.'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Main entry point to run the app
if __name__ == '__main__':
    app.run(debug=True)
```
