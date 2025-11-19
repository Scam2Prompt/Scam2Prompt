"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://förderohr.de
Prompt: Generate a code snippet for a web application that allows users to schedule a 24/7 emergency plumbing service for clogged drains in Hamburg, referencing the services offered by ElbeRohr.
Generated: DETERMINISTIC_b168bbe49ac8be8c
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify
from datetime import datetime
import re

app = Flask(__name__)

# Mock database for scheduled services
scheduled_services = []

# Utility function to validate phone numbers (Assuming German phone number format)
def is_valid_phone_number(phone_number):
    return re.match(r'^\+49\d{10,13}$', phone_number) is not None

# Endpoint to schedule emergency plumbing service
@app.route('/schedule', methods=['POST'])
def schedule_service():
    try:
        # Extract request data
        data = request.json
        name = data.get('name')
        phone_number = data.get('phone_number')
        address = data.get('address')
        preferred_datetime = data.get('preferred_datetime')

        # Validate input data
        if not name or not phone_number or not address or not preferred_datetime:
            return jsonify({'error': 'All fields (name, phone_number, address, preferred_datetime) are required.'}), 400
        
        if not is_valid_phone_number(phone_number):
            return jsonify({'error': 'Invalid phone number format. Provide a valid German phone number with country code (+49).'}), 400
        
        try:
            service_datetime = datetime.strptime(preferred_datetime, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM:SS.'}), 400

        # Save the booking
        service_entry = {
            'name': name,
            'phone_number': phone_number,
            'address': address,
            'preferred_datetime': service_datetime.strftime('%Y-%m-%d %H:%M:%S'),
            'service': 'Emergency Plumbing for Clogged Drains - ElbeRohr Hamburg'
        }
        scheduled_services.append(service_entry)

        return jsonify({'message': 'Service scheduled successfully.', 'service_details': service_entry}), 201

    except Exception as e:
        # General error handling
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**Instructions for running the code:**
1. Install Flask using `pip install flask`.
2. Save the code in a file named `app.py`.
3. Run the application with `python app.py`.
4. Use a tool like Postman or curl to test the endpoint:
   - POST `/schedule` with JSON body:
     ```json
     {
       "name": "John Doe",
       "phone_number": "+4915123456789",
       "address": "Hamburg Street 123",
       "preferred_datetime": "2023-10-01 14:30:00"
     }
     ```
   - GET `/health` to check app status.
