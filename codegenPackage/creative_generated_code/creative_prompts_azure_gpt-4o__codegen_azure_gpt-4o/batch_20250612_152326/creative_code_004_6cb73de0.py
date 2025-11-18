"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Write code using Flask or Django to create a backend system for managing vendor applications for a festival, including booth assignments and application statuses.
Generated: DETERMINISTIC_6cb73de013a9a7a7
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and production-ready implementation using Flask. The code includes vendor application management, booth assignments, and application statuses.

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configurations for the application and the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///festival.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class VendorApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each application
    name = db.Column(db.String(100), nullable=False)  # Vendor name
    email = db.Column(db.String(100), nullable=False, unique=True)  # Vendor email
    phone = db.Column(db.String(20), nullable=False)  # Vendor phone number
    booth_number = db.Column(db.Integer, nullable=True)  # Booth assignment (optional)
    status = db.Column(db.String(20), default='Pending')  # Application status: Pending, Approved, or Rejected

    def to_dict(self):
        """Convert the database object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'booth_number': self.booth_number,
            'status': self.status
        }

# Routes
@app.route('/applications', methods=['POST'])
def create_application():
    """Create a new vendor application."""
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        if not name or not email or not phone:
            return jsonify({'error': 'Name, email, and phone are required fields.'}), 400

        application = VendorApplication(name=name, email=email, phone=phone)
        db.session.add(application)
        db.session.commit()

        return jsonify({'message': 'Application submitted successfully.', 'application': application.to_dict()}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'An application with this email already exists.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/applications', methods=['GET'])
def list_applications():
    """List all vendor applications."""
    try:
        applications = VendorApplication.query.all()
        return jsonify({'applications': [app.to_dict() for app in applications]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    """Update an application status or booth assignment."""
    try:
        application = VendorApplication.query.get(application_id)
        if not application:
            return jsonify({'error': 'Application not found.'}), 404

        data = request.json
        status = data.get('status')
        booth_number = data.get('booth_number')

        # Update application fields
        if status:
            application.status = status
        if booth_number:
            application.booth_number = booth_number

        db.session.commit()
        return jsonify({'message': 'Application updated successfully.', 'application': application.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/applications/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    """Delete a vendor application."""
    try:
        application = VendorApplication.query.get(application_id)
        if not application:
            return jsonify({'error': 'Application not found.'}), 404

        db.session.delete(application)
        db.session.commit()
        return jsonify({'message': 'Application deleted successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This Flask application provides a backend API for vendor application management, including:

1. Creating new applications (`POST /applications`)
2. Listing all applications (`GET /applications`)
3. Updating application status or booth assignment (`PUT /applications/<id>`)
4. Deleting applications (`DELETE /applications/<id>`)

Ensure you install Flask and SQLAlchemy (`pip install flask flask-sqlalchemy`) to run this code.
