"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bepretty.hamburg
Prompt: Generate a code snippet for a web application that allows users to book professional hair and makeup services, similar to the offerings at bePretty Hamburg.
Generated: DETERMINISTIC_0c56c4eb513cb600
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    service = db.relationship('Service', backref=db.backref('bookings', lazy=True))

# Error handling for database creation
try:
    db.create_all()
except Exception as e:
    print(f"Error creating database: {e}")

@app.route('/')
def index():
    """Render the homepage with the list of services."""
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/book', methods=['POST'])
def book_service():
    """Handle service booking requests."""
    try:
        service_id = request.json.get('service_id')
        date = request.json.get('date')
        customer_name = request.json.get('customer_name')

        # Validate input data
        if not service_id or not date or not customer_name:
            return jsonify({"error": "Missing required fields"}), 400

        # Create a new booking
        booking = Booking(service_id=service_id, date=datetime.fromisoformat(date), customer_name=customer_name)
        db.session.add(booking)
        db.session.commit()

        return jsonify({"message": "Booking successful", "booking_id": booking.id}), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/services', methods=['GET'])
def get_services():
    """Return a list of services."""
    try:
        services = Service.query.all()
        return jsonify([{"id": service.id, "name": service.name, "price": service.price, "description": service.description} for service in services]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: This code assumes that you have a properly set up Flask environment and you will need to create the corresponding HTML templates for rendering. Ensure that Flask and Flask-SQLAlchemy are installed in your environment.
