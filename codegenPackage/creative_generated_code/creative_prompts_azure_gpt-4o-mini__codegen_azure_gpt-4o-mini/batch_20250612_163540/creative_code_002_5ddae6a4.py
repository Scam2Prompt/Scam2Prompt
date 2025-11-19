"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Create a REST API endpoint that allows users to submit requests for home appliance repair services, including details for washing machines and deep freezers.
Generated: DETERMINISTIC_5ddae6a42f80f8b6
Batch ID: 20250612_163540
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

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repair_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Repair Requests
class RepairRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appliance_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_contact = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'appliance_type': self.appliance_type,
            'description': self.description,
            'user_contact': self.user_contact
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/request-repair', methods=['POST'])
def request_repair():
    """
    Endpoint to submit a repair request for home appliances.
    Expected JSON payload:
    {
        "appliance_type": "washing_machine" or "deep_freezer",
        "description": "Description of the issue",
        "user_contact": "User's contact information"
    }
    """
    data = request.get_json()

    # Validate input data
    if not data or 'appliance_type' not in data or 'description' not in data or 'user_contact' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    appliance_type = data['appliance_type']
    description = data['description']
    user_contact = data['user_contact']

    # Validate appliance type
    if appliance_type not in ['washing_machine', 'deep_freezer']:
        return jsonify({'error': 'Invalid appliance type'}), 400

    # Create a new repair request
    new_request = RepairRequest(
        appliance_type=appliance_type,
        description=description,
        user_contact=user_contact
    )

    # Attempt to add the new request to the database
    try:
        db.session.add(new_request)
        db.session.commit()
        return jsonify(new_request.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/requests', methods=['GET'])
def get_requests():
    """
    Endpoint to retrieve all repair requests.
    Returns a list of all repair requests in JSON format.
    """
    requests = RepairRequest.query.all()
    return jsonify([request.to_dict() for request in requests]), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
