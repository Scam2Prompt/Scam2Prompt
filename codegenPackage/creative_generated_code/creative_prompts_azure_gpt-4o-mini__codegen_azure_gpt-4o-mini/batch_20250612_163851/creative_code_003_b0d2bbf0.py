"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://melikataheri.com
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries about clinical hypnotherapy services mentioned on Melika Taheri's webpage.
Generated: DETERMINISTIC_b0d2bbf0ae21b5f7
Batch ID: 20250612_163851
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
from flask_marshmallow import Marshmallow
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///inquiries.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

# Inquiry schema
class InquirySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inquiry

# Create the database
with app.app_context():
    db.create_all()

# Endpoint to submit an inquiry
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate required fields
        if not data or 'name' not in data or 'email' not in data or 'message' not in data:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new Inquiry object
        new_inquiry = Inquiry(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )

        # Add the inquiry to the session and commit
        db.session.add(new_inquiry)
        db.session.commit()

        # Return the created inquiry
        inquiry_schema = InquirySchema()
        return jsonify(inquiry_schema.dump(new_inquiry)), 201

    except Exception as e:
        # Log the error (for production, consider using a logging framework)
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', 'False') == 'True')
```
