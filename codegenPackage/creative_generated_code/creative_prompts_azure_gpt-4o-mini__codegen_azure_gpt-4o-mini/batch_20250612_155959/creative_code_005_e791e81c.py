"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Create a sample API endpoint for sending notifications to users on a platform that allows private chats and tips, based on Lovr's functionalities.
Generated: DETERMINISTIC_e791e81c5ad9a2d3
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notifications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Model for Notification
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(255), nullable=False)
    is_read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Notification {self.id} for User {self.user_id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/notifications', methods=['POST'])
def send_notification():
    """
    Endpoint to send notifications to users.
    Expected JSON payload: { "user_id": <int>, "message": "<string>" }
    Returns a JSON response with the status of the operation.
    """
    try:
        data = request.get_json()
        
        # Validate input data
        if not data or 'user_id' not in data or 'message' not in data:
            return jsonify({"error": "Invalid input data"}), 400
        
        user_id = data['user_id']
        message = data['message']

        # Create a new notification
        notification = Notification(user_id=user_id, message=message)
        db.session.add(notification)
        db.session.commit()

        return jsonify({"message": "Notification sent", "notification_id": notification.id}), 201

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@app.route('/api/notifications/<int:user_id>', methods=['GET'])
def get_notifications(user_id):
    """
    Endpoint to retrieve notifications for a specific user.
    Returns a JSON array of notifications.
    """
    try:
        notifications = Notification.query.filter_by(user_id=user_id).all()
        return jsonify([{
            "id": n.id,
            "message": n.message,
            "is_read": n.is_read
        } for n in notifications]), 200

    except SQLAlchemyError as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
