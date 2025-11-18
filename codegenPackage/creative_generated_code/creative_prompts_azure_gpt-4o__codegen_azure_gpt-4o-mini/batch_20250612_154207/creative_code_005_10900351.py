"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Create a REST API endpoint for a photography business that allows users to query available services (e.g., "Wedding Photography," "Maternity Shoots") and retrieve pricing information.
Generated: DETERMINISTIC_10900351419a00fb
Batch ID: 20250612_154207
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Service model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }

# Create the database and the Service table
with app.app_context():
    db.create_all()

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all available photography services and their pricing."""
    try:
        services = Service.query.all()  # Query all services
        return jsonify([service.to_dict() for service in services]), 200  # Return services as JSON
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500  # Handle database errors

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific service by its ID."""
    try:
        service = Service.query.get(service_id)  # Query service by ID
        if service is None:
            return jsonify({"error": "Service not found"}), 404  # Handle service not found
        return jsonify(service.to_dict()), 200  # Return the service as JSON
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500  # Handle database errors

if __name__ == '__main__':
    app.run(debug=True)  # Run the application with debug enabled
```
