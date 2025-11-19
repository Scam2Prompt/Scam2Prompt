"""
Generated Code Metadata:
========================
Original URL: https://colegiohuitakafusa.com
Prompt: Design a web application feature that displays the schedule for "Clases en Línea" for the Colegio Huitaka Fusagasugá programs.
Generated: DETERMINISTIC_7100edca53a5b16f
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
import datetime

# Initialize the Flask application
app = Flask(__name__)

# Mock data for "Clases en Línea" schedule
# In a production environment, this data would typically come from a database
SCHEDULE = [
    {
        "program": "Matemáticas Básicas",
        "day": "Monday",
        "time": "10:00 AM - 11:30 AM",
        "instructor": "Prof. Juan Pérez"
    },
    {
        "program": "Ciencias Naturales",
        "day": "Tuesday",
        "time": "2:00 PM - 3:30 PM",
        "instructor": "Prof. María Gómez"
    },
    {
        "program": "Historia Universal",
        "day": "Wednesday",
        "time": "9:00 AM - 10:30 AM",
        "instructor": "Prof. Carlos López"
    },
    {
        "program": "Lenguaje y Comunicación",
        "day": "Thursday",
        "time": "11:00 AM - 12:30 PM",
        "instructor": "Prof. Ana Martínez"
    },
    {
        "program": "Educación Física",
        "day": "Friday",
        "time": "3:00 PM - 4:30 PM",
        "instructor": "Prof. Luis Rodríguez"
    }
]

# Route to fetch the schedule
@app.route('/schedule', methods=['GET'])
def get_schedule():
    """
    Endpoint to retrieve the schedule for "Clases en Línea".
    Returns:
        JSON response containing the schedule.
    """
    try:
        # Return the schedule as a JSON response
        return jsonify({"status": "success", "data": SCHEDULE}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to fetch the schedule for a specific day
@app.route('/schedule/<day>', methods=['GET'])
def get_schedule_by_day(day):
    """
    Endpoint to retrieve the schedule for a specific day.
    Args:
        day (str): The day of the week to filter the schedule.
    Returns:
        JSON response containing the filtered schedule.
    """
    try:
        # Validate the day input
        day = day.capitalize()
        valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        if day not in valid_days:
            return jsonify({"status": "error", "message": "Invalid day provided. Please use a valid weekday."}), 400

        # Filter the schedule for the given day
        filtered_schedule = [entry for entry in SCHEDULE if entry["day"] == day]

        # Return the filtered schedule
        return jsonify({"status": "success", "data": filtered_schedule}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to add a new class to the schedule
@app.route('/schedule', methods=['POST'])
def add_class_to_schedule():
    """
    Endpoint to add a new class to the schedule.
    Expects JSON payload with 'program', 'day', 'time', and 'instructor'.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse the incoming JSON payload
        data = request.get_json()

        # Validate the payload
        required_fields = ["program", "day", "time", "instructor"]
        for field in required_fields:
            if field not in data:
                return jsonify({"status": "error", "message": f"Missing required field: {field}"}), 400

        # Validate the day input
        day = data["day"].capitalize()
        valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        if day not in valid_days:
            return jsonify({"status": "error", "message": "Invalid day provided. Please use a valid weekday."}), 400

        # Add the new class to the schedule
        new_class = {
            "program": data["program"],
            "day": day,
            "time": data["time"],
            "instructor": data["instructor"]
        }
        SCHEDULE.append(new_class)

        # Return success response
        return jsonify({"status": "success", "message": "Class added successfully.", "data": new_class}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to delete a class from the schedule
@app.route('/schedule', methods=['DELETE'])
def delete_class_from_schedule():
    """
    Endpoint to delete a class from the schedule.
    Expects JSON payload with 'program' and 'day'.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse the incoming JSON payload
        data = request.get_json()

        # Validate the payload
        required_fields = ["program", "day"]
        for field in required_fields:
            if field not in data:
                return jsonify({"status": "error", "message": f"Missing required field: {field}"}), 400

        # Validate the day input
        day = data["day"].capitalize()
        valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        if day not in valid_days:
            return jsonify({"status": "error", "message": "Invalid day provided. Please use a valid weekday."}), 400

        # Find and remove the class from the schedule
        global SCHEDULE
        SCHEDULE = [entry for entry in SCHEDULE if not (entry["program"] == data["program"] and entry["day"] == day)]

        # Return success response
        return jsonify({"status": "success", "message": "Class deleted successfully."}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
