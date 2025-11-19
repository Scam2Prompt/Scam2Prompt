"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olavovieira.com.br
Prompt: Generate a code snippet for a web application that allows users to request a Parecer Técnico de Avaliação Mercadológica (PTAM) for their property.
Generated: DETERMINISTIC_d2090e67a05efc8a
Batch ID: 20250612_161700
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
from werkzeug.exceptions import BadRequest, InternalServerError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ptam_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the database model for PTAM requests
class PTAMRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    property_address = db.Column(db.String(255), nullable=False)
    request_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<PTAMRequest {self.id} - {self.user_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/request_ptam', methods=['POST'])
def request_ptam():
    """Endpoint to request a Parecer Técnico de Avaliação Mercadológica (PTAM)"""
    try:
        # Extract data from the request
        data = request.get_json()
        user_name = data.get('user_name')
        property_address = data.get('property_address')

        # Validate input data
        if not user_name or not property_address:
            raise BadRequest("User name and property address are required.")

        # Create a new PTAM request
        new_request = PTAMRequest(user_name=user_name, property_address=property_address)
        db.session.add(new_request)
        db.session.commit()

        # Log the request creation
        logging.info(f"PTAM request created: {new_request}")

        # Return success response
        return jsonify({"message": "PTAM request submitted successfully.", "request_id": new_request.id}), 201

    except BadRequest as e:
        logging.error(f"BadRequest: {e.description}")
        return jsonify({"error": e.description}), 400
    except Exception as e:
        logging.error(f"InternalServerError: {str(e)}")
        return jsonify({"error": "An internal error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
