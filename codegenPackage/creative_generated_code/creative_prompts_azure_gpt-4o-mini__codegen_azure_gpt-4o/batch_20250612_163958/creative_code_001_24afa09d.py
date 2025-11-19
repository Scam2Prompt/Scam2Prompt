"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: How can I implement a smart school bus tracking API to enhance the transportation system for a school like Happy Boarding School?
Generated: DETERMINISTIC_24afa09da0d4d7d9
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from geopy.distance import geodesic
import datetime

# Initialize the Flask application
app = Flask(__name__)

# Sample data (in a production system, this would likely come from a database)
BUS_DATA = [
    {
        "bus_id": 1,
        "location": {"lat": 40.712776, "lng": -74.005974},  # Sample Bus Location (New York City, NY)
        "driver_name": "John Doe",
        "capacity": 40,
        "occupied_seats": 35,
    },
    {
        "bus_id": 2,
        "location": {"lat": 34.052235, "lng": -118.243683},  # Sample Bus Location (Los Angeles, CA)
        "driver_name": "Jane Smith",
        "capacity": 50,
        "occupied_seats": 20,
    },
]

STUDENT_DATA = [
    {
        "student_id": 1,
        "name": "Alice",
        "location": {"lat": 40.730610, "lng": -73.935242},  # Sample Student Location (New York City, NY)
        "bus_assigned": 1,
    },
    {
        "student_id": 2,
        "name": "Bob",
        "location": {"lat": 34.052235, "lng": -118.243683},  # Sample Student Location (Los Angeles, CA)
        "bus_assigned": 2,
    },
]

# Utility function to calculate distance between two geographical points
def calculate_distance(location1, location2):
    try:
        return geodesic(
            (location1["lat"], location1["lng"]),
            (location2["lat"], location2["lng"])
        ).miles
    except Exception as e:
        print(f"Error calculating distance: {e}")
        return None

@app.route('/')
def health_check():
    """
    Health check endpoint to verify API status.
    """
    return jsonify({"status": "API is running"}), 200

@app.route('/bus/<int:bus_id>', methods=['GET'])
def get_bus_details(bus_id):
    """
    API endpoint to retrieve details of a specific bus.
    """
    try:
        # Find the bus by ID
        bus = next((bus for bus in BUS_DATA if bus["bus_id"] == bus_id), None)
        if not bus:
            return jsonify({"error": "Bus not found"}), 404
        return jsonify(bus), 200
    except Exception as e:
        return jsonify({"error": f"Unexpected error occurred: {str(e)}"}), 500

@app.route('/student/<int:student_id>', methods=['GET'])
def get_student_details(student_id):
    """
    API endpoint to retrieve the details of a specific student.
    """
    try:
        # Find the student by ID
        student = next((student for student in STUDENT_DATA if student["student_id"] == student_id), None)
        if not student:
            return jsonify({"error": "Student not found"}), 404
        
        # Get assigned bus information
        bus = next((bus for bus in BUS_DATA if bus["bus_id"] == student["bus_assigned"]), None)
        if not bus:
            return jsonify({"error": "Bus information not available"}), 404

        # Calculate distance from student to their assigned bus
        distance_to_bus = calculate_distance(student["location"], bus["location"])

        # Return detailed student information
        return jsonify({
            "student": student,
            "assigned_bus": bus,
            "distance_to_bus_miles": distance_to_bus
        }), 200
    except Exception as e:
        return jsonify({"error": f"Unexpected error occurred: {str(e)}"}), 500

@app.route('/track', methods=['POST'])
def track_bus():
    """
    API endpoint to track a bus and get its updated location and distance to a given point.
    """
    try:
        # Parse the incoming JSON request
        data = request.json
        bus_id = data.get("bus_id")
        target_location = data.get("location")  # Expected format: {"lat": float, "lng": float}

        if not bus_id or not target_location:
            return jsonify({"error": "Missing required parameters (bus_id, location)"}), 400

        # Find the bus by ID
        bus = next((bus for bus in BUS_DATA if bus["bus_id"] == bus_id), None)
        if not bus:
            return jsonify({"error": "Bus not found"}), 404

        # Calculate the distance to target location
        distance_to_target = calculate_distance(bus["location"], target_location)

        if distance_to_target is None:
            return jsonify({"error": "Error calculating distance"}), 500

        # Return bus tracking details
        return jsonify({
            "bus_id": bus_id,
            "current_location": bus["location"],
            "distance_to_target_miles": distance_to_target,
            "timestamp": datetime.datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({"error": f"Unexpected error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
