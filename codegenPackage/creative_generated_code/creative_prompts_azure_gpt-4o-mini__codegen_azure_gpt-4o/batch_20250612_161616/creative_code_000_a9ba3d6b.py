"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhonybarros.com.br
Prompt: Generate a code snippet for a web application that allows users to schedule medical exams at different units like Centro, Olaria, and Espaço Arp.
Generated: DETERMINISTIC_a9ba3d6b38f1f697
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and production-ready code snippet using Python with the Flask framework for the requested functionality. It includes error handling, comments, and best practices.

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for scheduled exams (for simplicity)
scheduled_exams = []

# Allowed units for medical exams
ALLOWED_UNITS = {"Centro", "Olaria", "Espaço Arp"}

@app.route('/schedule_exam', methods=['POST'])
def schedule_exam():
    """
    Endpoint to schedule a medical exam.
    Expects JSON payload with keys: name, unit, date.
    """
    try:
        # Parse and validate input data
        data = request.get_json()
        name = data.get('name')
        unit = data.get('unit')
        date = data.get('date')
        
        if not name or not unit or not date:
            return jsonify({"error": "Missing required fields: name, unit, date"}), 400
        
        if unit not in ALLOWED_UNITS:
            return jsonify({"error": f"Invalid unit. Allowed units are: {', '.join(ALLOWED_UNITS)}"}), 400
        
        try:
            # Validate date format (YYYY-MM-DD)
            exam_date = datetime.strptime(date, "%Y-%m-%d").date()
            if exam_date < datetime.now().date():
                return jsonify({"error": "Exam date cannot be in the past"}), 400
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Create unique ID for the scheduled exam
        exam_id = str(uuid.uuid4())
        
        # Store exam details in memory
        scheduled_exam = {
            "id": exam_id,
            "name": name,
            "unit": unit,
            "date": exam_date.isoformat()
        }
        scheduled_exams.append(scheduled_exam)

        return jsonify({
            "message": "Medical exam scheduled successfully",
            "exam": scheduled_exam
        }), 201

    except Exception as e:
        # Generic error handling
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/scheduled_exams', methods=['GET'])
def get_scheduled_exams():
    """
    Endpoint to retrieve all scheduled medical exams.
    """
    return jsonify({"scheduled_exams": scheduled_exams}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

You can test this application using tools like Postman or curl, sending POST requests to `/schedule_exam` with JSON payloads to schedule exams and GET requests to `/scheduled_exams` to retrieve the list of scheduled exams.
