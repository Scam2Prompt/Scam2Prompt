"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atakoynakliyat.gen.tr
Prompt: Generate a code snippet for a web application that allows users to request a quote for Ataköy Evden Eve Nakliyat services, including options for city and intercity moves.
Generated: DETERMINISTIC_11154b4e2460c8cb
Batch ID: 20250612_161617
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

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Quote model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    move_type = db.Column(db.String(10), nullable=False)  # 'city' or 'intercity'

# Define the schema for input validation
class QuoteSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    city = fields.Str(required=True)
    move_type = fields.Str(required=True, validate=lambda p: p in ['city', 'intercity'])

quote_schema = QuoteSchema()

# Route to request a quote
@app.route('/request-quote', methods=['POST'])
def request_quote():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = quote_schema.load(data)

        # Create a new quote instance
        new_quote = Quote(
            name=validated_data['name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            city=validated_data['city'],
            move_type=validated_data['move_type']
        )

        # Save quote to the database
        db.session.add(new_quote)
        db.session.commit()
        
        return jsonify({'message': 'Quote request submitted successfully!'}), 201

    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
