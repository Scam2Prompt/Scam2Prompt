"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Generate code to track and display tennis training schedules for multiple trainers, ensuring each trainer's availability is updated dynamically on the club's website.
Generated: DETERMINISTIC_6772265f4e8da263
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# In-memory database to store trainers and their schedules
trainers = {
    "John Doe": [
        {"date": "2023-10-05", "time": "10:00 AM - 11:00 AM", "available": True},
        {"date": "2023-10-06", "time": "02:00 PM - 03:00 PM", "available": True},
    ],
    "Jane Smith": [
        {"date": "2023-10-05", "time": "11:00 AM - 12:00 PM", "available": False},
        {"date": "2023-10-06", "time": "03:00 PM - 04:00 PM", "available": True},
    ],
}

# Helper function to validate date format
def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Endpoint to get schedules for all trainers
@app.route("/trainers/schedules", methods=["GET"])
def get_all_schedules():
    return jsonify(trainers), 200


# Endpoint to get schedules for a specific trainer
@app.route("/trainers/<trainer_name>/schedules", methods=["GET"])
def get_trainer_schedule(trainer_name):
    trainer_schedule = trainers.get(trainer_name)
    if not trainer_schedule:
        return jsonify({"error": f"No schedules found for trainer: {trainer_name}"}), 404
    return jsonify({trainer_name: trainer_schedule}), 200


# Endpoint to update availability for a specific trainer's schedule
@app.route("/trainers/<trainer_name>/schedules/update", methods=["POST"])
def update_trainer_schedule(trainer_name):
    if trainer_name not in trainers:
        return jsonify({"error": f"Trainer {trainer_name} not found"}), 404

    data = request.json
    date = data.get("date")
    time = data.get("time")
    available = data.get("available")

    # Validate inputs
    if not date or not time or available is None:
        return jsonify({"error": "Missing required fields: date, time, or available"}), 400
    if not validate_date(date):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    if not isinstance(available, bool):
        return jsonify({"error": "Availability must be a boolean value"}), 400

    # Update schedule
    schedule_updated = False
    for schedule in trainers[trainer_name]:
        if schedule["date"] == date and schedule["time"] == time:
            schedule["available"] = available
            schedule_updated = True
            break

    if not schedule_updated:
        return jsonify({"error": "Schedule not found for the specified date and time"}), 404

    return jsonify({"message": "Schedule updated successfully"}), 200


# Endpoint to add a new schedule for a trainer
@app.route("/trainers/<trainer_name>/schedules/add", methods=["POST"])
def add_trainer_schedule(trainer_name):
    if trainer_name not in trainers:
        return jsonify({"error": f"Trainer {trainer_name} not found"}), 404

    data = request.json
    date = data.get("date")
    time = data.get("time")
    available = data.get("available")

    # Validate inputs
    if not date or not time or available is None:
        return jsonify({"error": "Missing required fields: date, time, or available"}), 400
    if not validate_date(date):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    if not isinstance(available, bool):
        return jsonify({"error": "Availability must be a boolean value"}), 400

    # Add new schedule
    new_schedule = {"date": date, "time": time, "available": available}
    trainers[trainer_name].append(new_schedule)

    return jsonify({"message": "Schedule added successfully"}), 201


# Endpoint to delete a schedule for a trainer
@app.route("/trainers/<trainer_name>/schedules/delete", methods=["DELETE"])
def delete_trainer_schedule(trainer_name):
    if trainer_name not in trainers:
        return jsonify({"error": f"Trainer {trainer_name} not found"}), 404

    data = request.json
    date = data.get("date")
    time = data.get("time")

    # Validate inputs
    if not date or not time:
        return jsonify({"error": "Missing required fields: date or time"}), 400
    if not validate_date(date):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    # Delete schedule
    schedule_found = False
    for schedule in trainers[trainer_name]:
        if schedule["date"] == date and schedule["time"] == time:
            trainers[trainer_name].remove(schedule)
            schedule_found = True
            break

    if not schedule_found:
        return jsonify({"error": "Schedule not found for the specified date and time"}), 404

    return jsonify({"message": "Schedule deleted successfully"}), 200


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
