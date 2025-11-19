"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heartofjesuscollege.com
Prompt: Suggest a framework for developing a virtual library that supports interactive learning, akin to the Reeduc platform mentioned on the Heart of Jesus College website.
Generated: DETERMINISTIC_41143f6396c91595
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
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///virtual_library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


# Define a model for the library item
class LibraryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<LibraryItem {self.title}>"


# Define a schema for input validation
class LibraryItemSchema(Schema):
    title = fields.String(required=True)
    author = fields.String(required=True)
    description = fields.String()


# Initialize the schema
item_schema = LibraryItemSchema()
items_schema = LibraryItemSchema(many=True)


# Route to create a new library item
@app.route('/library/items', methods=['POST'])
def add_item():
    try:
        # Validate input data
        item_data = item_schema.load(request.json)
        new_item = LibraryItem(**item_data)
        db.session.add(new_item)
        db.session.commit()
        return item_schema.jsonify(new_item), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"message": "An error occurred while adding the item.", "error": str(e)}), 500


# Route to get all library items
@app.route('/library/items', methods=['GET'])
def get_items():
    items = LibraryItem.query.all()
    return items_schema.jsonify(items), 200


# Route to get a specific library item by ID
@app.route('/library/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = LibraryItem.query.get_or_404(item_id)
    return item_schema.jsonify(item), 200


# Route to update a specific library item by ID
@app.route('/library/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = LibraryItem.query.get_or_404(item_id)
    try:
        # Validate input data
        item_data = item_schema.load(request.json)
        for key, value in item_data.items():
            setattr(item, key, value)
        db.session.commit()
        return item_schema.jsonify(item), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"message": "An error occurred while updating the item.", "error": str(e)}), 500


# Route to delete a specific library item by ID
@app.route('/library/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = LibraryItem.query.get_or_404(item_id)
    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Item deleted successfully."}), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while deleting the item.", "error": str(e)}), 500


# Main block to run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
