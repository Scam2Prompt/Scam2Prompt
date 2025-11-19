"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Generate a code snippet for an online platform that facilitates Istikhara requests, incorporating features mentioned on the Darul Raza website.
Generated: DETERMINISTIC_8c6e5c218f2407c4
Batch ID: 20250612_160720
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
from werkzeug.exceptions import BadRequest
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///istikhara_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

class IstikharaRequest(db.Model):
    """Model representing an Istikhara request."""
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    request_details = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<IstikharaRequest {self.user_name}>'

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/request_istikhara', methods=['POST'])
def request_istikhara():
    """Endpoint to submit an Istikhara request."""
    try:
        data = request.get_json()

        # Validate input data
        user_name = data.get('user_name')
        request_details = data.get('request_details')
        
        if not user_name or not request_details:
            raise BadRequest("Both 'user_name' and 'request_details' are required.")
        
        # Create a new Istikhara request
        new_request = IstikharaRequest(
            user_name=user_name,
            request_details=request_details,
            created_at=db.func.current_timestamp()
        )

        db.session.add(new_request)
        db.session.commit()

        logging.info(f"Istikhara request created for {user_name}.")
        return jsonify({'message': 'Istikhara request submitted successfully!'}), 201

    except BadRequest as e:
        logging.error(f"Bad Request: {str(e)}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

@app.route('/get_requests', methods=['GET'])
def get_requests():
    """Endpoint to retrieve all Istikhara requests."""
    try:
        requests = IstikharaRequest.query.all()
        results = [
            {
                'user_name': req.user_name,
                'request_details': req.request_details,
                'created_at': req.created_at
            } for req in requests
        ]
        return jsonify(results), 200
    except Exception as e:
        logging.error(f"An error occurred while retrieving requests: {str(e)}")
        return jsonify({'error': 'Unable to retrieve requests at this time.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
