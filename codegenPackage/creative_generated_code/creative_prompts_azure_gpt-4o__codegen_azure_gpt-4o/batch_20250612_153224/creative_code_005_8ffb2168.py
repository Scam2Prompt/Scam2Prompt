"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Recommend an API for tracking and managing annual operational plans, and provide example code for implementing a system similar to the "الخطة التشغيلية" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_8ffb21680a584e3f
Batch ID: 20250612_153224
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

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///operational_plans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Operational Plans
class OperationalPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Unique ID for each plan
    year = db.Column(db.Integer, nullable=False)  # Planning year
    title = db.Column(db.String(255), nullable=False)  # Title of the plan
    objectives = db.Column(db.Text, nullable=False)  # Objectives of the plan
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Plan creation timestamp

    def to_dict(self):
        """Convert model instance to a dictionary for JSON responses."""
        return {
            'id': self.id,
            'year': self.year,
            'title': self.title,
            'objectives': self.objectives,
            'created_at': self.created_at
        }

# Endpoint to add a new operational plan
@app.route('/plans', methods=['POST'])
def add_plan():
    """Add a new operational plan."""
    try:
        data = request.json  # Parse the incoming JSON data
        # Validate required fields
        if not all(field in data for field in ('year', 'title', 'objectives')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new plan instance
        new_plan = OperationalPlan(
            year=data['year'],
            title=data['title'],
            objectives=data['objectives']
        )

        # Save the plan to the database
        db.session.add(new_plan)
        db.session.commit()

        return jsonify({'message': 'Operational plan added successfully', 'plan': new_plan.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint to fetch all operational plans
@app.route('/plans', methods=['GET'])
def get_plans():
    """Fetch all operational plans."""
    try:
        plans = OperationalPlan.query.all()
        return jsonify({'plans': [plan.to_dict() for plan in plans]}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint to fetch a specific operational plan by ID
@app.route('/plans/<int:plan_id>', methods=['GET'])
def get_plan(plan_id):
    """Fetch a specific operational plan by ID."""
    try:
        plan = OperationalPlan.query.get(plan_id)
        if not plan:
            return jsonify({'error': 'Operational plan not found'}), 404

        return jsonify({'plan': plan.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint to update an operational plan
@app.route('/plans/<int:plan_id>', methods=['PUT'])
def update_plan(plan_id):
    """Update an existing operational plan."""
    try:
        plan = OperationalPlan.query.get(plan_id)
        if not plan:
            return jsonify({'error': 'Operational plan not found'}), 404

        data = request.json  # Parse the incoming JSON data
        # Update fields if present in the request
        if 'year' in data:
            plan.year = data['year']
        if 'title' in data:
            plan.title = data['title']
        if 'objectives' in data:
            plan.objectives = data['objectives']

        db.session.commit()  # Save changes to the database
        return jsonify({'message': 'Operational plan updated successfully', 'plan': plan.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint to delete an operational plan
@app.route('/plans/<int:plan_id>', methods=['DELETE'])
def delete_plan(plan_id):
    """Delete an operational plan."""
    try:
        plan = OperationalPlan.query.get(plan_id)
        if not plan:
            return jsonify({'error': 'Operational plan not found'}), 404

        db.session.delete(plan)
        db.session.commit()
        return jsonify({'message': 'Operational plan deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Initialize the database and create tables
@app.before_first_request
def setup_database():
    """Create database tables if they don't exist."""
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
