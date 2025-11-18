"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tpcontact.co.za
Prompt: Develop a tool to schedule consultations with MoveUp.co.za for South Africans seeking assistance with UK visa applications.
Generated: DETERMINISTIC_bfc19d5190b22968
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for consultations (in production, use a database)
consultations = []

# Available consultation slots (for demonstration purposes)
AVAILABLE_SLOTS = [
    {"date": "2023-10-15", "time": "10:00"},
    {"date": "2023-10-15", "time": "14:00"},
    {"date": "2023-10-16", "time": "11:00"},
    {"date": "2023-10-16", "time": "15:00"},
]

# Helper function to validate consultation slot
def is_valid_slot(date, time):
    for slot in AVAILABLE_SLOTS:
        if slot["date"] == date and slot["time"] == time:
            return True
    return False

# Route to view available slots
@app.route('/consultations/slots', methods=['GET'])
def get_available_slots():
    """
    Endpoint to fetch all available consultation slots.

    Returns:
        JSON response with a list of available slots.
    """
    return jsonify({"available_slots": AVAILABLE_SLOTS}), 200

# Route to schedule a consultation
@app.route('/consultations/schedule', methods=['POST'])
def schedule_consultation():
    """
    Endpoint to schedule a consultation.

    Request Body:
        {
            "name": "Full Name",
            "email": "example@example.com",
            "date": "YYYY-MM-DD",
            "time": "HH:MM"
        }

    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse request data
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        date = data.get("date")
        time = data.get("time")

        # Validate input
        if not all([name, email, date, time]):
            return jsonify({"error": "Missing required fields"}), 400

        if not is_valid_slot(date, time):
            return jsonify({"error": "Selected slot is not available"}), 400

        # Save consultation
        consultation = {
            "name": name,
            "email": email,
            "date": date,
            "time": time,
            "scheduled_at": datetime.datetime.now().isoformat(),
        }
        consultations.append(consultation)

        # Remove the slot from available slots
        AVAILABLE_SLOTS.remove({"date": date, "time": time})

        return jsonify({"message": "Consultation scheduled successfully", "consultation": consultation}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while scheduling consultation", "details": str(e)}), 500

# Route to view scheduled consultations
@app.route('/consultations', methods=['GET'])
def get_consultations():
    """
    Endpoint to fetch all scheduled consultations.

    Returns:
        JSON response with a list of scheduled consultations.
    """
    return jsonify({"consultations": consultations}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
