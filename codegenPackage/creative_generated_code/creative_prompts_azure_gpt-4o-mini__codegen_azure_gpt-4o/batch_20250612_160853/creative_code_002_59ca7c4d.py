"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://utkutantoglu.com
Prompt: Describe how to implement a consultation scheduling API for a clinic specializing in obesity and metabolic surgery, including features for multiple languages like Turkish and English.
Generated: DETERMINISTIC_59ca7c4d12ee95ce
Batch ID: 20250612_160853
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
import json

app = Flask(__name__)

# In-memory database for demonstration purposes
appointments = []

# Supported languages
LANGUAGES = ["en", "tr"]

# Error messages for different languages
ERROR_MESSAGES = {
    "en": {
        "missing_field": "Missing required field.",
        "invalid_date": "Invalid date format. Use YYYY-MM-DD.",
        "appointment_exists": "Appointment already exists for the selected time slot.",
        "not_found": "Appointment not found.",
        "language_not_supported": "Language not supported."
    },
    "tr": {
        "missing_field": "Gerekli alan eksik.",
        "invalid_date": "Geçersiz tarih formatı. YYYY-AA-GG kullanın.",
        "appointment_exists": "Seçilen zaman diliminde zaten bir randevu var.",
        "not_found": "Randevu bulunamadı.",
        "language_not_supported": "Dil desteklenmiyor."
    }
}

# Helper function to get error message based on language
def get_error_message(language, key):
    if language not in LANGUAGES:
        language = "en"
    return ERROR_MESSAGES.get(language, {}).get(key, "Unknown error.")

@app.route("/schedule", methods=["POST"])
def schedule_appointment():
    """
    Endpoint to schedule a new appointment.
    Request should contain:
        - name: Name of the patient
        - contact: Contact information
        - date: Appointment date in YYYY-MM-DD format
        - language: Response language ('en' for English, 'tr' for Turkish)
    """
    data = request.json
    language = data.get("language", "en")
    
    # Validate language
    if language not in LANGUAGES:
        return jsonify({"error": get_error_message(language, "language_not_supported")}), 400
    
    # Validate required fields
    if not all(field in data for field in ["name", "contact", "date"]):
        return jsonify({"error": get_error_message(language, "missing_field")}), 400
    
    # Validate date format
    try:
        appointment_date = datetime.strptime(data["date"], "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": get_error_message(language, "invalid_date")}), 400
    
    # Check for conflicts
    for appointment in appointments:
        if appointment["date"] == data["date"]:
            return jsonify({"error": get_error_message(language, "appointment_exists")}), 400
    
    # Schedule the appointment
    appointment = {
        "id": len(appointments) + 1,
        "name": data["name"],
        "contact": data["contact"],
        "date": data["date"]
    }
    appointments.append(appointment)
    return jsonify({"message": "Appointment scheduled successfully.", "appointment": appointment}), 201

@app.route("/appointments", methods=["GET"])
def list_appointments():
    """
    Endpoint to list all appointments.
    Accepts 'language' in query parameters for response language.
    """
    language = request.args.get("language", "en")
    
    # Validate language
    if language not in LANGUAGES:
        return jsonify({"error": get_error_message(language, "language_not_supported")}), 400

    return jsonify({"appointments": appointments}), 200

@app.route("/appointment/<int:appointment_id>", methods=["DELETE"])
def delete_appointment(appointment_id):
    """
    Endpoint to delete an appointment by ID.
    Accepts 'language' in query parameters for response language.
    """
    language = request.args.get("language", "en")
    
    # Validate language
    if language not in LANGUAGES:
        return jsonify({"error": get_error_message(language, "language_not_supported")}), 400
    
    # Find and delete the appointment
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            appointments.remove(appointment)
            return jsonify({"message": "Appointment deleted successfully."}), 200
    
    return jsonify({"error": get_error_message(language, "not_found")}), 404

if __name__ == "__main__":
    app.run(debug=True)
```
