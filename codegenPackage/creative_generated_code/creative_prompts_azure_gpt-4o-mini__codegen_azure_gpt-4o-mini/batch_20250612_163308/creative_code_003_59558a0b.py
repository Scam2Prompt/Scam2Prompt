"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Develop an API endpoint specification for a roofing service that allows clients to submit requests for inspections and estimates, including necessary parameters and response formats.
Generated: DETERMINISTIC_59558a0b22af006d
Batch ID: 20250612_163308
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roofing_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model for InspectionRequest
class InspectionRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    request_type = db.Column(db.String(50), nullable=False)  # 'inspection' or 'estimate'
    details = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'address': self.address,
            'request_type': self.request_type,
            'details': self.details,
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/roofing/requests', methods=['POST'])
def submit_request():
    """
    Submit a new inspection or estimate request.

    Request body should be in JSON format with the following structure:
    {
        "client_name": "John Doe",
        "address": "123 Main St, Anytown, USA",
        "request_type": "inspection" | "estimate",
        "details": "Additional details regarding the request"
    }

    Returns:
        JSON response with the created request data and status code.
    """
    try:
        # Validate incoming request data
        data = request.get_json()

        if not data:
            raise BadRequest("Request body must be JSON")

        client_name = data.get('client_name')
        address = data.get('address')
        request_type = data.get('request_type')
        details = data.get('details', '')

        if not client_name or not address or request_type not in ['inspection', 'estimate']:
            raise BadRequest("Missing or invalid parameters")

        # Create a new inspection request
        new_request = InspectionRequest(
            client_name=client_name,
            address=address,
            request_type=request_type,
            details=details
        )
        
        db.session.add(new_request)
        db.session.commit()

        return jsonify(new_request.to_dict()), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
