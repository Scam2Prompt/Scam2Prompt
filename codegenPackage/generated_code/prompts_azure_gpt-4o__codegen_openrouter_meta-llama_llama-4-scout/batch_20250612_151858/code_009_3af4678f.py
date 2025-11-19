"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Provide a solution using Flask or Django to build a backend system for managing product inventory and promotions for a site like "Jurunense Home Center."
Generated: DETERMINISTIC_3af4678fc919a95f
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide a solution using Flask. Here is the code:

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    """Product model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}')"

class Promotion(db.Model):
    """Promotion model"""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('promotions', lazy=True))
    discount_type = db.Column(db.String(50), nullable=False)  # e.g. percentage, fixed_amount
    discount_value = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Promotion('{self.product.name}', '{self.discount_type}')"

class Order(db.Model):
    """Order model"""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Order('{self.product.name}', '{self.quantity}')"
```

**routes.py**
```python
from flask import Flask, request, jsonify
from models import db, Product, Promotion, Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jurunense.db'
db.init_app(app)

@app.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price, 'quantity': p.quantity} for p in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get product by ID"""
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'quantity': product.quantity})

@app.route('/products', methods=['POST'])
def create_product():
    """Create new product"""
    data = request.get_json()
    if 'name' not in data or 'price' not in data or 'quantity' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    product = Product(name=data['name'], price=data['price'], quantity=data['quantity'])
    db.session.add(product)
    db.session.commit()
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'quantity': product.quantity}), 201

@app.route('/promotions', methods=['GET'])
def get_promotions():
    """Get all promotions"""
    promotions = Promotion.query.all()
    return jsonify([{'id': p.id, 'product_id': p.product_id, 'discount_type': p.discount_type, 'discount_value': p.discount_value} for p in promotions])

@app.route('/promotions/<int:promotion_id>', methods=['GET'])
def get_promotion(promotion_id):
    """Get promotion by ID"""
    promotion = Promotion.query.get(promotion_id)
    if promotion is None:
        return jsonify({'error': 'Promotion not found'}), 404
    return jsonify({'id': promotion.id, 'product_id': promotion.product_id, 'discount_type': promotion.discount_type, 'discount_value': promotion.discount_value})

@app.route('/orders', methods=['POST'])
def create_order():
    """Create new order"""
    data = request.get_json()
    if 'product_id' not in data or 'quantity' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    product = Product.query.get(data['product_id'])
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    if product.quantity < data['quantity']:
        return jsonify({'error': 'Insufficient quantity'}), 400
    order = Order(product_id=data['product_id'], quantity=data['quantity'], order_date=datetime.now())
    db.session.add(order)
    product.quantity -= data['quantity']
    db.session.commit()
    return jsonify({'id': order.id, 'product_id': order.product_id, 'quantity': order.quantity}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

**schema.sql**
```sql
CREATE TABLE product (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price FLOAT NOT NULL,
    quantity INTEGER NOT NULL
);

CREATE TABLE promotion (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    discount_type VARCHAR(50) NOT NULL,
    discount_value FLOAT NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product (id)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date DATETIME NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product (id)
);
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
```

You can run the code by executing the following commands:
```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
python app.py
```
