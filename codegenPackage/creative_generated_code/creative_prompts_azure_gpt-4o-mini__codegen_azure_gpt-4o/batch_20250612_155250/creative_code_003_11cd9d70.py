"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Suggest a library for building a shopping cart system that includes categories like 'Pisos e Revestimentos' and 'Materiais de Construção' as found on Jurunense Home Center."
Generated: DETERMINISTIC_11cd9d7094630430
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Building a shopping cart system using Flask and SQLAlchemy
This implementation provides a foundation for managing categories and items like 'Pisos e Revestimentos' and 'Materiais de Construção'.
"""

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_cart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Define the Category model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    items = db.relationship('Item', backref='category', lazy=True)

    def to_dict(self):
        """
        Convert Category object to dictionary for JSON serialization.
        """
        return {
            'id': self.id,
            'name': self.name
        }


# Define the Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def to_dict(self):
        """
        Convert Item object to dictionary for JSON serialization.
        """
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category_id': self.category_id
        }


@app.before_first_request
def create_tables():
    """
    Create database tables if they don't already exist.
    """
    db.create_all()


@app.route('/categories', methods=['POST'])
def create_category():
    """
    Endpoint to create a new category.
    """
    data = request.json
    if not data or 'name' not in data:
        abort(400, 'Request must include a "name" field.')

    category = Category(name=data['name'])
    try:
        db.session.add(category)
        db.session.commit()
        return jsonify(category.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        abort(500, f'Error creating category: {str(e)}')


@app.route('/categories', methods=['GET'])
def get_categories():
    """
    Endpoint to retrieve all categories.
    """
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories]), 200


@app.route('/items', methods=['POST'])
def create_item():
    """
    Endpoint to create a new item in a category.
    """
    data = request.json
    if not data or 'name' not in data or 'price' not in data or 'category_id' not in data:
        abort(400, 'Request must include "name", "price", and "category_id" fields.')

    category = Category.query.get(data['category_id'])
    if not category:
        abort(404, 'Category not found.')

    item = Item(name=data['name'], price=data['price'], category_id=data['category_id'])
    try:
        db.session.add(item)
        db.session.commit()
        return jsonify(item.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        abort(500, f'Error creating item: {str(e)}')


@app.route('/items', methods=['GET'])
def get_items():
    """
    Endpoint to retrieve all items with optional filtering by category.
    """
    category_id = request.args.get('category_id')
    if category_id:
        items = Item.query.filter_by(category_id=category_id).all()
    else:
        items = Item.query.all()

    return jsonify([item.to_dict() for item in items]), 200


@app.errorhandler(400)
def handle_bad_request(error):
    """
    Handle 400 Bad Request errors.
    """
    return jsonify({'error': str(error)}), 400


@app.errorhandler(404)
def handle_not_found(error):
    """
    Handle 404 Not Found errors.
    """
    return jsonify({'error': str(error)}), 404


@app.errorhandler(500)
def handle_internal_server_error(error):
    """
    Handle 500 Internal Server errors.
    """
    return jsonify({'error': str(error)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
