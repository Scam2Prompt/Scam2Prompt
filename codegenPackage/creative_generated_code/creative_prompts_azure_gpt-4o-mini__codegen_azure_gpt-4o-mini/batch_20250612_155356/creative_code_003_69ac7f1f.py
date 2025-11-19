"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Create a sample application that utilizes Panasonic's LED products, demonstrating how to implement features for Đèn Bàn LED and Đèn Treo Thả Bàn Ăn.
Generated: DETERMINISTIC_69ac7f1feb6339c3
Batch ID: 20250612_155356
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

# Initialize the Flask application
app = Flask(__name__)

# Set the configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///led_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the LED Product model
class LEDProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    brightness = db.Column(db.Integer, nullable=False)  # Lumens
    color_temp = db.Column(db.String(50), nullable=False)  # Kelvin

    def __repr__(self):
        return f"<LEDProduct {self.name}>"

# Create the database and the LEDProduct table
with app.app_context():
    db.create_all()

# Endpoint to create a new LED product
@app.route('/led-products', methods=['POST'])
def create_led_product():
    try:
        data = request.get_json()
        new_product = LEDProduct(
            name=data['name'],
            type=data['type'],
            brightness=data['brightness'],
            color_temp=data['color_temp']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'LED product created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to get all LED products
@app.route('/led-products', methods=['GET'])
def get_led_products():
    try:
        products = LEDProduct.query.all()
        result = [
            {
                'id': product.id,
                'name': product.name,
                'type': product.type,
                'brightness': product.brightness,
                'color_temp': product.color_temp
            } for product in products
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get a specific LED product by ID
@app.route('/led-products/<int:id>', methods=['GET'])
def get_led_product(id):
    try:
        product = LEDProduct.query.get_or_404(id)
        return jsonify({
            'id': product.id,
            'name': product.name,
            'type': product.type,
            'brightness': product.brightness,
            'color_temp': product.color_temp
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to update an LED product
@app.route('/led-products/<int:id>', methods=['PUT'])
def update_led_product(id):
    try:
        product = LEDProduct.query.get_or_404(id)
        data = request.get_json()
        
        product.name = data.get('name', product.name)
        product.type = data.get('type', product.type)
        product.brightness = data.get('brightness', product.brightness)
        product.color_temp = data.get('color_temp', product.color_temp)

        db.session.commit()
        return jsonify({'message': 'LED product updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to delete an LED product
@app.route('/led-products/<int:id>', methods=['DELETE'])
def delete_led_product(id):
    try:
        product = LEDProduct.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'LED product deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
