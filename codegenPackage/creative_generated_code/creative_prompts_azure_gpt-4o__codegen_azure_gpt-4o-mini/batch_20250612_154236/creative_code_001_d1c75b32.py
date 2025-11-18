"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Create a REST API that allows users to book repair services for BPL appliances, specifying the type of appliance (e.g., washing machine, microwave oven) and location (e.g., Delhi, Noida). Include endpoints for service charges and same-day repair availability.
Generated: DETERMINISTIC_d1c75b32162ae896
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///bpl_repair_services.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for the repair service bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appliance_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    service_charge = db.Column(db.Float, nullable=False)
    booking_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Booking {self.id}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/book', methods=['POST'])
def book_service():
    """
    Endpoint to book a repair service for BPL appliances.
    Expects JSON data with 'appliance_type' and 'location'.
    Returns the booking confirmation with service charge.
    """
    data = request.get_json()

    if not data or 'appliance_type' not in data or 'location' not in data:
        return jsonify({'error': 'Invalid input. Please provide appliance_type and location.'}), 400

    appliance_type = data['appliance_type']
    location = data['location']

    # Example service charge logic (could be replaced with more sophisticated logic)
    service_charge = calculate_service_charge(appliance_type)

    new_booking = Booking(appliance_type=appliance_type, location=location, service_charge=service_charge)
    db.session.add(new_booking)
    db.session.commit()

    return jsonify({
        'message': 'Booking successful.',
        'booking_id': new_booking.id,
        'service_charge': service_charge
    }), 201

def calculate_service_charge(appliance_type):
    """
    Simple function to calculate service charge based on appliance type.
    """
    charges = {
        'washing_machine': 500,
        'microwave_oven': 300,
        'refrigerator': 700
    }
    return charges.get(appliance_type.lower(), 400)  # Default charge if appliance type is unknown

@app.route('/api/service-charges', methods=['GET'])
def get_service_charges():
    """
    Endpoint to retrieve service charges for different appliance types.
    Returns a dictionary of appliance types and their corresponding service charges.
    """
    charges = {
        'washing_machine': 500,
        'microwave_oven': 300,
        'refrigerator': 700
    }
    return jsonify(charges), 200

@app.route('/api/same-day-repair-availability', methods=['POST'])
def check_same_day_repair_availability():
    """
    Endpoint to check if same-day repair is available for a given location.
    Expects JSON data with 'location'.
    Returns availability status.
    """
    data = request.get_json()

    if not data or 'location' not in data:
        return jsonify({'error': 'Invalid input. Please provide a location.'}), 400

    location = data['location']
    
    # Simple logic to determine availability (this could be more complex based on actual scheduling)
    now = datetime.utcnow()
    availability_time = now + timedelta(hours=4)  # Assuming repairs can be booked at least 4 hours in advance

    is_available = True  # Placeholder logic; replace with actual scheduling logic

    return jsonify({
        'location': location,
        'same_day_repair_available': is_available,
        'available_time': availability_time.strftime('%Y-%m-%d %H:%M:%S')
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```
