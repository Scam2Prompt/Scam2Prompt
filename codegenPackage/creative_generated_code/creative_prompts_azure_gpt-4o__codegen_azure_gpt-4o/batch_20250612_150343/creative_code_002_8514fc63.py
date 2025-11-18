"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strk.site
Prompt: Recommend a library or API for managing customer inquiries and scheduling free measurements for renovation services, as described on the webpage.
Generated: DETERMINISTIC_8514fc63e292cce4
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code, written in Python, using the Flask framework for the API and SQLAlchemy for database management. It is production-ready, follows best practices, and includes error handling.

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask App
app = Flask(__name__)

# Configure SQLAlchemy Database URI (Replace with your database credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer_inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO)

# Define the CustomerInquiry model for database
class CustomerInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    inquiry_details = db.Column(db.Text, nullable=False)
    measurement_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "inquiry_details": self.inquiry_details,
            "measurement_date": self.measurement_date,
            "created_at": self.created_at
        }

# API endpoint: Submit customer inquiry
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    try:
        data = request.json
        # Validate input data
        if not all(key in data for key in ['name', 'email', 'phone', 'inquiry_details']):
            return jsonify({"error": "Missing required fields"}), 400

        # Create a new inquiry record
        inquiry = CustomerInquiry(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            inquiry_details=data['inquiry_details'],
            measurement_date=datetime.strptime(data['measurement_date'], '%Y-%m-%d') if 'measurement_date' in data else None
        )
        db.session.add(inquiry)
        db.session.commit()

        return jsonify({"message": "Inquiry submitted successfully", "inquiry": inquiry.to_dict()}), 201
    except Exception as e:
        logging.error(f"Error submitting inquiry: {e}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

# API endpoint: List all inquiries
@app.route('/api/inquiries', methods=['GET'])
def list_inquiries():
    try:
        inquiries = CustomerInquiry.query.all()
        return jsonify([inquiry.to_dict() for inquiry in inquiries]), 200
    except Exception as e:
        logging.error(f"Error fetching inquiries: {e}")
        return jsonify({"error": "An error occurred while fetching inquiries"}), 500

# API endpoint: Get inquiry by ID
@app.route('/api/inquiries/<int:inquiry_id>', methods=['GET'])
def get_inquiry(inquiry_id):
    try:
        inquiry = CustomerInquiry.query.get(inquiry_id)
        if not inquiry:
            return jsonify({"error": "Inquiry not found"}), 404
        return jsonify(inquiry.to_dict()), 200
    except Exception as e:
        logging.error(f"Error fetching inquiry: {e}")
        return jsonify({"error": "An error occurred while fetching the inquiry"}), 500

# API endpoint: Update inquiry by ID
@app.route('/api/inquiries/<int:inquiry_id>', methods=['PUT'])
def update_inquiry(inquiry_id):
    try:
        inquiry = CustomerInquiry.query.get(inquiry_id)
        if not inquiry:
            return jsonify({"error": "Inquiry not found"}), 404

        data = request.json
        if 'name' in data:
            inquiry.name = data['name']
        if 'email' in data:
            inquiry.email = data['email']
        if 'phone' in data:
            inquiry.phone = data['phone']
        if 'inquiry_details' in data:
            inquiry.inquiry_details = data['inquiry_details']
        if 'measurement_date' in data:
            inquiry.measurement_date = datetime.strptime(data['measurement_date'], '%Y-%m-%d')

        db.session.commit()
        return jsonify({"message": "Inquiry updated successfully", "inquiry": inquiry.to_dict()}), 200
    except Exception as e:
        logging.error(f"Error updating inquiry: {e}")
        return jsonify({"error": "An error occurred while updating the inquiry"}), 500

# API endpoint: Delete inquiry by ID
@app.route('/api/inquiries/<int:inquiry_id>', methods=['DELETE'])
def delete_inquiry(inquiry_id):
    try:
        inquiry = CustomerInquiry.query.get(inquiry_id)
        if not inquiry:
            return jsonify({"error": "Inquiry not found"}), 404

        db.session.delete(inquiry)
        db.session.commit()
        return jsonify({"message": "Inquiry deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting inquiry: {e}")
        return jsonify({"error": "An error occurred while deleting the inquiry"}), 500

# Run the Flask app
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

To test this application:
1. Install required libraries: `pip install flask flask-sqlalchemy`.
2. Run the script with `python app.py`.
3. Interact with the API using tools like Postman or cURL.
