"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nkatandiinyom.com
Prompt: Write a code snippet for a web application that facilitates conflict resolution workshops in Igbo communities, inspired by the initiatives of Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_3348f5c0f81dbb71
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store for workshops and participants (In production, use a proper database)
workshops = []
participants = []

# Error response helper function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

@app.route("/workshops", methods=["POST"])
def create_workshop():
    """
    Endpoint to create a new conflict resolution workshop.
    Expects JSON payload:
    {
        "title": "Workshop Title",
        "description": "Brief workshop description",
        "date": "YYYY-MM-DD",
        "location": "Venue of the workshop"
    }
    """
    data = request.get_json()
    if not data:
        return error_response("Invalid JSON payload")

    # Validate the required fields
    required_fields = ["title", "description", "date", "location"]
    for field in required_fields:
        if field not in data:
            return error_response(f"Missing required field: {field}")

    # Create new workshop
    workshop = {
        "id": len(workshops) + 1,
        "title": data["title"],
        "description": data["description"],
        "date": data["date"],
        "location": data["location"]
    }
    workshops.append(workshop)

    return jsonify({"message": "Workshop created successfully", "workshop": workshop}), 201


@app.route("/workshops", methods=["GET"])
def list_workshops():
    """
    Endpoint to list all conflict resolution workshops.
    """
    return jsonify({"workshops": workshops}), 200


@app.route("/participants", methods=["POST"])
def register_participant():
    """
    Endpoint to register a participant to a workshop.
    Expects JSON payload:
    {
        "name": "Participant Name",
        "contact": "Participant Contact",
        "workshop_id": ID of the workshop the participant is registering for
    }
    """
    data = request.get_json()
    if not data:
        return error_response("Invalid JSON payload")

    # Validate the required fields
    required_fields = ["name", "contact", "workshop_id"]
    for field in required_fields:
        if field not in data:
            return error_response(f"Missing required field: {field}")

    # Check if workshop exists
    workshop = next((w for w in workshops if w["id"] == data["workshop_id"]), None)
    if not workshop:
        return error_response("Workshop not found", 404)

    # Register participant
    participant = {
        "id": len(participants) + 1,
        "name": data["name"],
        "contact": data["contact"],
        "workshop_id": data["workshop_id"]
    }
    participants.append(participant)

    return jsonify({"message": "Participant registered successfully", "participant": participant}), 201


@app.route("/participants/<int:workshop_id>", methods=["GET"])
def list_participants(workshop_id):
    """
    Endpoint to list all participants for a specific workshop.
    """
    # Filter participants by workshop_id
    workshop_participants = [p for p in participants if p["workshop_id"] == workshop_id]
    
    # Check if workshop exists
    workshop = next((w for w in workshops if w["id"] == workshop_id), None)
    if not workshop:
        return error_response("Workshop not found", 404)

    return jsonify({"workshop": workshop, "participants": workshop_participants}), 200


# Run the application
if __name__ == "__main__":
    # Production-ready applications should use a production-grade WSGI server like Gunicorn
    app.run(debug=True)  # Debug mode should be disabled in production
```
