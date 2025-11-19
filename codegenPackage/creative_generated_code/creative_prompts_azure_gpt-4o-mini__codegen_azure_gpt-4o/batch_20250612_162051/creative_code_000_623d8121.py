"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dentistasuzano.com.br
Prompt: Generate a code snippet for a web application that allows users to schedule a dental consultation at Odontoclinic in Suzano, including options for WhatsApp and phone contact.
Generated: DETERMINISTIC_623d81210b1dbca4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Data structure to store scheduled consultations
scheduled_consultations = []

# Define a route for scheduling consultations
@app.route('/schedule', methods=['POST'])
def schedule_consultation():
    """
    Endpoint to schedule a dental consultation.
    Users must provide their name, preferred date and time, and contact method.
    """
    try:
        # Parse the incoming JSON data
        data = request.json

        # Validate the required fields
        if 'name' not in data or 'date' not in data or 'time' not in data or 'contact_method' not in data:
            return jsonify({'error': 'Missing required fields: name, date, time, or contact_method'}), 400

        # Extract fields
        name = data['name']
        date = data['date']
        time = data['time']
        contact_method = data['contact_method']

        # Validate the contact method
        if contact_method not in ['WhatsApp', 'Phone']:
            return jsonify({'error': 'Invalid contact method. Choose either "WhatsApp" or "Phone".'}), 400

        # Validate date and time format
        try:
            consultation_datetime = datetime.strptime(f"{date} {time}", '%Y-%m-%d %H:%M')
        except ValueError:
            return jsonify({'error': 'Invalid date or time format. Use date: YYYY-MM-DD and time: HH:MM format.'}), 400

        # Add the consultation to the data structure
        consultation = {
            'name': name,
            'datetime': consultation_datetime.strftime('%Y-%m-%d %H:%M'),
            'contact_method': contact_method
        }
        scheduled_consultations.append(consultation)

        # Return a success response
        return jsonify({'message': 'Consultation scheduled successfully!', 'consultation': consultation}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

# Define a route to view all scheduled consultations
@app.route('/consultations', methods=['GET'])
def view_consultations():
    """
    Endpoint to retrieve all scheduled consultations.
    """
    return jsonify({'scheduled_consultations': scheduled_consultations}), 200

# Documentation for how to run the application
if __name__ == '__main__':
    # Run the Flask application
    # Debug mode is turned off for production
    app.run(host='0.0.0.0', port=5000, debug=False)
```

This code snippet represents a simple Flask application where users can schedule dental consultations at Odontoclinic in Suzano. Users can specify their preferred contact method (WhatsApp or phone), date, and time. The application includes error handling, validation, and best practices for production.
