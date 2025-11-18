"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Provide an example of a REST API endpoint for retrieving available time slots for medical exams offered by Gastrolife, such as teste de hidrogênio expirado and retossigmoidoscopia.
Generated: DETERMINISTIC_58e08a885fc6dff7
Batch ID: 20250612_151301
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

# Sample data for available time slots
TIME_SLOTS = {
    "teste_de_hidrogenio_expirado": [
        {"date": "2023-10-20", "time": "10:00"},
        {"date": "2023-10-21", "time": "14:00"},
        {"date": "2023-10-22", "time": "09:00"},
    ],
    "retossigmoidoscopia": [
        {"date": "2023-10-20", "time": "15:00"},
        {"date": "2023-10-21", "time": "10:00"},
        {"date": "2023-10-22", "time": "11:00"},
    ],
}

@app.route('/api/v1/time-slots', methods=['GET'])
def get_time_slots():
    """
    REST API endpoint for retrieving available medical exam time slots.
    Query Parameters:
        exam_type: The type of medical exam (e.g., 'teste_de_hidrogenio_expirado', 'retossigmoidoscopia')
    Returns:
        JSON object containing available time slots for the specified exam type.
    """
    try:
        # Get exam type from query parameters
        exam_type = request.args.get('exam_type')
        
        if not exam_type:
            return jsonify({
                "error": "Missing required query parameter: 'exam_type'"
            }), 400

        # Check if exam type exists in the available time slots
        if exam_type not in TIME_SLOTS:
            return jsonify({
                "error": f"Exam type '{exam_type}' not found. Available exam types: {list(TIME_SLOTS.keys())}"
            }), 404

        # Retrieve and return the available time slots for the specified exam type
        return jsonify({
            "exam_type": exam_type,
            "available_time_slots": TIME_SLOTS[exam_type]
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "error": "An unexpected error occurred.",
            "details": str(e)
        }), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
