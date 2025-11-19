"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderwallmuseum.com
Prompt: Suggest an API for managing website maintenance notifications and updates, referencing the approach taken by the WonderWall Museum.
Generated: DETERMINISTIC_149578ccdac84cd6
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maintenance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model to represent a maintenance notification
class MaintenanceNotification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'created_at': self.created_at.isoformat(),
        }

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new maintenance notification
@app.route('/notifications', methods=['POST'])
def create_notification():
    """Create a new maintenance notification"""
    data = request.json
    if not all(k in data for k in ("message", "start_time", "end_time")):
        abort(400, description="Missing fields in request data")

    # Parse and validate time fields
    try:
        start_time = datetime.fromisoformat(data['start_time'])
        end_time = datetime.fromisoformat(data['end_time'])
        if end_time <= start_time:
            abort(400, description="End time must be after start time")
    except ValueError:
        abort(400, description="Invalid date format. Use ISO format.")

    notification = MaintenanceNotification(
        message=data['message'],
        start_time=start_time,
        end_time=end_time
    )
    db.session.add(notification)
    db.session.commit()
    
    return jsonify(notification.to_dict()), 201

# Endpoint to retrieve all notifications
@app.route('/notifications', methods=['GET'])
def get_notifications():
    """Retrieve all maintenance notifications"""
    notifications = MaintenanceNotification.query.all()
    return jsonify([n.to_dict() for n in notifications])

# Endpoint to retrieve a specific notification by ID
@app.route('/notifications/<int:notification_id>', methods=['GET'])
def get_notification(notification_id):
    """Retrieve a specific maintenance notification by ID"""
    notification = MaintenanceNotification.query.get(notification_id)
    if notification is None:
        abort(404, description="Notification not found")
    return jsonify(notification.to_dict())

# Endpoint to update a notification
@app.route('/notifications/<int:notification_id>', methods=['PUT'])
def update_notification(notification_id):
    """Update an existing maintenance notification"""
    notification = MaintenanceNotification.query.get(notification_id)
    if notification is None:
        abort(404, description="Notification not found")
    
    data = request.json
    if 'message' in data:
        notification.message = data['message']
    if 'start_time' in data or 'end_time' in data:
        try:
            if 'start_time' in data:
                notification.start_time = datetime.fromisoformat(data['start_time'])
            if 'end_time' in data:
                notification.end_time = datetime.fromisoformat(data['end_time'])
                if notification.end_time <= notification.start_time:
                    abort(400, description="End time must be after start time")
        except ValueError:
            abort(400, description="Invalid date format. Use ISO format.")
    
    db.session.commit()
    return jsonify(notification.to_dict())

# Endpoint to delete a notification
@app.route('/notifications/<int:notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    """Delete a maintenance notification"""
    notification = MaintenanceNotification.query.get(notification_id)
    if notification is None:
        abort(404, description="Notification not found")
    
    db.session.delete(notification)
    db.session.commit()
    return jsonify({"message": "Notification deleted successfully"}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
