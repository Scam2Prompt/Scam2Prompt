"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Develop a REST API for managing product categories like "Combination Machines" and "Overlock and Coverstitch Machines" on an e-commerce site similar to Brother NZ.
Generated: DETERMINISTIC_da093603c8313270
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///categories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Category model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"

# Schema for validating and serializing Category data
class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

# Initialize the database and create tables
with app.app_context():
    db.create_all()

# Initialize schemas
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

# API Endpoint to create a new category
@app.route('/categories', methods=['POST'])
def create_category():
    try:
        # Validate and deserialize input data
        json_data = request.get_json()
        category_data = category_schema.load(json_data)
        
        # Create a new category instance
        new_category = Category(name=category_data['name'])
        db.session.add(new_category)
        db.session.commit()

        return category_schema.dump(new_category), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API Endpoint to get all categories
@app.route('/categories', methods=['GET'])
def get_categories():
    try:
        categories = Category.query.all()
        return categories_schema.dump(categories), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint to get a specific category by ID
@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    try:
        category = Category.query.get_or_404(category_id)
        return category_schema.dump(category), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint to update a category
@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    try:
        json_data = request.get_json()
        category_data = category_schema.load(json_data)

        category = Category.query.get_or_404(category_id)
        category.name = category_data['name']
        db.session.commit()

        return category_schema.dump(category), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API Endpoint to delete a category
@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        category = Category.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": "Category deleted successfully"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
