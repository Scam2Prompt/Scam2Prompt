"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamdga.com
Prompt: Design a mobile app feature that encourages athletes to set personal goals in both sports and life, reflecting the mentorship philosophy of Team DGA.
Generated: DETERMINISTIC_225cb3e80fd5403d
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///goals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Goal model
class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'sports' or 'life'
    target_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Goal {self.description}>'


# Route to create a new goal
@app.route('/goals', methods=['POST'])
def create_goal():
    try:
        data = request.get_json()
        if not data or 'athlete_id' not in data or 'description' not in data or 'category' not in data:
            return jsonify({'error': 'Bad Request', 'message': 'Missing required fields'}), 400
        
        # Create a new goal instance
        new_goal = Goal(
            athlete_id=data['athlete_id'],
            description=data['description'],
            category=data['category'],
            target_date=datetime.strptime(data['target_date'], '%Y-%m-%d') if 'target_date' in data else None
        )
        
        db.session.add(new_goal)
        db.session.commit()
        
        return jsonify({'message': 'Goal created successfully', 'goal': {'id': new_goal.id, 'description': new_goal.description}}), 201

    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500


# Route to retrieve all goals for an athlete
@app.route('/goals/<int:athlete_id>', methods=['GET'])
def get_goals(athlete_id):
    try:
        goals = Goal.query.filter_by(athlete_id=athlete_id).all()
        return jsonify({'goals': [{'id': goal.id, 'description': goal.description, 'category': goal.category, 'target_date': goal.target_date} for goal in goals]}), 200

    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500


# Route to update a goal
@app.route('/goals/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    try:
        data = request.get_json()
        goal = Goal.query.get_or_404(goal_id)

        if 'description' in data:
            goal.description = data['description']
        if 'category' in data:
            goal.category = data['category']
        if 'target_date' in data:
            goal.target_date = datetime.strptime(data['target_date'], '%Y-%m-%d')

        db.session.commit()

        return jsonify({'message': 'Goal updated successfully', 'goal': {'id': goal.id, 'description': goal.description}}), 200

    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500


# Route to delete a goal
@app.route('/goals/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    try:
        goal = Goal.query.get_or_404(goal_id)
        db.session.delete(goal)
        db.session.commit()
        return jsonify({'message': 'Goal deleted successfully'}), 204

    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500


# Initialize the database before starting the app
@app.before_first_request
def create_tables():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
