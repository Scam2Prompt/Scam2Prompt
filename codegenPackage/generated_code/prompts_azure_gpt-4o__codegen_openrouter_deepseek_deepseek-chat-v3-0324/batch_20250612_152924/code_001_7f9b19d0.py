"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Recommend APIs or libraries to create a web-based solution for independent pharmacy owners to manage profit sharing and transparency in a cooperative structure, as outlined by PharmaChoice Canada.
Generated: DETERMINISTIC_7f9b19d07687478f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import requests

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pharmacy_coop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this in production

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Database Models
class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200))
    revenue = db.Column(db.Float, default=0.0)
    profit_share = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pharmacy_id = db.Column(db.Integer, db.ForeignKey('pharmacy.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)  # 'revenue' or 'expense'
    description = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Marshmallow Schemas
class PharmacySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'address', 'revenue', 'profit_share')

class TransactionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'pharmacy_id', 'amount', 'transaction_type', 'description', 'timestamp')

pharmacy_schema = PharmacySchema()
pharmacies_schema = PharmacySchema(many=True)
transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_pharmacy = Pharmacy(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        address=data.get('address', '')
    )
    
    db.session.add(new_pharmacy)
    db.session.commit()
    
    return jsonify({'message': 'Pharmacy registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    pharmacy = Pharmacy.query.filter_by(email=data['email']).first()
    
    if not pharmacy or not check_password_hash(pharmacy.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity=pharmacy.id)
    return jsonify({'token': access_token}), 200

@app.route('/pharmacies', methods=['GET'])
@jwt_required()
def get_pharmacies():
    pharmacies = Pharmacy.query.all()
    result = pharmacies_schema.dump(pharmacies)
    return jsonify(result)

@app.route('/transactions', methods=['POST'])
@jwt_required()
def add_transaction():
    data = request.get_json()
    pharmacy = Pharmacy.query.get(data['pharmacy_id'])
    
    if not pharmacy:
        return jsonify({'message': 'Pharmacy not found'}), 404
    
    new_transaction = Transaction(
        pharmacy_id=data['pharmacy_id'],
        amount=data['amount'],
        transaction_type=data['transaction_type'],
        description=data.get('description', '')
    )
    
    if data['transaction_type'] == 'revenue':
        pharmacy.revenue += data['amount']
    
    db.session.add(new_transaction)
    db.session.commit()
    
    return jsonify({'message': 'Transaction added successfully'}), 201

@app.route('/profit-share', methods=['GET'])
@jwt_required()
def calculate_profit_share():
    # This is a simplified calculation - adjust according to business rules
    total_revenue = sum(pharmacy.revenue for pharmacy in Pharmacy.query.all())
    pharmacies = Pharmacy.query.all()
    
    for pharmacy in pharmacies:
        pharmacy.profit_share = (pharmacy.revenue / total_revenue) * 100 if total_revenue > 0 else 0
        db.session.commit()
    
    result = pharmacies_schema.dump(pharmacies)
    return jsonify(result)

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```

```javascript
// Frontend React components (simplified example)

// PharmacyList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PharmacyList = () => {
  const [pharmacies, setPharmacies] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPharmacies = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('/api/pharmacies', {
          headers: { Authorization: `Bearer ${token}` }
        });
        setPharmacies(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching pharmacies:', error);
        setLoading(false);
      }
    };
    fetchPharmacies();
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h2>Pharmacy Cooperative Members</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Revenue</th>
            <th>Profit Share</th>
          </tr>
        </thead>
        <tbody>
          {pharmacies.map(pharmacy => (
            <tr key={pharmacy.id}>
              <td>{pharmacy.name}</td>
              <td>{pharmacy.email}</td>
              <td>${pharmacy.revenue.toFixed(2)}</td>
              <td>{pharmacy.profit_share.toFixed(2)}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PharmacyList;

// TransactionForm.js
import React, { useState } from 'react';
import axios from 'axios';

const TransactionForm = () => {
  const [formData, setFormData] = useState({
    pharmacy_id: '',
    amount: '',
    transaction_type: 'revenue',
    description: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token');
      await axios.post('/api/transactions', formData, {
        headers: { Authorization: `Bearer ${token}` }
      });
      alert('Transaction added successfully');
      setFormData({
        pharmacy_id: '',
        amount: '',
        transaction_type: 'revenue',
        description: ''
      });
    } catch (error) {
      console.error('Error adding transaction:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Transaction</h2>
      <div>
        <label>Pharmacy ID:</label>
        <input
          type="number"
          value={formData.pharmacy_id}
          onChange={(e) => setFormData({...formData, pharmacy_id: e.target.value})}
          required
        />
      </div>
      <div>
        <label>Amount:</label>
        <input
          type="number"
          step="0.01"
          value={formData.amount}
          onChange={(e) => setFormData({...formData, amount: e.target.value})}
          required
        />
      </div>
      <div>
        <label>Transaction Type:</label>
        <select
          value={formData.transaction_type}
          onChange={(e) => setFormData({...formData, transaction_type: e.target.value})}
        >
          <option value="revenue">Revenue</option>
          <option value="expense">Expense</option>
        </select>
      </div>
      <div>
        <label>Description:</label>
        <input
          type="text"
          value={formData.description}
          onChange={(e) => setFormData({...formData, description: e.target.value})}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default TransactionForm;
```
