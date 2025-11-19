"""
Generated Code Metadata:
========================
Original URL: https://libertyaid.co
Prompt: Build a REST API that provides information on Medicare Supplement Insurance, including worldwide coverage and maximum out-of-pocket costs.
Generated: DETERMINISTIC_e6459f47590ef6d6
Batch ID: 20250612_154942
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicare_supplement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Medicare Supplement Insurance model
class MedicareSupplement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String(100), nullable=False)
    worldwide_coverage = db.Column(db.Boolean, nullable=False)
    max_out_of_pocket = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'plan_name': self.plan_name,
            'worldwide_coverage': self.worldwide_coverage,
            'max_out_of_pocket': self.max_out_of_pocket
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/medicare_supplement', methods=['GET'])
def get_plans():
    """Retrieve all Medicare Supplement Insurance plans."""
    try:
        plans = MedicareSupplement.query.all()
        return jsonify([plan.to_dict() for plan in plans]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/medicare_supplement/<int:plan_id>', methods=['GET'])
def get_plan(plan_id):
    """Retrieve a specific Medicare Supplement Insurance plan by ID."""
    try:
        plan = MedicareSupplement.query.get_or_404(plan_id)
        return jsonify(plan.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/medicare_supplement', methods=['POST'])
def add_plan():
    """Add a new Medicare Supplement Insurance plan."""
    data = request.get_json()
    if not data or 'plan_name' not in data or 'worldwide_coverage' not in data or 'max_out_of_pocket' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_plan = MedicareSupplement(
        plan_name=data['plan_name'],
        worldwide_coverage=data['worldwide_coverage'],
        max_out_of_pocket=data['max_out_of_pocket']
    )

    try:
        db.session.add(new_plan)
        db.session.commit()
        return jsonify(new_plan.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/medicare_supplement/<int:plan_id>', methods=['PUT'])
def update_plan(plan_id):
    """Update an existing Medicare Supplement Insurance plan."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        plan = MedicareSupplement.query.get_or_404(plan_id)
        plan.plan_name = data.get('plan_name', plan.plan_name)
        plan.worldwide_coverage = data.get('worldwide_coverage', plan.worldwide_coverage)
        plan.max_out_of_pocket = data.get('max_out_of_pocket', plan.max_out_of_pocket)

        db.session.commit()
        return jsonify(plan.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/medicare_supplement/<int:plan_id>', methods=['DELETE'])
def delete_plan(plan_id):
    """Delete a Medicare Supplement Insurance plan."""
    try:
        plan = MedicareSupplement.query.get_or_404(plan_id)
        db.session.delete(plan)
        db.session.commit()
        return jsonify({'message': 'Plan deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
