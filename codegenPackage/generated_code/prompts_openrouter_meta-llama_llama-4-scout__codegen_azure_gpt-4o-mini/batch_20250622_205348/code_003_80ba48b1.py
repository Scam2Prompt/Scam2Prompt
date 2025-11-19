"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Develop an API for retrieving dental service information from a database, including services like dental implants, veneers, and teeth whitening, as offered by Buford Dental.
Generated: DETERMINISTIC_80ba48b17d4b9639
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///buford_dental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    __tablename__ = 'services'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Service object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/services', methods=['GET'])
def get_services():
    """Retrieve all dental services from the database."""
    try:
        services = Service.query.all()
        return jsonify([service.to_dict() for service in services]), 200
    except SQLAlchemyError as e:
        # Log the error (in production, use a logging framework)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while retrieving services.'}), 500

@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific dental service by its ID."""
    try:
        service = Service.query.get(service_id)
        if service is None:
            return jsonify({'error': 'Service not found.'}), 404
        return jsonify(service.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error (in production, use a logging framework)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while retrieving the service.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to replace the database URI with your actual database connection string and install the required packages (`Flask` and `Flask-SQLAlchemy`) before running the code.
