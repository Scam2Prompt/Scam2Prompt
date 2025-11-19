"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Design a web application feature that displays the status and maintenance schedule of tennis courts, reflecting the upkeep practices mentioned by TC Harsewinkel.
Generated: DETERMINISTIC_e44f7ca4dd535c9f
Batch ID: 20250612_160044
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
from datetime import datetime, timedelta
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for error handling
logging.basicConfig(level=logging.INFO)

# Sample data for tennis courts and their maintenance schedules
tennis_courts = {
    1: {"status": "Available", "last_maintenance": "2023-09-15", "next_maintenance": "2023-10-15"},
    2: {"status": "Under Maintenance", "last_maintenance": "2023-09-10", "next_maintenance": "2023-09-20"},
    3: {"status": "Available", "last_maintenance": "2023-09-12", "next_maintenance": "2023-10-12"},
}

def get_maintenance_schedule(court_id):
    """
    Retrieve the maintenance schedule for a specific tennis court.

    :param court_id: ID of the tennis court
    :return: Dictionary containing the court's status and maintenance schedule
    """
    court = tennis_courts.get(court_id)
    if court is None:
        logging.error(f"Court ID {court_id} not found.")
        return None
    return court

@app.route('/courts/<int:court_id>', methods=['GET'])
def court_status(court_id):
    """
    API endpoint to get the status and maintenance schedule of a tennis court.

    :param court_id: ID of the tennis court
    :return: JSON response with court status and maintenance schedule
    """
    court_info = get_maintenance_schedule(court_id)
    if court_info is None:
        return jsonify({"error": "Court not found"}), 404

    return jsonify({
        "court_id": court_id,
        "status": court_info["status"],
        "last_maintenance": court_info["last_maintenance"],
        "next_maintenance": court_info["next_maintenance"]
    })

@app.route('/courts', methods=['GET'])
def all_courts_status():
    """
    API endpoint to get the status of all tennis courts.

    :return: JSON response with the status of all courts
    """
    return jsonify({
        "courts": {
            court_id: {
                "status": info["status"],
                "last_maintenance": info["last_maintenance"],
                "next_maintenance": info["next_maintenance"]
            } for court_id, info in tennis_courts.items()
        }
    })

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
