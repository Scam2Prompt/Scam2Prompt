"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://44-cm7.pages.dev
Prompt: Suggest an API for managing user notifications for collectible drops like Pudgy Penguins "GoldFeathers".
Generated: DETERMINISTIC_4b4aaa3a8f2ee09f
Batch ID: 20250612_161246
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
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notifications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Notification(db.Model):
    """Model representing a user notification."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def serialize(self):
        """Serialize the notification instance to a dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'message': self.message,
            'created_at': self.created_at.isoformat()
        }

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/notifications', methods=['POST'])
def create_notification():
    """Create a new notification for a user."""
    data = request.get_json()

    if not data or 'user_id' not in data or 'message' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    notification = Notification(user_id=data['user_id'], message=data['message'])
    
    try:
        db.session.add(notification)
        db.session.commit()
        return jsonify(notification.serialize()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/notifications/<int:user_id>', methods=['GET'])
def get_notifications(user_id):
    """Retrieve all notifications for a specific user."""
    notifications = Notification.query.filter_by(user_id=user_id).all()
    return jsonify([n.serialize() for n in notifications]), 200

@app.route('/notifications/<int:id>', methods=['DELETE'])
def delete_notification(id):
    """Delete a notification by its ID."""
    notification = Notification.query.get(id)

    if not notification:
        return jsonify({'error': 'Notification not found'}), 404
    
    try:
        db.session.delete(notification)
        db.session.commit()
        return jsonify({'message': 'Notification deleted'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
