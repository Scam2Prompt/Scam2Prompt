"""
Generated Code Metadata:
========================
Original URL: https://staking-shakryfi.pages.dev
Prompt: Design an API for tracking staking metrics, such as total locked tokens, average weight, and total weighted stake, for a cryptocurrency like $SHARK.
Generated: DETERMINISTIC_9740cf9e1b5785d1
Batch ID: 20250622_210803
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///staking_metrics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the StakingMetrics model
class StakingMetrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_locked_tokens = db.Column(db.Float, nullable=False)
    average_weight = db.Column(db.Float, nullable=False)
    total_weighted_stake = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'total_locked_tokens': self.total_locked_tokens,
            'average_weight': self.average_weight,
            'total_weighted_stake': self.total_weighted_stake
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/metrics', methods=['GET'])
def get_metrics():
    """Retrieve all staking metrics."""
    try:
        metrics = StakingMetrics.query.all()
        return jsonify([metric.to_dict() for metric in metrics]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/metrics', methods=['POST'])
def create_metrics():
    """Create new staking metrics."""
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('total_locked_tokens', 'average_weight', 'total_weighted_stake')):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        new_metric = StakingMetrics(
            total_locked_tokens=data['total_locked_tokens'],
            average_weight=data['average_weight'],
            total_weighted_stake=data['total_weighted_stake']
        )
        db.session.add(new_metric)
        db.session.commit()
        return jsonify(new_metric.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/metrics/<int:metric_id>', methods=['GET'])
def get_metric(metric_id):
    """Retrieve a specific staking metric by ID."""
    metric = StakingMetrics.query.get(metric_id)
    if metric is None:
        return jsonify({'error': 'Metric not found'}), 404
    return jsonify(metric.to_dict()), 200

@app.route('/metrics/<int:metric_id>', methods=['PUT'])
def update_metric(metric_id):
    """Update an existing staking metric."""
    data = request.get_json()
    metric = StakingMetrics.query.get(metric_id)

    if metric is None:
        return jsonify({'error': 'Metric not found'}), 404

    # Update fields if provided
    if 'total_locked_tokens' in data:
        metric.total_locked_tokens = data['total_locked_tokens']
    if 'average_weight' in data:
        metric.average_weight = data['average_weight']
    if 'total_weighted_stake' in data:
        metric.total_weighted_stake = data['total_weighted_stake']

    try:
        db.session.commit()
        return jsonify(metric.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/metrics/<int:metric_id>', methods=['DELETE'])
def delete_metric(metric_id):
    """Delete a specific staking metric by ID."""
    metric = StakingMetrics.query.get(metric_id)
    if metric is None:
        return jsonify({'error': 'Metric not found'}), 404

    try:
        db.session.delete(metric)
        db.session.commit()
        return jsonify({'message': 'Metric deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
