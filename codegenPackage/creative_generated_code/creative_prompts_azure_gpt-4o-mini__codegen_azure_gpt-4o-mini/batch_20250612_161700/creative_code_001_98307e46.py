"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Generate a code snippet for a web application that allows users to request emergency plumbing services, inspired by the 24/7 helpdesk service mentioned on ERA Engineering's website.
Generated: DETERMINISTIC_98307e463a6dff2f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emergency_plumbing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the database model for service requests
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ServiceRequest {self.id}: {self.name} - {self.description}>"

# Create the database
with app.app_context():
    db.create_all()

# Route to create a new service request
@app.route('/request', methods=['POST'])
def create_request():
    try:
        # Extract data from request
        data = request.get_json()
        
        # Validate input data
        if not all(key in data for key in ('name', 'address', 'phone', 'description')):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create a new service request instance
        new_request = ServiceRequest(
            name=data['name'],
            address=data['address'],
            phone=data['phone'],
            description=data['description']
        )
        
        # Add to the database and commit
        db.session.add(new_request)
        db.session.commit()
        
        logging.info(f"New service request created: {new_request.id}")
        return jsonify({"message": "Service request submitted successfully", "request_id": new_request.id}), 201
    except Exception as e:
        logging.error(f"Error creating service request: {e}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
