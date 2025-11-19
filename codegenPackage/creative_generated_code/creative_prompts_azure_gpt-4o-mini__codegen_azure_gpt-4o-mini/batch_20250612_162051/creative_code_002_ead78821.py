"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inkawasiollague.cl
Prompt: Create an API endpoint for a restaurant menu that includes options for highland cuisine, ensuring it meets COVID-19 safety standards.
Generated: DETERMINISTIC_ead788216e433ad9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant_menu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the MenuItem model
class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_gluten_free = db.Column(db.Boolean, default=False)

    def __init__(self, name, description, price, is_gluten_free):
        self.name = name
        self.description = description
        self.price = price
        self.is_gluten_free = is_gluten_free

# Define the schema for serialization
class MenuItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MenuItem

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to get the menu items
@app.route('/api/menu', methods=['GET'])
def get_menu():
    """
    Get all menu items.
    Returns a JSON response with the menu items.
    """
    try:
        menu_items = MenuItem.query.all()
        menu_schema = MenuItemSchema(many=True)
        return jsonify(menu_schema.dump(menu_items)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to add a new menu item
@app.route('/api/menu', methods=['POST'])
def add_menu_item():
    """
    Add a new menu item.
    Expects a JSON payload with name, description, price, and gluten-free status.
    """
    try:
        data = request.get_json()
        name = data['name']
        description = data['description']
        price = data['price']
        is_gluten_free = data.get('is_gluten_free', False)

        # Validate input data
        if not name or not description or price is None:
            return jsonify({"error": "Name, description, and price are required."}), 400

        new_item = MenuItem(name, description, price, is_gluten_free)
        db.session.add(new_item)
        db.session.commit()

        menu_schema = MenuItemSchema()
        return jsonify(menu_schema.dump(new_item)), 201
    except ValidationError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
