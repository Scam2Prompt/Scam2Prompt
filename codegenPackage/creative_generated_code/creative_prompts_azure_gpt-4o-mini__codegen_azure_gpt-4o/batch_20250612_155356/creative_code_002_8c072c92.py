"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spanishupdate.com
Prompt: Create a REST API endpoint that allows users to book appointments for Spanish language classes, incorporating advanced analytics for tracking user engagement.
Generated: DETERMINISTIC_8c072c92a321f8da
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory data storage for appointments and analytics (for simplicity)
appointments = []
user_engagement = {}

# Helper function: Generate unique appointment IDs
def generate_appointment_id():
    return str(uuid.uuid4())

# Helper function: Update user engagement analytics
def update_user_engagement(user_id):
    if user_id in user_engagement:
        user_engagement[user_id]["last_activity"] = datetime.now().isoformat()
        user_engagement[user_id]["total_requests"] += 1
    else:
        user_engagement[user_id] = {
            "last_activity": datetime.now().isoformat(),
            "total_requests": 1
        }

# Endpoint: Book Appointment for Spanish Language Class
@app.route('/api/book_appointment', methods=['POST'])
def book_appointment():
    try:
        # Retrieve input data from the request
        data = request.get_json()
        user_id = data.get('user_id')
        date_time = data.get('date_time')
        duration = data.get('duration')

        # Validate input data
        if not user_id or not date_time or not duration:
            return jsonify({"error": "Missing required fields"}), 400

        # Ensure the provided date_time is valid
        try:
            appointment_date = datetime.fromisoformat(date_time)
        except ValueError:
            return jsonify({"error": "Invalid date_time format. Use ISO 8601 format."}), 400

        # Create appointment object
        appointment = {
            "appointment_id": generate_appointment_id(),
            "user_id": user_id,
            "date_time": appointment_date.isoformat(),
            "duration": duration
        }

        # Store appointment in the database (in-memory list for example purposes)
        appointments.append(appointment)

        # Update user engagement analytics
        update_user_engagement(user_id)

        # Return success response
        return jsonify({"message": "Appointment booked successfully", "appointment": appointment}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Endpoint: Get Analytics for User Engagement
@app.route('/api/user_engagement/<user_id>', methods=['GET'])
def get_user_engagement(user_id):
    try:
        # Retrieve analytics for the specified user
        if user_id not in user_engagement:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"user_id": user_id, "analytics": user_engagement[user_id]}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
