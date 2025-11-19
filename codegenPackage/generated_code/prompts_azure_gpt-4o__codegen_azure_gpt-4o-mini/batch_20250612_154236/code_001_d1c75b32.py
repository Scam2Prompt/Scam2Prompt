"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Create a REST API that allows users to book repair services for BPL appliances, specifying the type of appliance (e.g., washing machine, microwave oven) and location (e.g., Delhi, Noida). Include endpoints for service charges and same-day repair availability.
Generated: DETERMINISTIC_d1c75b32162ae896
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bpl_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appliance_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    service_charge = db.Column(db.Float, nullable=False)
    same_day_availability = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Service {self.appliance_type} in {self.location}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Endpoint to book a repair service
@app.route('/book_service', methods=['POST'])
def book_service():
    data = request.get_json()
    
    # Validate input data
    if not data or 'appliance_type' not in data or 'location' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    appliance_type = data['appliance_type']
    location = data['location']
    
    # Check for existing service
    service = Service.query.filter_by(appliance_type=appliance_type, location=location).first()
    
    if not service:
        return jsonify({'error': 'Service not available for the specified appliance and location'}), 404

    # Create a booking (for simplicity, we just return the service details)
    booking_details = {
        'appliance_type': service.appliance_type,
        'location': service.location,
        'service_charge': service.service_charge,
        'same_day_availability': service.same_day_availability,
        'booking_time': datetime.now().isoformat()
    }
    
    return jsonify({'message': 'Service booked successfully', 'booking_details': booking_details}), 201

# Endpoint to get service charges
@app.route('/service_charge/<appliance_type>/<location>', methods=['GET'])
def get_service_charge(appliance_type, location):
    service = Service.query.filter_by(appliance_type=appliance_type, location=location).first()
    
    if not service:
        return jsonify({'error': 'Service not found'}), 404

    return jsonify({'service_charge': service.service_charge}), 200

# Endpoint to check same-day repair availability
@app.route('/same_day_availability/<appliance_type>/<location>', methods=['GET'])
def check_same_day_availability(appliance_type, location):
    service = Service.query.filter_by(appliance_type=appliance_type, location=location).first()
    
    if not service:
        return jsonify({'error': 'Service not found'}), 404

    return jsonify({'same_day_availability': service.same_day_availability}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions to Run the Code
1. Ensure you have Python and Flask installed. You can install Flask using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the code in a file named `app.py`.
3. Run the application:
   ```bash
   python app.py
   ```
4. Use a tool like Postman or curl to interact with the API.
