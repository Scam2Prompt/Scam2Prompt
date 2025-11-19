"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atvisaabogados.com
Prompt: Develop a RESTful API endpoint that allows users to schedule consultations for immigration services, similar to the booking system described on AT Visa Abogados.
Generated: DETERMINISTIC_c51d18ac073c50d0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a RESTful API endpoint to schedule consultations for immigration services using Python's Flask framework:

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# In-memory storage for scheduled consultations
consultations = []

# Error handling decorator
def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return wrapper

@app.route('/schedule-consultation', methods=['POST'])
@handle_errors
def schedule_consultation():
    """
    Endpoint to schedule a consultation.
    Request Body:
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
            "date": "2023-10-25",
            "time": "14:00"
        }
    Response:
        {
            "message": "Consultation scheduled successfully!",
            "consultation_id": 1
        }
    """
    # Parse incoming JSON request
    data = request.get_json()

    # Validate required fields
    required_fields = ["name", "email", "phone", "date", "time"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"'{field}' is required."}), 400

    try:
        # Validate date and time formats
        consultation_date = datetime.datetime.strptime(data['date'], '%Y-%m-%d').date()
        consultation_time = datetime.datetime.strptime(data['time'], '%H:%M').time()
    except ValueError:
        return jsonify({"error": "Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time."}), 400

    # Create a new consultation entry
    consultation_id = len(consultations) + 1
    consultation = {
        "id": consultation_id,
        "name": data["name"],
        "email": data["email"],
        "phone": data["phone"],
        "date": str(consultation_date),
        "time": str(consultation_time)
    }

    # Add to the in-memory storage
    consultations.append(consultation)

    # Return success response
    return jsonify({
        "message": "Consultation scheduled successfully!",
        "consultation_id": consultation_id
    }), 201

@app.route('/consultations', methods=['GET'])
@handle_errors
def get_consultations():
    """
    Endpoint to retrieve all scheduled consultations.
    Response:
        [
            {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "+1234567890",
                "date": "2023-10-25",
                "time": "14:00"
            },
            ...
        ]
    """
    return jsonify(consultations), 200

if __name__ == '__main__':
    app.run(debug=True)
```

You can use this code to create and manage consultation schedules. It includes validation, error handling, and documentation within comments. Make sure to install Flask (`pip install flask`) before running the application.
