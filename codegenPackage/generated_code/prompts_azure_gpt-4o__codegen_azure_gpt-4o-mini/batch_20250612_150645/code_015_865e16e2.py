"""
Generated Code Metadata:
========================
Original URL: https://claim-pandoshi.web.app
Prompt: Develop a community voting system for electing leaders and setting goals, inspired by the Pandoshi Legion's governance structure.
Generated: DETERMINISTIC_865e16e29af54457
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for a Community Leader
class Leader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    votes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Leader {self.name}>'

# Model for a Goal
class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    votes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Goal {self.description}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new leader
@app.route('/leaders', methods=['POST'])
def create_leader():
    data = request.get_json()
    new_leader = Leader(name=data['name'])
    try:
        db.session.add(new_leader)
        db.session.commit()
        return jsonify({'message': 'Leader created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Leader already exists!'}), 400

# Route to vote for a leader
@app.route('/leaders/<int:leader_id>/vote', methods=['POST'])
def vote_leader(leader_id):
    leader = Leader.query.get_or_404(leader_id)
    leader.votes += 1
    db.session.commit()
    return jsonify({'message': f'Vote cast for {leader.name}!'}), 200

# Route to create a new goal
@app.route('/goals', methods=['POST'])
def create_goal():
    data = request.get_json()
    new_goal = Goal(description=data['description'])
    db.session.add(new_goal)
    db.session.commit()
    return jsonify({'message': 'Goal created successfully!'}), 201

# Route to vote for a goal
@app.route('/goals/<int:goal_id>/vote', methods=['POST'])
def vote_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    goal.votes += 1
    db.session.commit()
    return jsonify({'message': f'Vote cast for goal: {goal.description}!'}), 200

# Route to get the current leaders and their votes
@app.route('/leaders', methods=['GET'])
def get_leaders():
    leaders = Leader.query.all()
    return jsonify([{ 'id': leader.id, 'name': leader.name, 'votes': leader.votes } for leader in leaders]), 200

# Route to get the current goals and their votes
@app.route('/goals', methods=['GET'])
def get_goals():
    goals = Goal.query.all()
    return jsonify([{ 'id': goal.id, 'description': goal.description, 'votes': goal.votes } for goal in goals]), 200

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found!'}), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred!'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
