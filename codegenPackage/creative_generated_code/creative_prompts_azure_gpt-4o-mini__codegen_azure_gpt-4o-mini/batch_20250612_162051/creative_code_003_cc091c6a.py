"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcelsolemos.com.br
Prompt: Develop an API endpoint that retrieves information about dental services such as implants and orthodontics available at Dr. Celso Lemos' clinic.
Generated: DETERMINISTIC_cc091c6ad8c3fc49
Batch ID: 20250612_162051
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

# Configure database URI (replace with your actual database configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dental_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Dental Services
class DentalService(db.Model):
    __tablename__ = 'dental_services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the DentalService instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Route to retrieve all dental services
@app.route('/api/services', methods=['GET'])
def get_services():
    """API endpoint to retrieve all dental services."""
    try:
        services = DentalService.query.all()
        return jsonify([service.to_dict() for service in services]), 200
    except SQLAlchemyError as e:
        # Log the error (in a real application, use logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'Unable to retrieve dental services'}), 500

# Route to retrieve a specific service by ID
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """API endpoint to retrieve a specific dental service by ID."""
    try:
        service = DentalService.query.get_or_404(service_id)
        return jsonify(service.to_dict()), 200
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        return jsonify({'error': 'Unable to retrieve dental service'}), 500

# Run the application
if __name__ == '__main__':
    # Create all database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Disable debug mode in production
```

> **Note:** Make sure to replace the database URI with your actual database configuration. This example uses SQLite for simplicity.
