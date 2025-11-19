"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Create a sample API endpoint for a CRM system that manages customer inquiries, based on the application development services offered by MDA Tech Sys.
Generated: DETERMINISTIC_5e3bf408da60a8b9
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Customer Inquiry
class CustomerInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    inquiry = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'inquiry': self.inquiry
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    """Create a new customer inquiry."""
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ('name', 'email', 'inquiry')):
        return jsonify({'error': 'Invalid input data'}), 400

    # Create a new inquiry
    new_inquiry = CustomerInquiry(
        name=data['name'],
        email=data['email'],
        inquiry=data['inquiry']
    )
    
    try:
        db.session.add(new_inquiry)
        db.session.commit()
        return jsonify(new_inquiry.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Inquiry could not be processed'}), 500

@app.route('/api/inquiries/<int:inquiry_id>', methods=['GET'])
def get_inquiry(inquiry_id):
    """Retrieve a customer inquiry by ID."""
    inquiry = CustomerInquiry.query.get(inquiry_id)
    
    if inquiry is None:
        return jsonify({'error': 'Inquiry not found'}), 404
    
    return jsonify(inquiry.to_dict()), 200

@app.route('/api/inquiries/<int:inquiry_id>', methods=['DELETE'])
def delete_inquiry(inquiry_id):
    """Delete a customer inquiry by ID."""
    inquiry = CustomerInquiry.query.get(inquiry_id)
    
    if inquiry is None:
        return jsonify({'error': 'Inquiry not found'}), 404
    
    db.session.delete(inquiry)
    db.session.commit()
    
    return jsonify({'message': 'Inquiry deleted successfully'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
