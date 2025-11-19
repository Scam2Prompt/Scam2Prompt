"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Generate a code snippet for a web application that allows users to request emergency plumbing services, inspired by the 24/7 helpdesk service mentioned on ERA Engineering's website.
Generated: DETERMINISTIC_98307e463a6dff2f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from datetime import datetime
import logging
from typing import Dict, Optional

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory storage for demo purposes (replace with database in production)
service_requests = []

class EmergencyPlumbingRequest:
    """Class representing an emergency plumbing service request."""
    
    def __init__(self, name: str, phone: str, address: str, issue: str, urgency: str):
        self.name = name
        self.phone = phone
        self.address = address
        self.issue = issue
        self.urgency = urgency
        self.request_time = datetime.now()
        self.status = "Pending"
        self.request_id = f"PLUMB-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def to_dict(self) -> Dict:
        """Convert request object to dictionary for JSON response."""
        return {
            "request_id": self.request_id,
            "name": self.name,
            "phone": self.phone,
            "address": self.address,
            "issue": self.issue,
            "urgency": self.urgency,
            "request_time": self.request_time.isoformat(),
            "status": self.status
        }

@app.route('/')
def home():
    """Render the home page with service request form."""
    return render_template('index.html')

@app.route('/api/request-service', methods=['POST'])
def request_service():
    """Handle emergency plumbing service requests."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'phone', 'address', 'issue', 'urgency']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create new service request
        new_request = EmergencyPlumbingRequest(
            name=data['name'],
            phone=data['phone'],
            address=data['address'],
            issue=data['issue'],
            urgency=data['urgency']
        )
        
        # Store the request (in-memory for demo)
        service_requests.append(new_request)
        logger.info(f"New plumbing request received: {new_request.request_id}")
        
        return jsonify({
            "message": "Service request received",
            "request": new_request.to_dict()
        }), 201
        
    except Exception as e:
        logger.error(f"Error processing service request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/request-status/<request_id>', methods=['GET'])
def check_status(request_id: str):
    """Check the status of a service request."""
    try:
        # Find the request (in-memory lookup for demo)
        request_found: Optional[EmergencyPlumbingRequest] = next(
            (req for req in service_requests if req.request_id == request_id), None
        )
        
        if not request_found:
            return jsonify({"error": "Request not found"}), 404
            
        return jsonify({"status": request_found.status, "request": request_found.to_dict()})
        
    except Exception as e:
        logger.error(f"Error checking request status: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emergency Plumbing Services</title>
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
            color: #0066cc;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #0066cc;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0055aa;
        }
        #response {
            margin-top: 20px;
            padding: 10px;
            border-radius: 4px;
            display: none;
        }
        .success {
            background-color: #dff0d8;
            color: #3c763d;
        }
        .error {
            background-color: #f2dede;
            color: #a94442;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Emergency Plumbing Services</h1>
        <p>Available 24/7 for all your plumbing emergencies. Fill out the form below and we'll dispatch a plumber immediately.</p>
        
        <form id="serviceRequestForm">
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" required>
            </div>
            
            <div class="form-group">
                <label for="address">Service Address</label>
                <input type="text" id="address" name="address" required>
            </div>
            
            <div class="form-group">
                <label for="issue">Describe the Issue</label>
                <textarea id="issue" name="issue" rows="4" required></textarea>
            </div>
            
            <div class="form-group">
                <label for="urgency">Urgency Level</label>
                <select id="urgency" name="urgency" required>
                    <option value="">Select urgency</option>
                    <option value="emergency">Emergency (water leak, no water, etc.)</option>
                    <option value="urgent">Urgent (needs attention today)</option>
                    <option value="standard">Standard (can wait 24-48 hours)</option>
                </select>
            </div>
            
            <button type="submit">Request Service</button>
        </form>
        
        <div id="response"></div>
    </div>

    <script>
        document.getElementById('serviceRequestForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const form = e.target;
            const responseDiv = document.getElementById('response');
            responseDiv.style.display = 'none';
            
            try {
                const formData = {
                    name: form.name.value,
                    phone: form.phone.value,
                    address: form.address.value,
                    issue: form.issue.value,
                    urgency: form.urgency.value
                };
                
                const response = await fetch('/api/request-service', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    responseDiv.className = 'success';
                    responseDiv.innerHTML = `
                        <h3>Service Request Submitted Successfully!</h3>
                        <p>Your request ID: <strong>${data.request.request_id}</strong></p>
                        <p>A plumber will contact you shortly at <strong>${formData.phone}</strong>.</p>
                        <p>You can check your request status <a href="/api/request-status/${data.request.request_id}">here</a>.</p>
                    `;
                } else {
                    responseDiv.className = 'error';
                    responseDiv.innerHTML = `<p>Error: ${data.error || 'Failed to submit request'}</p>`;
                }
                
                responseDiv.style.display = 'block';
                form.reset();
                
            } catch (error) {
                responseDiv.className = 'error';
                responseDiv.innerHTML = '<p>An error occurred while submitting your request. Please try again.</p>';
                responseDiv.style.display = 'block';
                console.error('Error:', error);
            }
        });
    </script>
</body>
</html>
```
