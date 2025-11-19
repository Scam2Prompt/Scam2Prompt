"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Design an API for tracking cryptocurrency token presales, including fields for presale cap, total supply, and token pricing tiers, inspired by the $ALIEN PRE-SALE webpage.
Generated: DETERMINISTIC_311a79892fbf5452
Batch ID: 20250622_205836
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///presales.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Presale model
class Presale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token_name = db.Column(db.String(100), nullable=False)
    presale_cap = db.Column(db.Float, nullable=False)
    total_supply = db.Column(db.Float, nullable=False)
    pricing_tiers = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f'<Presale {self.token_name}>'

# Define the schema for input validation
class PresaleSchema(Schema):
    token_name = fields.Str(required=True)
    presale_cap = fields.Float(required=True)
    total_supply = fields.Float(required=True)
    pricing_tiers = fields.List(fields.Dict(), required=True)

# Initialize the schema
presale_schema = PresaleSchema()
presales_schema = PresaleSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new presale
@app.route('/presales', methods=['POST'])
def create_presale():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        presale_data = presale_schema.load(data)

        # Create a new presale instance
        new_presale = Presale(
            token_name=presale_data['token_name'],
            presale_cap=presale_data['presale_cap'],
            total_supply=presale_data['total_supply'],
            pricing_tiers=presale_data['pricing_tiers']
        )

        # Add the new presale to the database
        db.session.add(new_presale)
        db.session.commit()

        return jsonify(presale_schema.dump(new_presale)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all presales
@app.route('/presales', methods=['GET'])
def get_presales():
    try:
        presales = Presale.query.all()
        return jsonify(presales_schema.dump(presales)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a specific presale by ID
@app.route('/presales/<int:presale_id>', methods=['GET'])
def get_presale(presale_id):
    try:
        presale = Presale.query.get_or_404(presale_id)
        return jsonify(presale_schema.dump(presale)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a presale
@app.route('/presales/<int:presale_id>', methods=['PUT'])
def update_presale(presale_id):
    try:
        data = request.get_json()
        presale_data = presale_schema.load(data)

        presale = Presale.query.get_or_404(presale_id)
        presale.token_name = presale_data['token_name']
        presale.presale_cap = presale_data['presale_cap']
        presale.total_supply = presale_data['total_supply']
        presale.pricing_tiers = presale_data['pricing_tiers']

        db.session.commit()
        return jsonify(presale_schema.dump(presale)), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a presale
@app.route('/presales/<int:presale_id>', methods=['DELETE'])
def delete_presale(presale_id):
    try:
        presale = Presale.query.get_or_404(presale_id)
        db.session.delete(presale)
        db.session.commit()
        return jsonify({"message": "Presale deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
