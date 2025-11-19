"""
Generated Code Metadata:
========================
Original URL: https://atwg.xyz
Prompt: Create a REST API that facilitates seamless communication for a call center, inspired by ATWG LTD's customer support model.
Generated: DETERMINISTIC_3b0d0c6e6e273736
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///call_center.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Call Center Model
class Call(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    issue_description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, customer_name, issue_description):
        self.customer_name = customer_name
        self.issue_description = issue_description

# Call Schema
class CallSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Call

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new call
@app.route('/api/calls', methods=['POST'])
def create_call():
    try:
        # Get JSON data from request
        data = request.get_json()
        customer_name = data.get('customer_name')
        issue_description = data.get('issue_description')

        # Validate input
        if not customer_name or not issue_description:
            return jsonify({'error': 'Customer name and issue description are required.'}), 400

        # Create a new call
        new_call = Call(customer_name, issue_description)
        db.session.add(new_call)
        db.session.commit()

        # Return the created call
        return CallSchema().jsonify(new_call), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get all calls
@app.route('/api/calls', methods=['GET'])
def get_calls():
    try:
        calls = Call.query.all()
        return CallSchema(many=True).jsonify(calls), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get a specific call by ID
@app.route('/api/calls/<int:call_id>', methods=['GET'])
def get_call(call_id):
    try:
        call = Call.query.get_or_404(call_id)
        return CallSchema().jsonify(call), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to update a call
@app.route('/api/calls/<int:call_id>', methods=['PUT'])
def update_call(call_id):
    try:
        data = request.get_json()
        call = Call.query.get_or_404(call_id)

        # Update call details
        if 'customer_name' in data:
            call.customer_name = data['customer_name']
        if 'issue_description' in data:
            call.issue_description = data['issue_description']

        db.session.commit()
        return CallSchema().jsonify(call), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a call
@app.route('/api/calls/<int:call_id>', methods=['DELETE'])
def delete_call(call_id):
    try:
        call = Call.query.get_or_404(call_id)
        db.session.delete(call)
        db.session.commit()
        return jsonify({'message': 'Call deleted successfully.'}), 204

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```
