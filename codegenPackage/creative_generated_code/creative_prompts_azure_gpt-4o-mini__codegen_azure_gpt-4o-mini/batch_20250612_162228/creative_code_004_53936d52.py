"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icestyle.pl
Prompt: Design an API endpoint for an online store that allows users to submit custom costume design requests, inspired by the services offered by IceStyle.pl.
Generated: DETERMINISTIC_53936d5246b2789b
Batch ID: 20250612_162228
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///costume_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the CostumeRequest model
class CostumeRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, user_name, email, description):
        self.user_name = user_name
        self.email = email
        self.description = description

# Define the schema for serialization
class CostumeRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CostumeRequest

# Initialize the schema
costume_request_schema = CostumeRequestSchema()
costume_requests_schema = CostumeRequestSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to submit a custom costume design request
@app.route('/api/costume-requests', methods=['POST'])
def submit_costume_request():
    # Get data from the request
    user_name = request.json.get('user_name')
    email = request.json.get('email')
    description = request.json.get('description')

    # Basic validation
    if not user_name or not email or not description:
        return jsonify({'error': 'All fields are required.'}), 400

    # Create a new costume request
    new_request = CostumeRequest(user_name=user_name, email=email, description=description)

    try:
        # Add and commit the new request to the database
        db.session.add(new_request)
        db.session.commit()
        return costume_request_schema.jsonify(new_request), 201
    except IntegrityError:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'error': 'Could not process your request. Please try again.'}), 500

# API endpoint to get all costume requests (for admin or internal use)
@app.route('/api/costume-requests', methods=['GET'])
def get_costume_requests():
    requests = CostumeRequest.query.all()
    return costume_requests_schema.jsonify(requests), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
