"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Develop a simple API to connect parents with Morahs and teachers in Lakewood, NJ, facilitating communication and guidance on educational choices.
Generated: DETERMINISTIC_f195cc38a3e077a5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///lakewood_education.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Parent model
class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Define the Morah/Teacher model
class Morah(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Schema for validating Parent data
class ParentSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)

# Schema for validating Morah/Teacher data
class MorahSchema(Schema):
    name = fields.Str(required=True)
    subject = fields.Str(required=True)
    email = fields.Email(required=True)

# Initialize schemas
parent_schema = ParentSchema()
morah_schema = MorahSchema()

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new parent
@app.route('/parents', methods=['POST'])
def add_parent():
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = parent_schema.load(data)
        
        # Create a new Parent instance
        new_parent = Parent(**validated_data)
        db.session.add(new_parent)
        db.session.commit()
        
        return jsonify(parent_schema.dump(new_parent)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to add a new Morah/Teacher
@app.route('/morahs', methods=['POST'])
def add_morah():
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = morah_schema.load(data)
        
        # Create a new Morah instance
        new_morah = Morah(**validated_data)
        db.session.add(new_morah)
        db.session.commit()
        
        return jsonify(morah_schema.dump(new_morah)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all parents
@app.route('/parents', methods=['GET'])
def get_parents():
    try:
        parents = Parent.query.all()
        return jsonify(parent_schema.dump(parents, many=True)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all Morahs/Teachers
@app.route('/morahs', methods=['GET'])
def get_morahs():
    try:
        morahs = Morah.query.all()
        return jsonify(morah_schema.dump(morahs, many=True)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
