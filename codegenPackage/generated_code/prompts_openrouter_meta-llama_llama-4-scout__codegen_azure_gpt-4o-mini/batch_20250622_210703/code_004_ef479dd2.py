"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: "Create a RESTful API endpoint to retrieve information about eControl SA's electrical services, including their areas of expertise, such as electrical studies and projects, and security installations."
Generated: DETERMINISTIC_ef479dd2000c1a37
Batch ID: 20250622_210703
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

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert the Service object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/services', methods=['GET'])
def get_services():
    """Retrieve all electrical services offered by eControl SA."""
    try:
        services = Service.query.all()
        return jsonify([service.to_dict() for service in services]), 200
    except SQLAlchemyError as e:
        # Log the error (in a real application, use logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while retrieving services.'}), 500

@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Retrieve a specific service by its ID."""
    try:
        service = Service.query.get(service_id)
        if service is None:
            return jsonify({'error': 'Service not found.'}), 404
        return jsonify(service.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error (in a real application, use logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while retrieving the service.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to install the required packages before running the code:

```bash
pip install Flask Flask-SQLAlchemy
```

This code sets up a simple RESTful API using Flask to retrieve information about electrical services. The database is configured to use SQLite for demonstration purposes. Adjust the database URI and models as needed for your production environment.
