"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Generate code for a web-based platform that allows for real-time monitoring of agricultural activities, including scheduling, registration, and reporting, like Azagros.
Generated: DETERMINISTIC_c89bc91684221ed9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a web-based platform for real-time monitoring of agricultural activities. The code uses Python with the Flask framework for the backend and SQLite for the database. It includes scheduling, registration, and reporting functionalities.

### Backend Code (`app.py`)

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agriculture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activity_type = db.Column(db.String(100), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default="Pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Error handling middleware
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Routes
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Expects JSON payload: {"name": "John Doe", "email": "john@example.com"}
    """
    data = request.get_json()
    try:
        name = data['name']
        email = data['email']
        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400

        # Check if email already exists
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already registered"}), 400

        # Create new user
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully", "user_id": new_user.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/schedule', methods=['POST'])
def schedule_activity():
    """
    Endpoint to schedule a new agricultural activity.
    Expects JSON payload: {"user_id": 1, "activity_type": "Planting", "scheduled_time": "2023-10-01T10:00:00"}
    """
    data = request.get_json()
    try:
        user_id = data['user_id']
        activity_type = data['activity_type']
        scheduled_time = data['scheduled_time']

        # Validate inputs
        if not user_id or not activity_type or not scheduled_time:
            return jsonify({"error": "User ID, activity type, and scheduled time are required"}), 400

        # Check if user exists
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Create new activity
        new_activity = Activity(
            user_id=user_id,
            activity_type=activity_type,
            scheduled_time=datetime.fromisoformat(scheduled_time)
        )
        db.session.add(new_activity)
        db.session.commit()
        return jsonify({"message": "Activity scheduled successfully", "activity_id": new_activity.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/report', methods=['GET'])
def get_report():
    """
    Endpoint to fetch a report of all activities.
    Optional query parameters: user_id=<int>
    """
    try:
        user_id = request.args.get('user_id')
        if user_id:
            activities = Activity.query.filter_by(user_id=user_id).all()
        else:
            activities = Activity.query.all()

        # Format response
        report = [
            {
                "activity_id": activity.id,
                "user_id": activity.user_id,
                "activity_type": activity.activity_type,
                "scheduled_time": activity.scheduled_time.isoformat(),
                "status": activity.status,
                "created_at": activity.created_at.isoformat()
            }
            for activity in activities
        ]
        return jsonify(report), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Database Initialization
Run the following command to initialize the SQLite database:
```bash
python app.py
```

### Frontend (Optional)
You can use a frontend framework like React or Vue.js to interact with this API.
