"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwereplicabelts.com
Prompt: Develop a REST API for managing categories like WWE, NBA, NFL, NHL, and MLB championship belts, with endpoints for adding, updating, and retrieving product information.
Generated: DETERMINISTIC_2a4d3ebd1d9eb8ad
Batch ID: 20250612_154355
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///categories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Category
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"

# Schema for validating and serializing Category data
class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all categories
@app.route('/categories', methods=['GET'])
def get_categories():
    """Retrieve all categories."""
    categories = Category.query.all()
    return jsonify(categories_schema.dump(categories)), 200

# Endpoint to get a single category by ID
@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """Retrieve a single category by ID."""
    category = Category.query.get(category_id)
    if category is None:
        abort(404, description="Category not found")
    return jsonify(category_schema.dump(category)), 200

# Endpoint to add a new category
@app.route('/categories', methods=['POST'])
def add_category():
    """Add a new category."""
    try:
        new_category = category_schema.load(request.json)
        category = Category(name=new_category['name'])
        db.session.add(category)
        db.session.commit()
        return jsonify(category_schema.dump(category)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        abort(500, description=str(e))

# Endpoint to update an existing category
@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    """Update an existing category."""
    category = Category.query.get(category_id)
    if category is None:
        abort(404, description="Category not found")
    
    try:
        updated_data = category_schema.load(request.json)
        category.name = updated_data['name']
        db.session.commit()
        return jsonify(category_schema.dump(category)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        abort(500, description=str(e))

# Endpoint to delete a category
@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    """Delete a category."""
    category = Category.query.get(category_id)
    if category is None:
        abort(404, description="Category not found")
    
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted successfully"}), 204

if __name__ == '__main__':
    app.run(debug=False)
```
