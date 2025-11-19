"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Generate a code snippet for a web application that allows users to request periodic maintenance for their diesel generators, referencing the services offered by Birlik Jeneratör.
Generated: DETERMINISTIC_1d2bca764ad21fd0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta
import logging
from typing import Dict, Optional

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock database for demonstration purposes
maintenance_requests_db = []

class MaintenanceRequest:
    """Class representing a maintenance request for a diesel generator."""
    
    def __init__(self, customer_name: str, generator_model: str, generator_serial: str, 
                 service_type: str, frequency: str, contact_email: str, 
                 next_service_date: Optional[datetime] = None):
        """
        Initialize a maintenance request.
        
        Args:
            customer_name: Name of the customer
            generator_model: Model of the generator
            generator_serial: Serial number of the generator
            service_type: Type of service requested
            frequency: How often maintenance should be performed
            contact_email: Customer's contact email
            next_service_date: When the next service is due (calculated if None)
        """
        self.customer_name = customer_name
        self.generator_model = generator_model
        self.generator_serial = generator_serial
        self.service_type = service_type
        self.frequency = frequency
        self.contact_email = contact_email
        self.request_date = datetime.now()
        self.next_service_date = next_service_date or self._calculate_next_service_date()
        
    def _calculate_next_service_date(self) -> datetime:
        """Calculate the next service date based on frequency."""
        frequency_map = {
            'weekly': timedelta(weeks=1),
            'monthly': timedelta(days=30),
            'quarterly': timedelta(days=90),
            'yearly': timedelta(days=365)
        }
        return datetime.now() + frequency_map.get(self.frequency.lower(), timedelta(days=30))
    
    def to_dict(self) -> Dict:
        """Convert the maintenance request to a dictionary."""
        return {
            'customer_name': self.customer_name,
            'generator_model': self.generator_model,
            'generator_serial': self.generator_serial,
            'service_type': self.service_type,
            'frequency': self.frequency,
            'contact_email': self.contact_email,
            'request_date': self.request_date.isoformat(),
            'next_service_date': self.next_service_date.isoformat()
        }

@app.route('/')
def home():
    """Render the home page with maintenance request form."""
    return render_template('index.html', company_name="Birlik Jeneratör")

@app.route('/api/maintenance-request', methods=['POST'])
def create_maintenance_request():
    """Handle maintenance request submission."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['customer_name', 'generator_model', 'generator_serial', 
                          'service_type', 'frequency', 'contact_email']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Create and store the request
        request_obj = MaintenanceRequest(
            customer_name=data['customer_name'],
            generator_model=data['generator_model'],
            generator_serial=data['generator_serial'],
            service_type=data['service_type'],
            frequency=data['frequency'],
            contact_email=data['contact_email']
        )
        
        maintenance_requests_db.append(request_obj)
        logger.info(f"New maintenance request created for {data['customer_name']}")
        
        return jsonify({
            'message': 'Maintenance request created successfully',
            'request': request_obj.to_dict()
        }), 201
        
    except Exception as e:
        logger.error(f"Error creating maintenance request: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500

@app.route('/api/maintenance-requests', methods=['GET'])
def get_maintenance_requests():
    """Retrieve all maintenance requests."""
    try:
        return jsonify([req.to_dict() for req in maintenance_requests_db]), 200
    except Exception as e:
        logger.error(f"Error retrieving maintenance requests: {str(e)}")
        return jsonify({'error': 'An error occurred while retrieving requests'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generator Maintenance - {{ company_name }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #2980b9;
        }
        #response-message {
            margin-top: 20px;
            padding: 10px;
            border-radius: 4px;
            display: none;
        }
        .success {
            background-color: #d4edda;
            color: #155724;
        }
        .error {
            background-color: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Diesel Generator Maintenance Request</h1>
        <p>Fill out the form below to schedule periodic maintenance for your diesel generator with {{ company_name }}.</p>
        
        <form id="maintenanceForm">
            <div class="form-group">
                <label for="customer_name">Your Name:</label>
                <input type="text" id="customer_name" name="customer_name" required>
            </div>
            
            <div class="form-group">
                <label for="generator_model">Generator Model:</label>
                <input type="text" id="generator_model" name="generator_model" required>
            </div>
            
            <div class="form-group">
                <label for="generator_serial">Generator Serial Number:</label>
                <input type="text" id="generator_serial" name="generator_serial" required>
            </div>
            
            <div class="form-group">
                <label for="service_type">Service Type:</label>
                <select id="service_type" name="service_type" required>
                    <option value="">Select a service</option>
                    <option value="Routine Maintenance">Routine Maintenance</option>
                    <option value="Oil Change">Oil Change</option>
                    <option value="Filter Replacement">Filter Replacement</option>
                    <option value="Full Inspection">Full Inspection</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="frequency">Maintenance Frequency:</label>
                <select id="frequency" name="frequency" required>
                    <option value="">Select frequency</option>
                    <option value="weekly">Weekly</option>
                    <option value="monthly">Monthly</option>
                    <option value="quarterly">Quarterly</option>
                    <option value="yearly">Yearly</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="contact_email">Email Address:</label>
                <input type="email" id="contact_email" name="contact_email" required>
            </div>
            
            <button type="submit">Submit Request</button>
        </form>
        
        <div id="response-message"></div>
    </div>

    <script>
        document.getElementById('maintenanceForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const form = e.target;
            const formData = {
                customer_name: form.customer_name.value,
                generator_model: form.generator_model.value,
                generator_serial: form.generator_serial.value,
                service_type: form.service_type.value,
                frequency: form.frequency.value,
                contact_email: form.contact_email.value
            };
            
            const responseMessage = document.getElementById('response-message');
            
            try {
                const response = await fetch('/api/maintenance-request', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
