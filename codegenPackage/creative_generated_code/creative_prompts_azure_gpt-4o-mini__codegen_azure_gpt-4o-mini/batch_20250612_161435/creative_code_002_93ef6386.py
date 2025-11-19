"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://förderohr.de
Prompt: Create an API endpoint that provides users with a quote for high-pressure cleaning services based on the type of blockage, inspired by the pricing model of ElbeRohr.
Generated: DETERMINISTIC_93ef63868d147552
Batch ID: 20250612_161435
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database (you can change this to your production database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the blockage types and their pricing
class Blockage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create a schema for validating input
class QuoteSchema(Schema):
    blockage_type = fields.String(required=True)

# Endpoint to get a quote for high-pressure cleaning services
@app.route('/api/quote', methods=['POST'])
def get_quote():
    # Validate input data
    schema = QuoteSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": "Invalid input", "messages": err.messages}), 400

    blockage_type = data['blockage_type']

    # Fetch the price for the specified blockage type
    blockage = Blockage.query.filter_by(type=blockage_type).first()
    if blockage is None:
        return jsonify({"error": "Blockage type not found"}), 404

    return jsonify({"blockage_type": blockage.type, "price": blockage.price}), 200

# Initialize the database and create some sample data (for demonstration purposes)
@app.before_first_request
def create_tables():
    db.create_all()
    if Blockage.query.count() == 0:
        sample_data = [
            Blockage(type='Grease', price=150.0),
            Blockage(type='Mud', price=100.0),
            Blockage(type='Roots', price=200.0)
        ]
        db.session.bulk_save_objects(sample_data)
        db.session.commit()

# Error handling for unexpected issues
@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

To run this code, ensure you have Flask, Flask-SQLAlchemy, and Marshmallow installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy marshmallow
```
