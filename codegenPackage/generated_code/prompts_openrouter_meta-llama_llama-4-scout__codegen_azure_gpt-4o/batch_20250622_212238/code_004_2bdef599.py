"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Create a team management system for the Team Mathematics Competition using a Python library or framework, allowing schools to register teams and track student participation.
Generated: DETERMINISTIC_2bdef599548d437a
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for simplicity
schools = {}
teams = {}
students = {}

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to register a school
@app.route('/schools', methods=['POST'])
def register_school():
    data = request.json
    school_id = data.get('school_id')
    name = data.get('name')

    if not school_id or not name:
        return jsonify({"error": "Invalid input", "message": "school_id and name are required"}), 400

    if school_id in schools:
        return jsonify({"error": "Conflict", "message": "School ID already exists"}), 409

    schools[school_id] = {"name": name, "teams": []}
    return jsonify({"message": "School registered successfully"}), 201

# Route to register a team
@app.route('/teams', methods=['POST'])
def register_team():
    data = request.json
    team_id = data.get('team_id')
    school_id = data.get('school_id')
    team_name = data.get('team_name')

    if not team_id or not school_id or not team_name:
        return jsonify({"error": "Invalid input", "message": "team_id, school_id, and team_name are required"}), 400

    if team_id in teams:
        return jsonify({"error": "Conflict", "message": "Team ID already exists"}), 409

    if school_id not in schools:
        return jsonify({"error": "Not Found", "message": "School ID does not exist"}), 404

    teams[team_id] = {"school_id": school_id, "team_name": team_name, "students": []}
    schools[school_id]["teams"].append(team_id)
    return jsonify({"message": "Team registered successfully"}), 201

# Route to register a student
@app.route('/students', methods=['POST'])
def register_student():
    data = request.json
    student_id = data.get('student_id')
    team_id = data.get('team_id')
    name = data.get('name')

    if not student_id or not team_id or not name:
        return jsonify({"error": "Invalid input", "message": "student_id, team_id, and name are required"}), 400

    if student_id in students:
        return jsonify({"error": "Conflict", "message": "Student ID already exists"}), 409

    if team_id not in teams:
        return jsonify({"error": "Not Found", "message": "Team ID does not exist"}), 404

    students[student_id] = {"name": name, "team_id": team_id}
    teams[team_id]["students"].append(student_id)
    return jsonify({"message": "Student registered successfully"}), 201

# Route to get school details
@app.route('/schools/<school_id>', methods=['GET'])
def get_school(school_id):
    if school_id not in schools:
        return jsonify({"error": "Not Found", "message": "School ID does not exist"}), 404

    school = schools[school_id]
    return jsonify(school), 200

# Route to get team details
@app.route('/teams/<team_id>', methods=['GET'])
def get_team(team_id):
    if team_id not in teams:
        return jsonify({"error": "Not Found", "message": "Team ID does not exist"}), 404

    team = teams[team_id]
    return jsonify(team), 200

# Route to get student details
@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Not Found", "message": "Student ID does not exist"}), 404

    student = students[student_id]
    return jsonify(student), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
