"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin100-maxair.com
Prompt: Explain how Bitcoin +100 Maxair facilitates connections between learners and finance experts, and suggest an API for managing these interactions.
Generated: DETERMINISTIC_ba2bdf50f80d2daa
Batch ID: 20250612_160129
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
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maxair.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Learner model
class Learner(db.Model):
    __tablename__ = 'learners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Learner {self.name}>'

# Define the FinanceExpert model
class FinanceExpert(db.Model):
    __tablename__ = 'finance_experts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    expertise = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<FinanceExpert {self.name}>'

# Define the Interaction model to manage connections
class Interaction(db.Model):
    __tablename__ = 'interactions'
    id = db.Column(db.Integer, primary_key=True)
    learner_id = db.Column(db.Integer, db.ForeignKey('learners.id'), nullable=False)
    expert_id = db.Column(db.Integer, db.ForeignKey('finance_experts.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    learner = db.relationship('Learner', backref='interactions')
    expert = db.relationship('FinanceExpert', backref='interactions')

    def __repr__(self):
        return f'<Interaction {self.id}>'

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to add a learner
@app.route('/learners', methods=['POST'])
def add_learner():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        raise BadRequest('Missing name or email.')

    new_learner = Learner(name=data['name'], email=data['email'])
    db.session.add(new_learner)
    db.session.commit()
    return jsonify({'id': new_learner.id}), 201

# API endpoint to add a finance expert
@app.route('/finance_experts', methods=['POST'])
def add_finance_expert():
    data = request.get_json()
    if not data or 'name' not in data or 'expertise' not in data:
        raise BadRequest('Missing name or expertise.')

    new_expert = FinanceExpert(name=data['name'], expertise=data['expertise'])
    db.session.add(new_expert)
    db.session.commit()
    return jsonify({'id': new_expert.id}), 201

# API endpoint to create an interaction
@app.route('/interactions', methods=['POST'])
def create_interaction():
    data = request.get_json()
    if not data or 'learner_id' not in data or 'expert_id' not in data:
        raise BadRequest('Missing learner_id or expert_id.')

    interaction = Interaction(learner_id=data['learner_id'], expert_id=data['expert_id'])
    db.session.add(interaction)
    db.session.commit()
    return jsonify({'id': interaction.id}), 201

# API endpoint to get all interactions
@app.route('/interactions', methods=['GET'])
def get_interactions():
    interactions = Interaction.query.all()
    return jsonify([{'id': i.id, 'learner_id': i.learner_id, 'expert_id': i.expert_id, 'timestamp': i.timestamp} for i in interactions])

# Error handling for NotFound
@app.errorhandler(NotFound)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

# Error handling for BadRequest
@app.errorhandler(BadRequest)
def bad_request(e):
    return jsonify(error=str(e)), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
