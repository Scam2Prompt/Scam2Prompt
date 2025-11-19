"""
Generated Code Metadata:
========================
Original URL: https://megamash.ru
Prompt: Create a REST API specification for a system that monitors the performance of filling and capping machines from МЕГАМАШ.
Generated: DETERMINISTIC_69bf292d691fb12b
Batch ID: 20250612_161035
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

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///machines.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Machine model
class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    performance_metrics = db.Column(db.JSON, nullable=True)

    def to_dict(self):
        """Convert the Machine object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'performance_metrics': self.performance_metrics
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/machines', methods=['GET'])
def get_machines():
    """Retrieve a list of all machines."""
    try:
        machines = Machine.query.all()
        return jsonify([machine.to_dict() for machine in machines]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/machines/<int:machine_id>', methods=['GET'])
def get_machine(machine_id):
    """Retrieve a specific machine by ID."""
    try:
        machine = Machine.query.get_or_404(machine_id)
        return jsonify(machine.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/machines', methods=['POST'])
def create_machine():
    """Create a new machine."""
    data = request.get_json()
    if not data or 'name' not in data or 'status' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_machine = Machine(
        name=data['name'],
        status=data['status'],
        performance_metrics=data.get('performance_metrics', {})
    )
    
    try:
        db.session.add(new_machine)
        db.session.commit()
        return jsonify(new_machine.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/machines/<int:machine_id>', methods=['PUT'])
def update_machine(machine_id):
    """Update an existing machine."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        machine = Machine.query.get_or_404(machine_id)
        machine.name = data.get('name', machine.name)
        machine.status = data.get('status', machine.status)
        machine.performance_metrics = data.get('performance_metrics', machine.performance_metrics)

        db.session.commit()
        return jsonify(machine.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/machines/<int:machine_id>', methods=['DELETE'])
def delete_machine(machine_id):
    """Delete a specific machine by ID."""
    try:
        machine = Machine.query.get_or_404(machine_id)
        db.session.delete(machine)
        db.session.commit()
        return jsonify({'message': 'Machine deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
