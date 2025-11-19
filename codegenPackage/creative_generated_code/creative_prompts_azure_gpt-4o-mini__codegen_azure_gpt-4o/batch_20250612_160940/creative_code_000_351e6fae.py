"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Generate a code snippet for a web application that allows users to book appointments with legal and accounting professionals, similar to the services offered by Carthew Chau & Co.
Generated: DETERMINISTIC_351e6fae52901e08
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for professionals and appointments
professionals = [
    {"id": 1, "name": "John Smith", "profession": "Lawyer"},
    {"id": 2, "name": "Jane Doe", "profession": "Accountant"},
]
appointments = []


# Endpoint to list available professionals
@app.route('/professionals', methods=['GET'])
def list_professionals():
    """
    Get a list of all available legal and accounting professionals.
    """
    return jsonify({"professionals": professionals})


# Endpoint to book an appointment
@app.route('/appointments', methods=['POST'])
def book_appointment():
    """
    Book an appointment with a professional.

    Request JSON format:
    {
        "professional_id": 1,
        "user_name": "Alice",
        "appointment_date": "2023-12-01 10:00"
    }
    """
    try:
        data = request.json

        # Validate input
        professional_id = data.get("professional_id")
        user_name = data.get("user_name")
        appointment_date_str = data.get("appointment_date")

        if not professional_id or not user_name or not appointment_date_str:
            return jsonify({"error": "Missing required fields"}), 400

        # Check if professional exists
        professional = next(
            (p for p in professionals if p["id"] == professional_id), None
        )
        if not professional:
            return jsonify({"error": "Professional not found"}), 404

        # Parse appointment date
        try:
            appointment_date = datetime.strptime(appointment_date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD HH:MM"}), 400

        # Create and store the appointment
        appointment = {
            "id": len(appointments) + 1,
            "professional_id": professional_id,
            "user_name": user_name,
            "appointment_date": appointment_date,
        }
        appointments.append(appointment)

        return jsonify({"message": "Appointment booked successfully", "appointment": appointment}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to view all appointments
@app.route('/appointments', methods=['GET'])
def view_appointments():
    """
    Get a list of all booked appointments.
    """
    return jsonify({"appointments": appointments})


# Start the Flask app
if __name__ == '__main__':
    # Run on localhost, port 5000
    app.run(debug=True)
```
