"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carthewchautaxreports.pages.dev
Prompt: Develop a RESTful API endpoint that provides information on migration law services, similar to the offerings of Carthew Chau & Co.
Generated: DETERMINISTIC_8f60525b9aba77df
Batch ID: 20250612_155455
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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# Configure SQLite database for demonstration purposes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///migration_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Migration Service model
class MigrationService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/migration-services', methods=['GET'])
def get_services():
    """Retrieve all migration law services."""
    services = MigrationService.query.all()
    return jsonify([service.to_dict() for service in services]), 200

@app.route('/api/migration-services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific migration law service by ID."""
    service = MigrationService.query.get(service_id)
    if service is None:
        raise NotFound(f'Service with ID {service_id} not found')
    return jsonify(service.to_dict()), 200

@app.route('/api/migration-services', methods=['POST'])
def create_service():
    """Create a new migration law service."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        raise BadRequest('Missing required fields: name, description, price')

    new_service = MigrationService(
        name=data['name'],
        description=data['description'],
        price=data['price']
    )
    
    db.session.add(new_service)
    db.session.commit()
    return jsonify(new_service.to_dict()), 201

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle NotFound exceptions."""
    return jsonify({'error': str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle BadRequest exceptions."""
    return jsonify({'error': str(error)}), 400

if __name__ == "__main__":
    app.run(debug=True)  # Set debug to False in production
```

### Instructions:
1. Make sure to install Flask and Flask-SQLAlchemy if you haven't already:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the code in a file, e.g., `app.py`, and run it using:
   ```bash
   python app.py
   ```
3. Use an API client like Postman to test the endpoints.
