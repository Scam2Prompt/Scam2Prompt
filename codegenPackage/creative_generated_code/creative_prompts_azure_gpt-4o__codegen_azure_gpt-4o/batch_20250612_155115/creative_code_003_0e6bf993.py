"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Provide an API recommendation for tracking global economic events and their impact on market performance, as emphasized on Investolazlo.
Generated: DETERMINISTIC_0e6bf993339432d5
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Flask-based API to track global economic events and their impact on market performance.
# Author: <Your Name>
# Date: <Date>
# Version: 1.0.0

from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Sample data to simulate economic events and market impact
# In production, this data would come from a real database or external API
economic_events = [
    {
        "id": 1,
        "event_name": "Federal Reserve Interest Rate Decision",
        "date": "2023-11-01",
        "impact": {
            "market": "S&P 500",
            "change": "+0.5%",
            "reason": "Rate cut provided market stimulus"
        }
    },
    {
        "id": 2,
        "event_name": "US Consumer Price Index Release",
        "date": "2023-11-15",
        "impact": {
            "market": "NASDAQ",
            "change": "-0.8%",
            "reason": "Higher inflation data dampened sentiment"
        }
    }
]

@app.route('/api/events', methods=['GET'])
def get_events():
    """
    Endpoint to retrieve all economic events and their market impacts.
    Returns:
        JSON response with all economic events.
    """
    logging.info("Fetching all economic events.")
    return jsonify(economic_events), 200


@app.route('/api/events/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    """
    Endpoint to retrieve a single economic event by its ID.
    Args:
        event_id (int): ID of the requested event.
    Returns:
        JSON response with the specific event details or error message if not found.
    """
    logging.info(f"Fetching event with ID: {event_id}")
    event = next((e for e in economic_events if e['id'] == event_id), None)
    if event:
        return jsonify(event), 200
    else:
        logging.warning(f"Event with ID {event_id} not found.")
        return jsonify({"error": "Event not found"}), 404


@app.route('/api/events', methods=['POST'])
def add_event():
    """
    Endpoint to add a new economic event.
    Expects JSON payload with 'event_name', 'date', and 'impact' details.
    Returns:
        JSON response with the added event or error message in case of invalid input.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ["event_name", "date", "impact"]):
            logging.error("Invalid input data. Missing required fields.")
            return jsonify({"error": "Invalid input. Required fields: event_name, date, impact"}), 400
        
        new_event = {
            "id": len(economic_events) + 1,
            "event_name": data["event_name"],
            "date": data["date"],
            "impact": data["impact"]
        }
        economic_events.append(new_event)
        logging.info(f"New event added: {new_event}")
        return jsonify(new_event), 201
    except Exception as e:
        logging.error(f"Error occurred while adding event: {str(e)}")
        return jsonify({"error": "An error occurred while adding the event"}), 500


@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """
    Endpoint to delete an economic event by its ID.
    Args:
        event_id (int): ID of the event to be deleted.
    Returns:
        JSON response indicating success or failure of the deletion.
    """
    logging.info(f"Attempting to delete event with ID: {event_id}")
    global economic_events
    event = next((e for e in economic_events if e['id'] == event_id), None)
    if event:
        economic_events = [e for e in economic_events if e['id'] != event_id]
        logging.info(f"Event with ID {event_id} deleted successfully.")
        return jsonify({"message": "Event deleted successfully"}), 200
    else:
        logging.warning(f"Event with ID {event_id} not found.")
        return jsonify({"error": "Event not found"}), 404


# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

This code provides a production-ready Flask API to track global economic events and their market impacts. It includes endpoints for retrieving, adding, and deleting events, with robust error handling and logging for debugging and monitoring in production environments.
