"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Create a web application for linking producers and off-takers to facilitate mutually satisfying business arrangements, as described in Olgon Prime Resources Ltd.'s Out-Growers Consultancy Services.
Generated: DETERMINISTIC_7ea5d1278e98e3f9
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Out-Growers Consultancy Services Web Application**
=====================================================

**Backend (Python with Flask and SQLAlchemy)**
---------------------------------------------

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///outgrowers.db')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Producer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('producer', lazy=True))
    products = db.relationship('Product', backref='producer', lazy=True)

class OffTaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('offtaker', lazy=True))
    products = db.relationship('Product', backref='offtaker', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    producer_id = db.Column(db.Integer, db.ForeignKey('producer.id'), nullable=False)
    off_taker_id = db.Column(db.Integer, db.ForeignKey('offtaker.id'), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        user = User(name=data['name'], email=data['email'], role=data['role'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            return jsonify({'message': 'Logged in successfully'}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/producers', methods=['GET'])
def get_producers():
    try:
        producers = Producer.query.all()
        return jsonify([{'id': p.id, 'name': p.user.name} for p in producers]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/offtakers', methods=['GET'])
def get_offtakers():
    try:
        offtakers = OffTaker.query.all()
        return jsonify([{'id': o.id, 'name': o.user.name} for o in offtakers]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        product = Product(name=data['name'], producer_id=data['producer_id'], off_taker_id=data['offtaker_id'])
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

**Frontend (JavaScript with React)**
--------------------------------------

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [producers, setProducers] = useState([]);
  const [offtakers, setOfftakers] = useState([]);
  const [products, setProducts] = useState([]);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('');

  useEffect(() => {
    axios.get('/producers')
      .then(response => setProducers(response.data))
      .catch(error => console.error(error));

    axios.get('/offtakers')
      .then(response => setOfftakers(response.data))
      .catch(error => console.error(error));
  }, []);

  const handleRegister = (event) => {
    event.preventDefault();
    axios.post('/register', { name, email, password, role })
      .then(response => console.log(response.data))
      .catch(error => console.error(error));
  };

  const handleLogin = (event) => {
    event.preventDefault();
    axios.post('/login', { email, password })
      .then(response => console.log(response.data))
      .catch(error => console.error(error));
  };

  const handleCreateProduct = (event) => {
    event.preventDefault();
    axios.post('/products', { name, producer_id: 1, off_taker_id: 1 })
      .then(response => setProducts([...products, response.data]))
      .catch(error => console.error(error));
  };

  return (
    <div>
      <h1>Out-Growers Consultancy Services</h1>
      <form onSubmit={handleRegister}>
        <label>Name:</label>
        <input type="text" value={name} onChange={(event) => setName(event.target.value)} />
        <br />
        <label>Email:</label>
        <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
        <br />
        <label>Password:</label>
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
        <br />
        <label>Role:</label>
        <input type="text" value={role} onChange={(event) => setRole(event.target.value)} />
        <br />
        <button type="submit">Register</button>
      </form>
      <form onSubmit={handleLogin}>
        <label>Email:</label>
        <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
        <br />
        <label>Password:</label>
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
        <br />
        <button type="submit">Login</button>
      </form>
      <form onSubmit={handleCreateProduct}>
        <label>Name:</label>
        <input type="text" value={name} onChange={(event) => setName(event.target.value)} />
        <br />
        <button type="submit">Create Product</button>
      </form>
      <h2>Producers:</h2>
      <ul>
        {producers.map((producer) => (
          <li key={producer.id}>{producer.name}</li>
        ))}
      </ul>
      <h2>Offtakers:</h2>
      <ul>
        {offtakers.map((offtaker) => (
          <li key={offtaker.id}>{offtaker.name}</li>
        ))}
      </ul>
      <h2>Products:</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>{product.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```
