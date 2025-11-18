"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Suggest a framework for creating a database-driven web application, tailored to the service offerings of Fantom Internet Dienst.
Generated: DETERMINISTIC_615c03d9bae56a4b
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for the web framework and database management
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite used for simplicity, change as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fantom_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Service model for the database
class Service(db.Model):
    """Model representing a service offered by Fantom Internet Dienst."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Service {self.name}>"

# Create the database if it doesn't exist
with app.app_context():
    db.create_all()

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all services offered by Fantom Internet Dienst."""
    try:
        services = Service.query.all()
        return jsonify([{'id': service.id, 'name': service.name, 'description': service.description, 'price': service.price} for service in services])
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/services', methods=['POST'])
def add_service():
    """Add a new service to the database."""
    try:
        data = request.get_json()
        new_service = Service(
            name=data['name'],
            description=data['description'],
            price=data['price']
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify({'message': 'Service added successfully!'}), 201
    except (SQLAlchemyError, KeyError) as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing service by its ID."""
    try:
        service = Service.query.get_or_404(service_id)
        data = request.get_json()
        
        service.name = data.get('name', service.name)
        service.description = data.get('description', service.description)
        service.price = data.get('price', service.price)

        db.session.commit()
        return jsonify({'message': 'Service updated successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a service by its ID."""
    try:
        service = Service.query.get_or_404(service_id)
        db.session.delete(service)
        db.session.commit()
        return jsonify({'message': 'Service deleted successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
```
