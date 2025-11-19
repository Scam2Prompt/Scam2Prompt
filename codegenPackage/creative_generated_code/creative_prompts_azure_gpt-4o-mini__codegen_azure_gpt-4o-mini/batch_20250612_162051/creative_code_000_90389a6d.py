"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dombrinde.com.br
Prompt: Generate a code snippet for an API that allows users to customize and order personalized promotional items like pens and bags from Dom Brindes.
Generated: DETERMINISTIC_90389a6d96ba2169
Batch ID: 20250612_162051
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///promotional_items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model for Promotional Items
class PromotionalItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<PromotionalItem {self.name}>'

# Schema for input validation
class PromotionalItemSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    price = fields.Float(required=True)

item_schema = PromotionalItemSchema()
items_schema = PromotionalItemSchema(many=True)

# Create database tables on startup
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a personalized promotional item
@app.route('/items', methods=['POST'])
def create_item():
    try:
        # Validate and deserialize input
        item_data = request.get_json()
        validated_data = item_schema.load(item_data)
        
        # Create a new promotional item
        new_item = PromotionalItem(**validated_data)
        db.session.add(new_item)
        db.session.commit()
        
        return item_schema.dump(new_item), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all promotional items
@app.route('/items', methods=['GET'])
def get_items():
    try:
        items = PromotionalItem.query.all()
        return items_schema.dump(items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific promotional item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    try:
        item = PromotionalItem.query.get_or_404(item_id)
        return item_schema.dump(item), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
