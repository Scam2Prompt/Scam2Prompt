"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starmissteenindia.com
Prompt: Create an API that handles the registration process for a modeling contest, including validation for age and educational qualifications as seen in Star Miss Teen India 2025.
Generated: DETERMINISTIC_d747d136c6557289
Batch ID: 20250612_161209
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
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contestants.db'
db = SQLAlchemy(app)

# Define the Contestant model
class Contestant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    education = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class ContestantSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True, validate=lambda n: 18 <= n <= 25)
    education = fields.String(required=True, validate=lambda s: bool(re.match(r"^(High School|Undergraduate|Graduate)$", s)))

contestant_schema = ContestantSchema()

@app.route('/register', methods=['POST'])
def register_contestant():
    """
    Endpoint to register a contestant for the modeling contest.
    Validates age (18-25) and education (High School, Undergraduate, Graduate).
    """
    try:
        # Validate and deserialize input data
        data = contestant_schema.load(request.json)

        # Check if contestant already exists in the database
        existing_contestant = Contestant.query.filter_by(name=data['name']).first()
        if existing_contestant:
            return jsonify({"error": "Contestant already registered."}), 400

        # Create a new contestant record
        new_contestant = Contestant(name=data['name'], age=data['age'], education=data['education'])
        db.session.add(new_contestant)
        db.session.commit()

        return jsonify({"message": "Contestant registered successfully!"}), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle other unforeseen errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
