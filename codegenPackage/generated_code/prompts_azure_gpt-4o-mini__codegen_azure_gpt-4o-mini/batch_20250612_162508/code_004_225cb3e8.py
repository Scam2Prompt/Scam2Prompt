"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Design a mobile app feature that encourages athletes to set personal goals in both sports and life, reflecting the mentorship philosophy of Team DGA.
Generated: DETERMINISTIC_225cb3e80fd5403d
Batch ID: 20250612_162508
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///goals.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Goal model
class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'sports' or 'life'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Goal {self.id}: {self.description}>'


# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()


# Route to create a new goal
@app.route('/goals', methods=['POST'])
def create_goal():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        description = data.get('description')
        category = data.get('category')

        # Validate input
        if not user_id or not description or category not in ['sports', 'life']:
            return jsonify({'error': 'Invalid input'}), 400

        # Create a new goal
        new_goal = Goal(user_id=user_id, description=description, category=category)
        db.session.add(new_goal)
        db.session.commit()

        return jsonify({'message': 'Goal created successfully', 'goal_id': new_goal.id}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route to retrieve goals for a user
@app.route('/goals/<int:user_id>', methods=['GET'])
def get_goals(user_id):
    try:
        goals = Goal.query.filter_by(user_id=user_id).all()
        return jsonify([{'id': goal.id, 'description': goal.description, 'category': goal.category, 'created_at': goal.created_at} for goal in goals]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route to update a goal
@app.route('/goals/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    try:
        data = request.get_json()
        goal = Goal.query.get_or_404(goal_id)

        # Update goal attributes
        if 'description' in data:
            goal.description = data['description']
        if 'category' in data and data['category'] in ['sports', 'life']:
            goal.category = data['category']

        db.session.commit()
        return jsonify({'message': 'Goal updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route to delete a goal
@app.route('/goals/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    try:
        goal = Goal.query.get_or_404(goal_id)
        db.session.delete(goal)
        db.session.commit()
        return jsonify({'message': 'Goal deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
