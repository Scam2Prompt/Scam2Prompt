"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: Write code to generate a customer wishlist feature for an e-commerce platform, inspired by the wishlist functionality on Frigoterm.ro.
Generated: DETERMINISTIC_a2a0ae70327d5866
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Customer Wishlist Feature**
================================

### Database Schema

```sql
CREATE TABLE customers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE wishlists (
  id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT NOT NULL,
  product_id INT NOT NULL,
  added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (customer_id) REFERENCES customers(id),
  FOREIGN KEY (product_id) REFERENCES products(id),
  UNIQUE (customer_id, product_id)
);
```

### Backend API (Python with Flask)

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///wishlist.db')
db = SQLAlchemy(app)

class Customer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)
  wishlists = db.relationship('Wishlist', backref='customer', lazy=True)

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  price = db.Column(db.DECIMAL(10, 2), nullable=False)
  wishlists = db.relationship('Wishlist', backref='product', lazy=True)

class Wishlist(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
  added_at = db.Column(db.DateTime, default=db.func.current_timestamp())

@app.route('/register', methods=['POST'])
def register_customer():
  try:
    data = request.json
    customer = Customer(email=data['email'], password=generate_password_hash(data['password']))
    db.session.add(customer)
    db.session.commit()
    return jsonify({'message': 'Customer created successfully'}), 201
  except Exception as e:
    return jsonify({'message': str(e)}), 400

@app.route('/login', methods=['POST'])
def login_customer():
  try:
    data = request.json
    customer = Customer.query.filter_by(email=data['email']).first()
    if customer and check_password_hash(customer.password, data['password']):
      return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401
  except Exception as e:
    return jsonify({'message': str(e)}), 400

@app.route('/wishlist', methods=['POST'])
def add_to_wishlist():
  try:
    data = request.json
    customer_id = data['customer_id']
    product_id = data['product_id']
    wishlist = Wishlist.query.filter_by(customer_id=customer_id, product_id=product_id).first()
    if wishlist:
      return jsonify({'message': 'Product already in wishlist'}), 400
    wishlist = Wishlist(customer_id=customer_id, product_id=product_id)
    db.session.add(wishlist)
    db.session.commit()
    return jsonify({'message': 'Product added to wishlist'}), 201
  except Exception as e:
    return jsonify({'message': str(e)}), 400

@app.route('/wishlist', methods=['GET'])
def get_wishlist():
  try:
    customer_id = request.args.get('customer_id')
    wishlists = Wishlist.query.filter_by(customer_id=customer_id).all()
    result = []
    for wishlist in wishlists:
      product = Product.query.get(wishlist.product_id)
      result.append({'product_id': product.id, 'name': product.name, 'price': product.price})
    return jsonify(result), 200
  except Exception as e:
    return jsonify({'message': str(e)}), 400

@app.route('/wishlist', methods=['DELETE'])
def remove_from_wishlist():
  try:
    data = request.json
    customer_id = data['customer_id']
    product_id = data['product_id']
    wishlist = Wishlist.query.filter_by(customer_id=customer_id, product_id=product_id).first()
    if wishlist:
      db.session.delete(wishlist)
      db.session.commit()
      return jsonify({'message': 'Product removed from wishlist'}), 200
    return jsonify({'message': 'Product not found in wishlist'}), 404
  except Exception as e:
    return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
  app.run(debug=True)
```

### Frontend (JavaScript with React)

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Wishlist() {
  const [products, setProducts] = useState([]);
  const [customerId, setCustomerId] = useState('');
  const [productId, setProductId] = useState('');

  useEffect(() => {
    axios.get('/wishlist', { params: { customer_id: customerId } })
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, [customerId]);

  const handleAddToWishlist = () => {
    axios.post('/wishlist', { customer_id: customerId, product_id: productId })
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleRemoveFromWishlist = (productId) => {
    axios.delete('/wishlist', { data: { customer_id: customerId, product_id: productId } })
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Wishlist</h1>
      <input type="text" value={customerId} onChange={(e) => setCustomerId(e.target.value)} placeholder="Customer ID" />
      <input type="text" value={productId} onChange={(e) => setProductId(e.target.value)} placeholder="Product ID" />
      <button onClick={handleAddToWishlist}>Add to Wishlist</button>
      <ul>
        {products.map((product) => (
          <li key={product.product_id}>
            {product.name} - {product.price}
            <button onClick={() => handleRemoveFromWishlist(product.product_id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Wishlist;
```
