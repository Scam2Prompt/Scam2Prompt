"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Create a REST API that allows users to book a dumpster rental service from Purple Dumpster, specifying the dumpster size, service area, and rental duration.
Generated: DETERMINISTIC_a33bf44e545c1229
Batch ID: 20250612_153224
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
from marshmallow import Schema, fields, ValidationError
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dumpster_rentals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create an enumeration for valid dumpster sizes
DUMPSTER_SIZES = ['small', 'medium', 'large']


# Model representing the dumpster rental
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(10), nullable=False)
    service_area = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # duration in days

    def __repr__(self):
        return f"<Rental {self.size} | {self.service_area} | {self.duration} days>"


# Schema for input validation
class RentalSchema(Schema):
    size = fields.String(required=True, validate=lambda s: s in DUMPSTER_SIZES)
    service_area = fields.String(required=True)
    duration = fields.Integer(required=True, validate=lambda n: n > 0)


# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()


# API endpoint to create a dumpster rental
@app.route('/api/rentals', methods=['POST'])
def create_rental():
    json_data = request.get_json()

    # Validate input data
    try:
        data = RentalSchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new rental entry
    rental = Rental(size=data['size'], service_area=data['service_area'], duration=data['duration'])

    try:
        db.session.add(rental)
        db.session.commit()
        return jsonify({"message": "Rental created", "id": rental.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create rental", "details": str(e)}), 500


# API endpoint to get all rentals
@app.route('/api/rentals', methods=['GET'])
def get_rentals():
    rentals = Rental.query.all()
    result = [{"id": rental.id, "size": rental.size, "service_area": rental.service_area, "duration": rental.duration} for rental in rentals]
    return jsonify(result)


# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', True))
```
