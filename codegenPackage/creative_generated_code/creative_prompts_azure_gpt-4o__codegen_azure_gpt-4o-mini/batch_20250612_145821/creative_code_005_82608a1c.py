"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: Write code to optimize a sales funnel for pre-selling services and booking appointments, based on the "Click, Capture, Close" model described on the Client Fuel website.
Generated: DETERMINISTIC_82608a1c62770f37
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# In-memory storage for leads (in a real application, use a database)
leads = []

@app.route('/click', methods=['POST'])
def click():
    """
    Endpoint to handle clicks on the pre-sell service.
    Captures lead information and stores it.
    """
    data = request.json
    try:
        # Validate input data
        if not data or 'name' not in data or 'email' not in data:
            logging.error("Invalid input data")
            return jsonify({"error": "Invalid input data"}), 400
        
        # Simulate capturing a click
        lead = {
            'name': data['name'],
            'email': data['email'],
            'status': 'captured'
        }
        leads.append(lead)
        logging.info(f"Lead captured: {lead}")
        return jsonify({"message": "Lead captured successfully", "lead": lead}), 201
    
    except Exception as e:
        logging.error(f"Error capturing lead: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/capture', methods=['POST'])
def capture():
    """
    Endpoint to handle capturing additional lead information after a click.
    """
    data = request.json
    try:
        # Validate input data
        if not data or 'email' not in data or 'appointment_time' not in data:
            logging.error("Invalid input data")
            return jsonify({"error": "Invalid input data"}), 400

        # Update lead status to 'captured' with appointment details
        for lead in leads:
            if lead['email'] == data['email']:
                lead['appointment_time'] = data['appointment_time']
                lead['status'] = 'appointment booked'
                logging.info(f"Lead updated: {lead}")
                return jsonify({"message": "Lead information updated successfully", "lead": lead}), 200
        
        logging.warning("Lead not found for capture")
        return jsonify({"error": "Lead not found"}), 404

    except Exception as e:
        logging.error(f"Error capturing lead information: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/close', methods=['POST'])
def close():
    """
    Endpoint to finalize the appointment booking.
    """
    data = request.json
    try:
        # Validate input data
        if not data or 'email' not in data:
            logging.error("Invalid input data")
            return jsonify({"error": "Invalid input data"}), 400

        # Find and close the appointment
        for lead in leads:
            if lead['email'] == data['email'] and lead.get('appointment_time'):
                lead['status'] = 'closed'
                logging.info(f"Lead closed: {lead}")
                return jsonify({"message": "Appointment successfully closed", "lead": lead}), 200
        
        logging.warning("Lead not found for closing appointment")
        return jsonify({"error": "Lead not found or appointment not booked"}), 404

    except Exception as e:
        logging.error(f"Error closing appointment: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
