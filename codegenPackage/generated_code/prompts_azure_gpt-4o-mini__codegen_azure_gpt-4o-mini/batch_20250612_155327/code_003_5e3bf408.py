"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Create a sample API endpoint for a CRM system that manages customer inquiries, based on the application development services offered by MDA Tech Sys.
Generated: DETERMINISTIC_5e3bf408da60a8b9
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Inquiry object to a dictionary."""
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'email': self.email,
            'message': self.message
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    """Create a new customer inquiry."""
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ('customer_name', 'email', 'message')):
            return jsonify({'error': 'Invalid input'}), 400

        new_inquiry = Inquiry(
            customer_name=data['customer_name'],
            email=data['email'],
            message=data['message']
        )
        db.session.add(new_inquiry)
        db.session.commit()

        return jsonify(new_inquiry.to_dict()), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/inquiries/<int:inquiry_id>', methods=['GET'])
def get_inquiry(inquiry_id):
    """Retrieve a specific customer inquiry by ID."""
    inquiry = Inquiry.query.get(inquiry_id)
    if inquiry is None:
        return jsonify({'error': 'Inquiry not found'}), 404
    return jsonify(inquiry.to_dict()), 200

@app.route('/api/inquiries', methods=['GET'])
def get_inquiries():
    """Retrieve all customer inquiries."""
    inquiries = Inquiry.query.all()
    return jsonify([inquiry.to_dict() for inquiry in inquiries]), 200

@app.route('/api/inquiries/<int:inquiry_id>', methods=['DELETE'])
def delete_inquiry(inquiry_id):
    """Delete a specific customer inquiry by ID."""
    inquiry = Inquiry.query.get(inquiry_id)
    if inquiry is None:
        return jsonify({'error': 'Inquiry not found'}), 404

    try:
        db.session.delete(inquiry)
        db.session.commit()
        return jsonify({'message': 'Inquiry deleted successfully'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
