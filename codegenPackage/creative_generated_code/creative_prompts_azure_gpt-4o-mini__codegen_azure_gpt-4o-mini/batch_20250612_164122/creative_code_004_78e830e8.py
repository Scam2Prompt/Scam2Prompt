"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://handyfix.co.nz
Prompt: Suggest an API that could be used to manage bookings for handyman services in Wellington, incorporating features like availability and service categorization as described by Handyfix.
Generated: DETERMINISTIC_78e830e82408498d
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///handyman_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Logger configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Model for Service Categories
class ServiceCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f'<ServiceCategory {self.name}>'

# Model for Bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_category_id = db.Column(db.Integer, db.ForeignKey('service_category.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='Pending')

    service_category = db.relationship('ServiceCategory', backref='bookings')

    def __repr__(self):
        return f'<Booking {self.id} - {self.customer_name} for {self.service_category.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get available service categories
@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = ServiceCategory.query.all()
    return jsonify([{'id': cat.id, 'name': cat.name} for cat in categories]), 200

# Endpoint to create a new booking
@app.route('/api/bookings', methods=['POST'])
def create_booking():
    data = request.json
    try:
        customer_name = data['customer_name']
        service_category_id = data['service_category_id']
        date_time = datetime.fromisoformat(data['date_time'])

        # Check for availability (this is a basic example; real check would be more complex)
        if date_time < datetime.now():
            raise ValueError('Cannot book in the past.')

        new_booking = Booking(customer_name=customer_name, service_category_id=service_category_id, date_time=date_time)
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Booking created successfully!', 'booking_id': new_booking.id}), 201

    except KeyError as e:
        logger.error(f'Missing key: {e}')
        return jsonify({'error': 'Missing required field.'}), 400
    except ValueError as e:
        logger.error(f'Value error: {e}')
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f'Error creating booking: {e}')
        return jsonify({'error': 'Failed to create booking.'}), 500

# Endpoint to get bookings
@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return jsonify([{
        'id': booking.id,
        'customer_name': booking.customer_name,
        'service_category': booking.service_category.name,
        'date_time': booking.date_time.isoformat(),
        'status': booking.status
    } for booking in bookings]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
