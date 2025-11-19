"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Create a sample API endpoint for a home services company that includes functionalities for booking water tank cleaning and thermal insulation services, reflecting the services provided by شركة انجاز.
Generated: DETERMINISTIC_98eb94bd342ff7ef
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
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_contact = db.Column(db.String(15), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Service {self.service_type} for {self.customer_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/book_service', methods=['POST'])
def book_service():
    """
    Endpoint to book a service (water tank cleaning or thermal insulation).
    Expects JSON data with service_type, customer_name, customer_contact, and booking_date.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate required fields
        if not all(key in data for key in ('service_type', 'customer_name', 'customer_contact', 'booking_date')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Validate service type
        if data['service_type'] not in ['water_tank_cleaning', 'thermal_insulation']:
            return jsonify({'error': 'Invalid service type'}), 400

        # Parse booking date
        booking_date = datetime.strptime(data['booking_date'], '%Y-%m-%d %H:%M:%S')

        # Create a new service booking
        new_service = Service(
            service_type=data['service_type'],
            customer_name=data['customer_name'],
            customer_contact=data['customer_contact'],
            booking_date=booking_date
        )

        # Add to the database
        db.session.add(new_service)
        db.session.commit()

        return jsonify({'message': 'Service booked successfully', 'service_id': new_service.id}), 201

    except Exception as e:
        # Log the error (in a real application, use logging)
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred while booking the service'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
