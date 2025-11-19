"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pozymedia.com
Prompt: Write a code snippet for a website that integrates an event management system, focusing on features like vendor contract negotiation and program management, inspired by Pozy Media's services.
Generated: DETERMINISTIC_24af7e04db03e3fb
Batch ID: 20250612_161700
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
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Sample in-memory database for simplicity
# In production, replace with a proper database system (e.g., PostgreSQL, MongoDB)
events = {}  # Stores event details
vendors = {}  # Stores vendor contracts

# Error messages
ERROR_EVENT_NOT_FOUND = "Event not found."
ERROR_VENDOR_NOT_FOUND = "Vendor not found."

# Route: Create a new event
@app.route("/events", methods=["POST"])
def create_event():
    """
    Endpoint to create a new event.
    Expected JSON Request Body:
    {
        "name": "Event Name",
        "date": "YYYY-MM-DD",
        "location": "Event Location",
        "program": ["Activity 1", "Activity 2"]
    }
    """
    try:
        data = request.json
        event_id = str(len(events) + 1)  # Generate a unique ID for the event
        events[event_id] = {
            "name": data["name"],
            "date": datetime.strptime(data["date"], "%Y-%m-%d").date(),
            "location": data["location"],
            "program": data["program"],
            "vendors": []
        }
        return jsonify({"message": "Event created successfully!", "event_id": event_id}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Add a vendor contract to an event
@app.route("/events/<event_id>/vendors", methods=["POST"])
def add_vendor_to_event(event_id):
    """
    Endpoint to add a vendor contract to an event.
    Expected JSON Request Body:
    {
        "vendor_name": "Vendor Name",
        "contract_details": "Contract Details"
    }
    """
    try:
        # Check if event exists
        if event_id not in events:
            return jsonify({"error": ERROR_EVENT_NOT_FOUND}), 404

        data = request.json
        vendor_id = str(len(vendors) + 1)  # Generate a unique ID for the vendor
        vendors[vendor_id] = {
            "vendor_name": data["vendor_name"],
            "contract_details": data["contract_details"]
        }
        # Link vendor to the event
        events[event_id]["vendors"].append(vendor_id)
        return jsonify({"message": "Vendor added successfully!", "vendor_id": vendor_id}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: View program details for an event
@app.route("/events/<event_id>/program", methods=["GET"])
def view_event_program(event_id):
    """
    Endpoint to view program details for an event.
    """
    try:
        # Check if event exists
        if event_id not in events:
            return jsonify({"error": ERROR_EVENT_NOT_FOUND}), 404

        program = events[event_id]["program"]
        return jsonify({"program": program}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: View vendor contracts for an event
@app.route("/events/<event_id>/vendors", methods=["GET"])
def view_event_vendors(event_id):
    """
    Endpoint to view vendor contracts for an event.
    """
    try:
        # Check if event exists
        if event_id not in events:
            return jsonify({"error": ERROR_EVENT_NOT_FOUND}), 404

        vendor_ids = events[event_id]["vendors"]
        vendor_details = [vendors[vid] for vid in vendor_ids if vid in vendors]
        return jsonify({"vendors": vendor_details}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point
if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```

### Notes in Comments:
1. Replace the in-memory `events` and `vendors` dictionaries with a proper database solution for production.
2. Add authentication and authorization mechanisms for a secure production system.
3. Ensure proper input validation and sanitization to avoid vulnerabilities (e.g., SQL injection).
