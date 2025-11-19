"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries for wrought iron fences, reflecting the contact features found on baochuanco.com.
Generated: DETERMINISTIC_d9adaf7a2b6124f6
Batch ID: 20250612_160507
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///inquiries.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Inquiry {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit an inquiry for wrought iron fences.
    
    Request JSON should contain:
    - name: str
    - email: str
    - phone: str (optional)
    - message: str
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input data
        if not all(k in data for k in ("name", "email", "message")):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create a new Inquiry instance
        new_inquiry = Inquiry(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            message=data['message']
        )
        
        # Add the new inquiry to the session and commit
        db.session.add(new_inquiry)
        db.session.commit()
        
        return jsonify({"message": "Inquiry submitted successfully!"}), 201
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Inquiry could not be processed due to a database error."}), 500
    except Exception as e:
        # Handle any other exceptions
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
