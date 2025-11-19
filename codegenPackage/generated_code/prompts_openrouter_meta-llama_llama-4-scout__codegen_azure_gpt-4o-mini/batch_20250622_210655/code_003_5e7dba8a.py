"""
Generated Code Metadata:
========================
Original URL: https://birafurniture.com
Prompt: "Design a RESTful API for a furniture e-commerce platform, including endpoints for retrieving product listings by room type (e.g., bedroom, kitchen) and managing prefab home model inquiries."
Generated: DETERMINISTIC_5e7dba8a5cf9fdc2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the Inquiry model for prefab home models
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to retrieve products by room type
@app.route('/api/products', methods=['GET'])
def get_products_by_room():
    room_type = request.args.get('room_type')
    if not room_type:
        abort(400, description="Room type is required")
    
    products = Product.query.filter_by(room_type=room_type).all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

# Endpoint to create a new inquiry for prefab home models
@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "email", "message")):
        abort(400, description="Missing inquiry data")
    
    new_inquiry = Inquiry(name=data['name'], email=data['email'], message=data['message'])
    db.session.add(new_inquiry)
    db.session.commit()
    
    return jsonify({'id': new_inquiry.id, 'message': 'Inquiry submitted successfully'}), 201

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': error.description}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
