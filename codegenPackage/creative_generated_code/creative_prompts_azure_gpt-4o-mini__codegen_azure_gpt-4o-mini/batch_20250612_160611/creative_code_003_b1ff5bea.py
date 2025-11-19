"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ens.gifts
Prompt: Provide an example of a RESTful API endpoint for managing gift categories as seen on ens.gifts.
Generated: DETERMINISTIC_b1ff5beab0756619
Batch ID: 20250612_160611
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
from flask_marshmallow import Marshmallow

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gifts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# GiftCategory model
class GiftCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

# GiftCategory schema
class GiftCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GiftCategory

# Create a category
@app.route('/categories', methods=['POST'])
def add_category():
    name = request.json.get('name')
    
    if not name:
        abort(400, description="Name is required")
    
    new_category = GiftCategory(name)
    
    try:
        db.session.add(new_category)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))
    
    return GiftCategorySchema().dump(new_category), 201

# Get all categories
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = GiftCategory.query.all()
    return GiftCategorySchema(many=True).dump(categories), 200

# Get a single category by ID
@app.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = GiftCategory.query.get(id)
    
    if not category:
        abort(404, description="Category not found")
    
    return GiftCategorySchema().dump(category), 200

# Update a category
@app.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    category = GiftCategory.query.get(id)
    
    if not category:
        abort(404, description="Category not found")
    
    name = request.json.get('name', category.name)
    
    category.name = name
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

    return GiftCategorySchema().dump(category), 200

# Delete a category
@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = GiftCategory.query.get(id)
    
    if not category:
        abort(404, description="Category not found")
    
    try:
        db.session.delete(category)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

    return jsonify({'message': 'Category deleted'}), 204

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```
