"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdefi-thedogeverse.pages.dev
Prompt: Create a roadmap visualization tool for the Dogeverse project that dynamically updates based on the phases described (Big Bang, Development, Awareness, Expansion, Cosmic Travel). Include milestones such as DEX/CEX listings and community incentives.
Generated: DETERMINISTIC_795507739e6bbe32
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Define the roadmap structure
roadmap = {
    "Big Bang": {
        "description": "Project initiation and foundational setup.",
        "milestones": [
            {"name": "Concept Design", "completed": False},
            {"name": "Team Formation", "completed": False}
        ]
    },
    "Development": {
        "description": "Building the core features and preparing launch.",
        "milestones": [
            {"name": "Smart Contract Deployment", "completed": False},
            {"name": "Website Launch", "completed": False}
        ]
    },
    "Awareness": {
        "description": "Marketing and community building.",
        "milestones": [
            {"name": "Community Incentives Program", "completed": False},
            {"name": "Social Media Campaigns", "completed": False}
        ]
    },
    "Expansion": {
        "description": "Growth through partnerships and listings.",
        "milestones": [
            {"name": "DEX Listing", "completed": False},
            {"name": "CEX Listing", "completed": False}
        ]
    },
    "Cosmic Travel": {
        "description": "Long-term sustainability and innovative ventures.",
        "milestones": [
            {"name": "Launch of Intergalactic Features", "completed": False},
            {"name": "Cross-Blockchain Integration", "completed": False}
        ]
    }
}

# Helper function to validate phase and milestone
def validate_phase_and_milestone(phase, milestone):
    if phase not in roadmap:
        return False, f"Invalid phase: {phase}"
    if not any(m['name'] == milestone for m in roadmap[phase]["milestones"]):
        return False, f"Invalid milestone: {milestone} for phase {phase}"
    return True, None

@app.route('/roadmap', methods=['GET'])
def get_roadmap():
    """
    Endpoint to retrieve the full roadmap.
    """
    return jsonify(roadmap)

@app.route('/update_milestone', methods=['POST'])
def update_milestone():
    """
    Endpoint to update the status of a milestone.
    Expects JSON payload with 'phase', 'milestone', and 'completed' status.
    """
    try:
        data = request.json
        phase = data.get("phase")
        milestone = data.get("milestone")
        completed = data.get("completed")

        # Validate inputs
        if not phase or not milestone or completed is None:
            return jsonify({"error": "Invalid input. Required fields: phase, milestone, completed"}), 400
        
        is_valid, error_message = validate_phase_and_milestone(phase, milestone)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Update milestone status
        for m in roadmap[phase]["milestones"]:
            if m["name"] == milestone:
                m["completed"] = completed
                return jsonify({"message": "Milestone updated successfully", "roadmap": roadmap})
        
        return jsonify({"error": "Milestone not found"}), 404

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/add_milestone', methods=['POST'])
def add_milestone():
    """
    Endpoint to add a new milestone to a phase.
    Expects JSON payload with 'phase' and 'milestone'.
    """
    try:
        data = request.json
        phase = data.get("phase")
        new_milestone = data.get("milestone")

        # Validate inputs
        if not phase or not new_milestone:
            return jsonify({"error": "Invalid input. Required fields: phase, milestone"}), 400
        if phase not in roadmap:
            return jsonify({"error": f"Invalid phase: {phase}"}), 400

        # Check if milestone already exists
        if any(m['name'] == new_milestone for m in roadmap[phase]["milestones"]):
            return jsonify({"error": "Milestone already exists in this phase"}), 400

        # Add new milestone
        roadmap[phase]["milestones"].append({"name": new_milestone, "completed": False})
        return jsonify({"message": "Milestone added successfully", "roadmap": roadmap})

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/phases', methods=['GET'])
def get_phases():
    """
    Endpoint to retrieve all phases.
    """
    return jsonify({"phases": list(roadmap.keys())})

@app.route('/milestones/<phase>', methods=['GET'])
def get_milestones(phase):
    """
    Endpoint to retrieve milestones for a specific phase.
    """
    if phase not in roadmap:
        return jsonify({"error": f"Invalid phase: {phase}"}), 404
    return jsonify(roadmap[phase]["milestones"])

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
