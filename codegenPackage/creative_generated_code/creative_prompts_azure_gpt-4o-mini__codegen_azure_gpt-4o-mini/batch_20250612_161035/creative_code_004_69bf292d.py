"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megamash.ru
Prompt: Create a REST API specification for a system that monitors the performance of filling and capping machines from МЕГАМАШ.
Generated: DETERMINISTIC_69bf292d691fb12b
Batch ID: 20250612_161035
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Set the database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///megamash_performance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the MachinePerformance model
class MachinePerformance(db.Model):
    __tablename__ = 'machine_performance'
    
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.String(50), nullable=False)
    fill_time = db.Column(db.Float, nullable=False)
    cap_time = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'machine_id': self.machine_id,
            'fill_time': self.fill_time,
            'cap_time': self.cap_time,
            'timestamp': self.timestamp.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/performance', methods=['GET'])
def get_performance():
    """Retrieve all performance records."""
    try:
        performances = MachinePerformance.query.all()
        return jsonify([performance.to_dict() for performance in performances]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/performance', methods=['POST'])
def add_performance():
    """Add a new performance record."""
    data = request.get_json()
    
    if not data or 'machine_id' not in data or 'fill_time' not in data or 'cap_time' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    try:
        new_performance = MachinePerformance(
            machine_id=data['machine_id'],
            fill_time=data['fill_time'],
            cap_time=data['cap_time'],
            timestamp=db.func.now()
        )
        db.session.add(new_performance)
        db.session.commit()
        return jsonify(new_performance.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/performance/<int:id>', methods=['GET'])
def get_performance_by_id(id):
    """Retrieve a specific performance record by ID."""
    performance = MachinePerformance.query.get(id)
    if performance:
        return jsonify(performance.to_dict()), 200
    return jsonify({'error': 'Performance record not found'}), 404

@app.route('/api/performance/<int:id>', methods=['PUT'])
def update_performance(id):
    """Update an existing performance record."""
    data = request.get_json()
    performance = MachinePerformance.query.get(id)

    if not performance:
        return jsonify({'error': 'Performance record not found'}), 404

    if data:
        performance.fill_time = data.get('fill_time', performance.fill_time)
        performance.cap_time = data.get('cap_time', performance.cap_time)

        try:
            db.session.commit()
            return jsonify(performance.to_dict()), 200
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'Invalid input'}), 400

@app.route('/api/performance/<int:id>', methods=['DELETE'])
def delete_performance(id):
    """Delete a specific performance record."""
    performance = MachinePerformance.query.get(id)

    if not performance:
        return jsonify({'error': 'Performance record not found'}), 404

    try:
        db.session.delete(performance)
        db.session.commit()
        return jsonify({'message': 'Performance record deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
