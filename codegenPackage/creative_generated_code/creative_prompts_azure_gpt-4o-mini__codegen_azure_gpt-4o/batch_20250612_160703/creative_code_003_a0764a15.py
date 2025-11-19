"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconfoundation.online
Prompt: Describe an API that could facilitate outreach programs for children with special education needs, taking cues from the ICON Foundation's community connect initiatives.
Generated: DETERMINISTIC_a0764a150bd66474
Batch ID: 20250612_160703
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

# In-memory database for demonstration purposes
programs = []
participants = []
feedback = []

# API Root
@app.route("/", methods=["GET"])
def api_root():
    return jsonify({
        "message": "Welcome to the Outreach Program API for Special Education Needs",
        "endpoints": {
            "/programs": "Manage outreach programs",
            "/participants": "Manage participants in programs",
            "/feedback": "Submit and retrieve feedback for programs"
        }
    })


# Endpoint to manage programs
@app.route("/programs", methods=["GET", "POST"])
def manage_programs():
    if request.method == "GET":
        # Return a list of all programs
        return jsonify(programs)

    elif request.method == "POST":
        try:
            # Add a new program
            data = request.get_json()
            program = {
                "id": len(programs) + 1,
                "name": data["name"],
                "description": data["description"],
                "age_group": data["age_group"],
                "special_needs_focus": data["special_needs_focus"]
            }
            programs.append(program)
            return jsonify({"message": "Program created successfully", "program": program}), 201
        except KeyError as e:
            return jsonify({"error": f"Missing required field: {str(e)}"}), 400


# Endpoint to manage participants
@app.route("/participants", methods=["GET", "POST"])
def manage_participants():
    if request.method == "GET":
        # Return a list of all participants
        return jsonify(participants)

    elif request.method == "POST":
        try:
            # Register a new participant
            data = request.get_json()
            participant = {
                "id": len(participants) + 1,
                "name": data["name"],
                "age": data["age"],
                "needs": data["needs"],
                "program_id": data["program_id"]
            }
            # Validate program_id
            if not any(p["id"] == participant["program_id"] for p in programs):
                return jsonify({"error": "Program ID does not exist"}), 400

            participants.append(participant)
            return jsonify({"message": "Participant added successfully", "participant": participant}), 201
        except KeyError as e:
            return jsonify({"error": f"Missing required field: {str(e)}"}), 400


# Endpoint to manage feedback
@app.route("/feedback", methods=["GET", "POST"])
def manage_feedback():
    if request.method == "GET":
        # Return a list of all feedback
        return jsonify(feedback)

    elif request.method == "POST":
        try:
            # Submit feedback
            data = request.get_json()
            feedback_entry = {
                "id": len(feedback) + 1,
                "program_id": data["program_id"],
                "feedback_author": data["feedback_author"],
                "comments": data["comments"],
                "rating": data["rating"]
            }
            # Validate program_id
            if not any(p["id"] == feedback_entry["program_id"] for p in programs):
                return jsonify({"error": "Program ID does not exist"}), 400

            feedback.append(feedback_entry)
            return jsonify({"message": "Feedback submitted successfully", "feedback": feedback_entry}), 201
        except KeyError as e:
            return jsonify({"error": f"Missing required field: {str(e)}"}), 400


# Error handling for unsupported routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An internal error occurred"}), 500


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
