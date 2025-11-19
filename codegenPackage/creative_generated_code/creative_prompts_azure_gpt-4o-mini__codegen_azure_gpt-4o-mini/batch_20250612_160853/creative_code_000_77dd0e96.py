"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosario.gob.mx
Prompt: Generate a code snippet for a web application that allows users to submit requests for information access as outlined in the Rosario municipal transparency portal.
Generated: DETERMINISTIC_77dd0e965046377a
Batch ID: 20250612_160853
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

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class InfoRequest(db.Model):
    """Model representing a request for information."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    request_detail = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<InfoRequest {self.id}: {self.name}>'

@app.before_first_request
def create_tables():
    """Create database tables before the first request if they don't exist."""
    db.create_all()

@app.route('/submit_request', methods=['POST'])
def submit_request():
    """
    Endpoint to submit requests for information access.
    Expects JSON with name, email, and request_detail fields.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data or not all(key in data for key in ('name', 'email', 'request_detail')):
            return jsonify({'error': 'Invalid input data'}), 400

        # Create a new InfoRequest instance
        new_request = InfoRequest(
            name=data['name'],
            email=data['email'],
            request_detail=data['request_detail']
        )

        # Add to the session and commit
        db.session.add(new_request)
        db.session.commit()

        return jsonify({'message': 'Request submitted successfully', 'request_id': new_request.id}), 201

    except IntegrityError:
        db.session.rollback()  # Rollback in case of an error
        return jsonify({'error': 'A request with that email already exists'}), 409

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/requests', methods=['GET'])
def get_requests():
    """
    Endpoint to retrieve all submitted information requests.
    Returns a JSON list of requests.
    """
    try:
        requests = InfoRequest.query.all()
        return jsonify([{'id': req.id, 'name': req.name, 'email': req.email, 'request_detail': req.request_detail} for req in requests]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
