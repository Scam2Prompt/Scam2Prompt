"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piscorealestate.com
Prompt: Suggest a library for building a real estate management system that can handle "Održavanje higijene" and property listings like "Nekretnine Podgorica."
Generated: DETERMINISTIC_28831bbdd11eff3b
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is Python code for building a real estate management system that handles tasks like "Održavanje higijene" (hygiene maintenance) and property listings such as "Nekretnine Podgorica." The example leverages the popular `Flask` web framework for the backend, along with `SQLAlchemy` for database interactions.

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity; use PostgreSQL/MySQL in production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define the Property model (Nekretnine Podgorica)
class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert the Property object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'price': self.price,
            'description': self.description
        }

# Define the Maintenance model (Održavanje higijene)
class Maintenance(db.Model):
    __tablename__ = 'maintenance'
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pending')

    def to_dict(self):
        """Convert the Maintenance object to a dictionary."""
        return {
            'id': self.id,
            'property_id': self.property_id,
            'service_type': self.service_type,
            'date': self.date.isoformat(),
            'status': self.status
        }

# Create the database tables
@app.before_first_request
def create_tables():
    """Create tables in the database before the first request."""
    db.create_all()

# Route to list all properties
@app.route('/properties', methods=['GET'])
def get_properties():
    """Retrieve all properties from the database."""
    properties = Property.query.all()
    return jsonify([property.to_dict() for property in properties]), 200

# Route to add a new property
@app.route('/properties', methods=['POST'])
def add_property():
    """Add a new property to the database."""
    try:
        data = request.json
        new_property = Property(
            name=data['name'],
            location=data['location'],
            price=data['price'],
            description=data.get('description', '')
        )
        db.session.add(new_property)
        db.session.commit()
        return jsonify(new_property.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to list all maintenance records
@app.route('/maintenance', methods=['GET'])
def get_maintenance_records():
    """Retrieve all maintenance records from the database."""
    maintenance_records = Maintenance.query.all()
    return jsonify([maintenance.to_dict() for maintenance in maintenance_records]), 200

# Route to add a new maintenance record
@app.route('/maintenance', methods=['POST'])
def add_maintenance_record():
    """Add a new maintenance record to the database."""
    try:
        data = request.json
        new_maintenance = Maintenance(
            property_id=data['property_id'],
            service_type=data['service_type'],
            date=data['date'],
            status=data.get('status', 'Pending')
        )
        db.session.add(new_maintenance)
        db.session.commit()
        return jsonify(new_maintenance.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

# Run the application
if __name__ == '__main__':
    # Use debug=True only in development; remove it in production
    app.run(debug=True)
```

### Notes for Production:
1. Replace SQLite with a production-grade database like PostgreSQL or MySQL.
2. Add proper authentication and authorization mechanisms.
3. Use environment variables for sensitive configurations (e.g., database URI).
4. Consider adding unit tests and logging mechanisms for better maintainability.
