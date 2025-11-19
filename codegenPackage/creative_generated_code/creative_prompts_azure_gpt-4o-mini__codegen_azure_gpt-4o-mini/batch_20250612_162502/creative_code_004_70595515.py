"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bienbonvoyage.com
Prompt: Develop a RESTful API endpoint for a travel service that lists luxury adventures, taking cues from the content on Bien Bon Voyage.
Generated: DETERMINISTIC_70595515f4bfcbdb
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (example using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///luxury_adventures.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the model for Luxury Adventures
class LuxuryAdventure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<LuxuryAdventure {self.title}>'

# Create a schema for serializing Luxury Adventures
class LuxuryAdventureSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)

# Create the schema instance
luxury_adventure_schema = LuxuryAdventureSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Endpoint to list all luxury adventures
@app.route('/api/luxury-adventures', methods=['GET'])
def get_luxury_adventures():
    """
    Get a list of all luxury adventures.
    Returns:
        JSON: A list of luxury adventures with their details.
    """
    try:
        adventures = LuxuryAdventure.query.all()
        return jsonify(luxury_adventure_schema.dump(adventures)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main block to run the app
if __name__ == "__main__":
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
