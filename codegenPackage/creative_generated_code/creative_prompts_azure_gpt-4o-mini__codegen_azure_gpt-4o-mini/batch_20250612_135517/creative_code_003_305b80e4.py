"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cakco.com
Prompt: Develop an API endpoint that allows users to filter and search for specific types of handbags, referencing the categories found on Cakco's product listings.
Generated: DETERMINISTIC_305b80e49607db3f
Batch ID: 20250612_135517
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

# Initialize Flask application
app = Flask(__name__)

# Configure database (modify according to your database setup)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///handbags.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Handbag model
class Handbag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create a schema for validation and serialization
class HandbagSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the schema
handbag_schema = HandbagSchema(many=True)

@app.route('/api/handbags', methods=['GET'])
def get_handbags():
    """
    API endpoint to filter and search for handbags.
    Query parameters:
        - category: filter by handbag category
        - name: search by handbag name
    """
    try:
        category = request.args.get('category')
        name = request.args.get('name')

        # Build the query
        query = Handbag.query

        if category:
            query = query.filter(Handbag.category.ilike(f'%{category}%'))
        if name:
            query = query.filter(Handbag.name.ilike(f'%{name}%'))

        # Execute the query and serialize the results
        handbags = query.all()
        result = handbag_schema.dump(handbags)

        return jsonify(result), 200

    except ValidationError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()

    # Run the application
    app.run(debug=True)
```

**Note:** Ensure you have the necessary dependencies installed, such as Flask, Flask-SQLAlchemy, and Marshmallow. Adjust the database configuration and handle migrations according to your environment.
