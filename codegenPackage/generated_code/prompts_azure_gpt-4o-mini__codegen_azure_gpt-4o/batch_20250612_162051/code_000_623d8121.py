"""
Generated Code Metadata:
========================
Original URL: https://dentistasuzano.com.br
Prompt: Generate a code snippet for a web application that allows users to schedule a dental consultation at Odontoclinic in Suzano, including options for WhatsApp and phone contact.
Generated: DETERMINISTIC_623d81210b1dbca4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for scheduled consultations
consultations = []

# Endpoint to schedule a dental consultation
@app.route('/schedule', methods=['POST'])
def schedule_consultation():
    try:
        # Parse request data
        data = request.json
        name = data.get('name')
        contact_method = data.get('contact_method')  # 'whatsapp' or 'phone'
        contact_info = data.get('contact_info')
        preferred_date = data.get('preferred_date')  # Expected format: 'YYYY-MM-DD'

        # Validate input
        if not name or not contact_method or not contact_info or not preferred_date:
            return jsonify({"error": "Missing required fields"}), 400

        try:
            # Validate date format
            preferred_date = datetime.strptime(preferred_date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD'."}), 400

        if contact_method not in ['whatsapp', 'phone']:
            return jsonify({"error": "Invalid contact method. Use 'whatsapp' or 'phone'."}), 400

        # Create consultation record
        consultation = {
            "id": len(consultations) + 1,
            "name": name,
            "contact_method": contact_method,
            "contact_info": contact_info,
            "preferred_date": preferred_date.strftime('%Y-%m-%d'),
            "clinic": "Odontoclinic Suzano"
        }
        consultations.append(consultation)

        # Return success response
        return jsonify({"message": "Consultation scheduled successfully", "consultation": consultation}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while scheduling the consultation", "details": str(e)}), 500

# Endpoint to list all scheduled consultations
@app.route('/consultations', methods=['GET'])
def list_consultations():
    return jsonify({"consultations": consultations}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions:
1. Install Flask: `pip install flask`
2. Run the script: `python app.py`
3. Use a tool like Postman or curl to test the endpoints:
   - POST `/schedule` with JSON payload: `{"name": "John Doe", "contact_method": "whatsapp", "contact_info": "+5511999999999", "preferred_date": "2023-10-15"}`
   - GET `/consultations` to list all scheduled consultations.
