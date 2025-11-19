"""
Generated Code Metadata:
========================
Original URL: https://mommymilestones.com
Prompt: Recommend a platform or tool for mothers to track and celebrate their daily accomplishments, inspired by the concept of "Mommaversary" and "Mommy Milestones".
Generated: DETERMINISTIC_d809e66276d6df87
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mommaversary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Milestone model
class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Milestone {self.description}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to add a new milestone
@app.route('/milestones', methods=['POST'])
def add_milestone():
    try:
        data = request.get_json()
        new_milestone = Milestone(description=data['description'])
        db.session.add(new_milestone)
        db.session.commit()
        return jsonify({'message': 'Milestone added!', 'milestone': new_milestone.description}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all milestones
@app.route('/milestones', methods=['GET'])
def get_milestones():
    try:
        milestones = Milestone.query.all()
        return jsonify([{'id': m.id, 'description': m.description, 'date': m.date} for m in milestones]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a milestone
@app.route('/milestones/<int:id>', methods=['DELETE'])
def delete_milestone(id):
    try:
        milestone = Milestone.query.get_or_404(id)
        db.session.delete(milestone)
        db.session.commit()
        return jsonify({'message': 'Milestone deleted!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
