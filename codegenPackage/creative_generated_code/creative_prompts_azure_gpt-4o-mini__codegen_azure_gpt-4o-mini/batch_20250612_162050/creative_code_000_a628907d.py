"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nellyservis.sk
Prompt: Generate a code snippet for a web application that allows users to request a quote for window installation services, similar to the offerings on NellyServis.
Generated: DETERMINISTIC_a628907d6c5e10f8
Batch ID: 20250612_162050
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
import re

# Initialize the Flask application
app = Flask(__name__)

# Configurations for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and schema
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Quote model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    window_type = db.Column(db.String(100), nullable=False)
    dimensions = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.Text, nullable=True)

    def __init__(self, name, email, phone, window_type, dimensions, notes):
        self.name = name
        self.email = email
        self.phone = phone
        self.window_type = window_type
        self.dimensions = dimensions
        self.notes = notes

# Quote schema
class QuoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quote

# Initialize database
with app.app_context():
    db.create_all()

# Route to request a quote
@app.route('/request-quote', methods=['POST'])
def request_quote():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate required fields
        if not all(key in data for key in ('name', 'email', 'phone', 'window_type', 'dimensions')):
            return jsonify({"error": "Missing required fields"}), 400

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
            return jsonify({"error": "Invalid email format"}), 400

        # Create a new quote
        new_quote = Quote(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            window_type=data['window_type'],
            dimensions=data['dimensions'],
            notes=data.get('notes', '')
        )

        # Add to the database
        db.session.add(new_quote)
        db.session.commit()

        # Serialize the new quote
        quote_schema = QuoteSchema()
        return quote_schema.jsonify(new_quote), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
```
