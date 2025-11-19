"""
Generated Code Metadata:
========================
Original URL: https://iwslink.com
Prompt: Suggest tools or frameworks for creating an interactive system that alerts users about safety information and enhances customer satisfaction, referencing the Interactive Warning Systems website.
Generated: DETERMINISTIC_8174823fe1df4f3a
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alerts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Alert model
class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Alert {self.message}>'

# Create the database
with app.app_context():
    db.create_all()

# Route to create a new alert
@app.route('/alerts', methods=['POST'])
def create_alert():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        
        new_alert = Alert(message=data['message'])
        db.session.add(new_alert)
        db.session.commit()
        return jsonify({'message': 'Alert created successfully', 'alert': new_alert.message}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all alerts
@app.route('/alerts', methods=['GET'])
def get_alerts():
    try:
        alerts = Alert.query.all()
        return jsonify([{'id': alert.id, 'message': alert.message, 'created_at': alert.created_at} for alert in alerts]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to send alerts to users (placeholder for integration with a notification system)
def send_alerts():
    alerts = Alert.query.all()
    for alert in alerts:
        # Placeholder for sending alert (e.g., email, SMS, push notification)
        print(f'Sending alert: {alert.message}')

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- This code sets up a simple Flask application with a SQLite database to manage safety alerts.
- It includes routes to create and retrieve alerts, with error handling for invalid input and database errors.
- The `send_alerts` function is a placeholder for integrating with a notification system to alert users.
