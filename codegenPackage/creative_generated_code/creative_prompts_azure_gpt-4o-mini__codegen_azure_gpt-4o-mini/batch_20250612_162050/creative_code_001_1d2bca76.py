"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Generate a code snippet for a web application that allows users to request periodic maintenance for their diesel generators, referencing the services offered by Birlik Jeneratör.
Generated: DETERMINISTIC_1d2bca764ad21fd0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# main.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maintenance_requests.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing maintenance requests
class MaintenanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    generator_model = db.Column(db.String(100), nullable=False)
    service_frequency = db.Column(db.String(50), nullable=False)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<MaintenanceRequest {self.name}, {self.generator_model}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/request-maintenance', methods=['POST'])
def request_maintenance():
    """
    Endpoint to request periodic maintenance for diesel generators.
    Expects JSON data with user details and maintenance request information.
    """
    data = request.get_json()

    # Validate input data
    if not is_valid_request(data):
        return jsonify({'error': 'Invalid input data'}), 400

    # Create a new maintenance request
    new_request = MaintenanceRequest(
        name=data['name'],
        email=data['email'],
        generator_model=data['generator_model'],
        service_frequency=data['service_frequency']
    )

    # Add to the database
    try:
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message': 'Maintenance request submitted successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': 'Failed to submit maintenance request'}), 500

def is_valid_request(data):
    """Validate the incoming request data."""
    if not data:
        return False
    if 'name' not in data or 'email' not in data or 'generator_model' not in data or 'service_frequency' not in data:
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return False
    return True

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maintenance Request</title>
    <script>
        async function submitRequest() {
            const requestData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                generator_model: document.getElementById('generator_model').value,
                service_frequency: document.getElementById('service_frequency').value
            };

            try {
                const response = await fetch('/request-maintenance', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(requestData)
                });

                const result = await response.json();
                alert(result.message || result.error);
            } catch (error) {
                alert('An error occurred while submitting the request.');
            }
        }
    </script>
</head>
<body>
    <h1>Request Diesel Generator Maintenance</h1>
    <form onsubmit="event.preventDefault(); submitRequest();">
        <label>Name: <input type="text" id="name" required></label><br>
        <label>Email: <input type="email" id="email" required></label><br>
        <label>Generator Model: <input type="text" id="generator_model" required></label><br>
        <label>Service Frequency: <input type="text" id="service_frequency" required></label><br>
        <button type="submit">Submit Request</button>
    </form>
</body>
</html>
```
