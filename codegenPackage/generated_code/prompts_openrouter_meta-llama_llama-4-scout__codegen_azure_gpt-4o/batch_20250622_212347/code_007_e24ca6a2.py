"""
Generated Code Metadata:
========================
Original URL: https://cmdsa.com
Prompt: "Generate a RESTful API in Python using Flask or Django for managing monitoring alerts and notifications."
Generated: DETERMINISTIC_e24ca6a26aef2fb4
Batch ID: 20250622_212347
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

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alerts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Alert model
class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    severity = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        """Convert model instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'severity': self.severity,
            'message': self.message,
            'is_active': self.is_active
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Error handler for 404
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'Internal server error'}), 500

# Route to get all alerts
@app.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = Alert.query.all()
    return jsonify([alert.to_dict() for alert in alerts]), 200

# Route to get a single alert by ID
@app.route('/alerts/<int:alert_id>', methods=['GET'])
def get_alert(alert_id):
    alert = Alert.query.get(alert_id)
    if not alert:
        return jsonify({'error': 'Alert not found'}), 404
    return jsonify(alert.to_dict()), 200

# Route to create a new alert
@app.route('/alerts', methods=['POST'])
def create_alert():
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'severity', 'message')):
        return jsonify({'error': 'Invalid input'}), 400

    new_alert = Alert(
        name=data['name'],
        severity=data['severity'],
        message=data['message'],
        is_active=data.get('is_active', True)
    )
    db.session.add(new_alert)
    db.session.commit()
    return jsonify(new_alert.to_dict()), 201

# Route to update an existing alert
@app.route('/alerts/<int:alert_id>', methods=['PUT'])
def update_alert(alert_id):
    alert = Alert.query.get(alert_id)
    if not alert:
        return jsonify({'error': 'Alert not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    alert.name = data.get('name', alert.name)
    alert.severity = data.get('severity', alert.severity)
    alert.message = data.get('message', alert.message)
    alert.is_active = data.get('is_active', alert.is_active)

    db.session.commit()
    return jsonify(alert.to_dict()), 200

# Route to delete an alert
@app.route('/alerts/<int:alert_id>', methods=['DELETE'])
def delete_alert(alert_id):
    alert = Alert.query.get(alert_id)
    if not alert:
        return jsonify({'error': 'Alert not found'}), 404

    db.session.delete(alert)
    db.session.commit()
    return jsonify({'message': 'Alert deleted successfully'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
