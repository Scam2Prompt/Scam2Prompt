"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: How can I design an event management API that supports member-only meetups for a community like Sync Connects?
Generated: DETERMINISTIC_4eb01f292237d1e8
Batch ID: 20250612_163706
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

# In-memory database (for simplicity)
events = {}
members = set()  # List of authorized member emails

# Util function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Sample member initialization (in a real application, this would likely come from a database)
members.update(["member1@example.com", "member2@example.com"])

@app.route("/events", methods=["POST"])
def create_event():
    """
    Create a new event.
    Only authorized members can create events.
    """
    try:
        data = request.json
        creator_email = data.get("creator_email")
        
        # Validate member authorization
        if creator_email not in members:
            return jsonify({"error": "Unauthorized member"}), 403
        
        # Validate input data
        event_name = data.get("name")
        event_date = data.get("date")
        if not event_name or not event_date:
            return jsonify({"error": "Missing required fields"}), 400

        # Validate date format
        try:
            event_date = datetime.strptime(event_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'"}), 400

        # Create and store event
        event_id = generate_id()
        events[event_id] = {
            "id": event_id,
            "name": event_name,
            "date": event_date,
            "creator_email": creator_email,
        }
        return jsonify({"message": "Event created successfully", "event": events[event_id]}), 201

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route("/events", methods=["GET"])
def list_events():
    """
    List all events.
    Only authorized members can view events.
    """
    try:
        member_email = request.args.get("email")

        # Validate member authorization
        if member_email not in members:
            return jsonify({"error": "Unauthorized member"}), 403

        return jsonify({"events": list(events.values())}), 200

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    """
    Get details of a specific event.
    Only authorized members can view event details.
    """
    try:
        member_email = request.args.get("email")

        # Validate member authorization
        if member_email not in members:
            return jsonify({"error": "Unauthorized member"}), 403

        event = events.get(event_id)
        if not event:
            return jsonify({"error": "Event not found"}), 404

        return jsonify(event), 200

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route("/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    """
    Delete a specific event.
    Only the creator of the event can delete it.
    """
    try:
        data = request.json
        requester_email = data.get("email")

        # Validate member authorization
        if requester_email not in members:
            return jsonify({"error": "Unauthorized member"}), 403

        event = events.get(event_id)
        if not event:
            return jsonify({"error": "Event not found"}), 404

        # Check if requester is the creator
        if event["creator_email"] != requester_email:
            return jsonify({"error": "Permission denied"}), 403

        # Delete event
        del events[event_id]
        return jsonify({"message": "Event deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route("/members", methods=["POST"])
def add_member():
    """
    Add a new member to the community.
    """
    try:
        data = request.json
        new_member_email = data.get("email")

        if not new_member_email:
            return jsonify({"error": "Email is required"}), 400

        if new_member_email in members:
            return jsonify({"error": "Member already exists"}), 400

        members.add(new_member_email)
        return jsonify({"message": "Member added successfully"}), 201

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route("/members", methods=["GET"])
def list_members():
    """
    List all members of the community.
    """
    try:
        return jsonify({"members": list(members)}), 200

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
