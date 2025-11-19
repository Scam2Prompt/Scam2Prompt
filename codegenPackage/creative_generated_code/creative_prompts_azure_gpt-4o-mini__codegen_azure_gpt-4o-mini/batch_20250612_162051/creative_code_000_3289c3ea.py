"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluivars.com
Prompt: Generate a code snippet for a web application that allows users to request quotes for iron and aluminum carpentry services, similar to those offered by Aluivars.
Generated: DETERMINISTIC_3289c3ea9602be5e
Batch ID: 20250612_162051
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
from marshmallow import ValidationError

# Initialize app, database, and marshmallow
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Quote model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(50), required=True)
    description = db.Column(db.String(200), required=True)
    contact_info = db.Column(db.String(100), required=True)

    def __init__(self, material, description, contact_info):
        self.material = material
        self.description = description
        self.contact_info = contact_info

# Define the Quote Schema
class QuoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quote

# Create a new quote
@app.route('/quotes', methods=['POST'])
def create_quote():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input
        if 'material' not in data or 'description' not in data or 'contact_info' not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create a new quote
        new_quote = Quote(
            material=data['material'],
            description=data['description'],
            contact_info=data['contact_info']
        )
        
        # Add to the database
        db.session.add(new_quote)
        db.session.commit()
        
        # Serialize the new quote
        quote_schema = QuoteSchema()
        return quote_schema.jsonify(new_quote), 201
    
    except ValidationError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the quote"}), 500

# Get all quotes
@app.route('/quotes', methods=['GET'])
def get_quotes():
    try:
        quotes = Quote.query.all()
        quotes_schema = QuoteSchema(many=True)
        return quotes_schema.jsonify(quotes), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching quotes"}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Creates database tables
    app.run(debug=False)  # Set debug=True only in development
```
