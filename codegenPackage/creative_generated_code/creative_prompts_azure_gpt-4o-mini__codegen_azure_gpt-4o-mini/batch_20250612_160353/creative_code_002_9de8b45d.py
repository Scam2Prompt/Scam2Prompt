"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Create an API endpoint in Flask that allows users to submit cocktail recipes, reflecting the skills taught in the Bar y Mixología course at Egatur.
Generated: DETERMINISTIC_9de8b45d5d207b75
Batch ID: 20250612_160353
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cocktails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Cocktail model
class Cocktail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Cocktail {self.name}>'

# Create a schema for validating input data
class CocktailSchema(Schema):
    name = fields.Str(required=True, validate=lambda s: len(s) > 0)
    ingredients = fields.Str(required=True, validate=lambda s: len(s) > 0)
    instructions = fields.Str(required=True, validate=lambda s: len(s) > 0)

# Initialize the schema
cocktail_schema = CocktailSchema()
cocktails_schema = CocktailSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to submit a cocktail recipe
@app.route('/cocktails', methods=['POST'])
def add_cocktail():
    # Parse and validate the incoming JSON data
    try:
        data = request.get_json()
        cocktail_data = cocktail_schema.load(data)  # Validate data
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400  # Return error for validation issues

    # Create a new Cocktail instance
    new_cocktail = Cocktail(
        name=cocktail_data['name'],
        ingredients=cocktail_data['ingredients'],
        instructions=cocktail_data['instructions']
    )

    # Add and commit the new cocktail to the database
    try:
        db.session.add(new_cocktail)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": "Failed to add cocktail to the database."}), 500

    # Return the created cocktail data
    return cocktail_schema.jsonify(new_cocktail), 201

# API endpoint to retrieve all cocktail recipes
@app.route('/cocktails', methods=['GET'])
def get_cocktails():
    try:
        cocktails = Cocktail.query.all()  # Fetch all cocktails
        return cocktails_schema.jsonify(cocktails), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch cocktails."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', '0') == '1')
```
