"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Develop a simple API to connect parents with Morahs and teachers in Lakewood, NJ, facilitating communication and guidance on educational choices.
Generated: DETERMINISTIC_f195cc38a3e077a5
Batch ID: 20250622_210703
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

# In-memory database simulation
parents = []
teachers = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

# Route to add a parent
@app.route('/parents', methods=['POST'])
def add_parent():
    try:
        data = request.json
        if not data or 'name' not in data or 'contact' not in data:
            return jsonify({"error": "Invalid input"}), 400
        parent = {
            "id": len(parents) + 1,
            "name": data['name'],
            "contact": data['contact']
        }
        parents.append(parent)
        return jsonify({"message": "Parent added successfully", "parent": parent}), 201
    except Exception as e:
        return handle_exception(e)

# Route to add a teacher
@app.route('/teachers', methods=['POST'])
def add_teacher():
    try:
        data = request.json
        if not data or 'name' not in data or 'contact' not in data:
            return jsonify({"error": "Invalid input"}), 400
        teacher = {
            "id": len(teachers) + 1,
            "name": data['name'],
            "contact": data['contact']
        }
        teachers.append(teacher)
        return jsonify({"message": "Teacher added successfully", "teacher": teacher}), 201
    except Exception as e:
        return handle_exception(e)

# Route to list all parents
@app.route('/parents', methods=['GET'])
def list_parents():
    return jsonify({"parents": parents}), 200

# Route to list all teachers
@app.route('/teachers', methods=['GET'])
def list_teachers():
    return jsonify({"teachers": teachers}), 200

# Route to facilitate communication between parent and teacher
@app.route('/communicate', methods=['POST'])
def communicate():
    try:
        data = request.json
        if not data or 'parent_id' not in data or 'teacher_id' not in data or 'message' not in data:
            return jsonify({"error": "Invalid input"}), 400

        parent = next((p for p in parents if p['id'] == data['parent_id']), None)
        teacher = next((t for t in teachers if t['id'] == data['teacher_id']), None)

        if not parent or not teacher:
            return jsonify({"error": "Parent or Teacher not found"}), 404

        # Simulate communication (In production, this could be an email or SMS)
        communication = {
            "parent": parent['name'],
            "teacher": teacher['name'],
            "message": data['message']
        }
        return jsonify({"message": "Communication sent successfully", "details": communication}), 200
    except Exception as e:
        return handle_exception(e)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
