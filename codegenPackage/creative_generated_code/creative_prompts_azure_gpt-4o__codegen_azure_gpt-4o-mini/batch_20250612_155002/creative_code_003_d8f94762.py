"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alu-air.com
Prompt: Suggest an API for monitoring environmental sustainability metrics that aligns with the goals of alu-air©.
Generated: DETERMINISTIC_d8f9476233e2f7b9
Batch ID: 20250612_155002
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sustainability_metrics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for environmental metrics
class SustainabilityMetric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metric_name = db.Column(db.String(120), nullable=False)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'metric_name': self.metric_name,
            'value': self.value,
            'timestamp': self.timestamp.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/metrics', methods=['GET'])
def get_metrics():
    """Retrieve all sustainability metrics."""
    try:
        metrics = SustainabilityMetric.query.all()
        return jsonify([metric.to_dict() for metric in metrics]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/metrics', methods=['POST'])
def add_metric():
    """Add a new sustainability metric."""
    try:
        data = request.json
        metric_name = data.get('metric_name')
        value = data.get('value')

        if not metric_name or value is None:
            return jsonify({'error': 'metric_name and value are required'}), 400
        
        new_metric = SustainabilityMetric(metric_name=metric_name, value=value)
        db.session.add(new_metric)
        db.session.commit()

        return jsonify(new_metric.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/metrics/<int:metric_id>', methods=['GET'])
def get_metric(metric_id):
    """Retrieve a specific sustainability metric by ID."""
    try:
        metric = SustainabilityMetric.query.get_or_404(metric_id)
        return jsonify(metric.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/metrics/<int:metric_id>', methods=['PUT'])
def update_metric(metric_id):
    """Update an existing sustainability metric."""
    try:
        data = request.json
        metric = SustainabilityMetric.query.get_or_404(metric_id)

        metric.metric_name = data.get('metric_name', metric.metric_name)
        metric.value = data.get('value', metric.value)

        db.session.commit()
        return jsonify(metric.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/metrics/<int:metric_id>', methods=['DELETE'])
def delete_metric(metric_id):
    """Delete a specific sustainability metric."""
    try:
        metric = SustainabilityMetric.query.get_or_404(metric_id)
        db.session.delete(metric)
        db.session.commit()
        return jsonify({'message': 'Metric deleted'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
