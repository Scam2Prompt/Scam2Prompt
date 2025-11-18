"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Suggest a library or framework for building a web-based platform to manage technical assistance requests for machinery brands like FIATALLIS and IVECO, as offered by Track Diesel Peru.
Generated: DETERMINISTIC_24550192d786a054
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///technical_assistance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Technical Assistance Request model
class TechnicalAssistanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    request_description = db.Column(db.String(500), nullable=False)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)

# Create a schema for serialization
class TechnicalAssistanceRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TechnicalAssistanceRequest

# Create the database table
with app.app_context():
    db.create_all()

# Route to create a new technical assistance request
@app.route('/requests', methods=['POST'])
def add_request():
    try:
        # Get JSON data from request
        brand = request.json.get('brand')
        request_description = request.json.get('request_description')
        
        # Validate input data
        if not brand or not request_description:
            return jsonify({"error": "Brand and description are required."}), 400

        # Create a new request
        new_request = TechnicalAssistanceRequest(
            brand=brand,
            request_description=request_description
        )
        
        # Add to the session and commit
        db.session.add(new_request)
        db.session.commit()

        # Serialize the new request
        return TechnicalAssistanceRequestSchema().jsonify(new_request), 201

    except Exception as e:
        # Handle any exceptions that occur
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all technical assistance requests
@app.route('/requests', methods=['GET'])
def get_requests():
    try:
        requests = TechnicalAssistanceRequest.query.all()
        return TechnicalAssistanceRequestSchema(many=True).jsonify(requests), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required libraries before running the code:

```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow
```
