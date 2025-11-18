"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Create a REST API endpoint to allow users in the City of York to query their recycling collection schedule based on their address.
Generated: DETERMINISTIC_3d496449f3346c8e
Batch ID: 20250612_151018
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
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///recycling.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the RecyclingCollection model
class RecyclingCollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200), nullable=False)
    collection_date = db.Column(db.String(10), nullable=False)

# Define the schema for input validation
class RecyclingCollectionSchema(Schema):
    address = fields.Str(required=True)
    
collection_schema = RecyclingCollectionSchema()

# API endpoint to get the recycling collection schedule
@app.route('/api/recycling-schedule', methods=['GET'])
def get_recycling_schedule():
    """
    Endpoint to retrieve the recycling collection schedule for a given address in the City of York.
    Query parameter: address (str) - The address to check the recycling schedule.
    Returns: JSON object with collection date or error message.
    """
    try:
        # Validate and deserialize input data
        args = request.args
        errors = collection_schema.validate(args)
        if errors:
            return jsonify({"error": errors}), 400
        
        address = args['address']
        
        # Query the database for the recycling collection schedule
        schedule = RecyclingCollection.query.filter_by(address=address).first()
        
        if schedule:
            return jsonify({
                "address": schedule.address,
                "collection_date": schedule.collection_date
            }), 200
        else:
            return jsonify({"message": "No recycling schedule found for this address."}), 404
    
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

# Function to create the database
def create_db():
    """Create the database with the defined tables if it doesn't exist."""
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_db()  # Create database tables if needed
    app.run(debug=False)  # Set debug=False for production
```
