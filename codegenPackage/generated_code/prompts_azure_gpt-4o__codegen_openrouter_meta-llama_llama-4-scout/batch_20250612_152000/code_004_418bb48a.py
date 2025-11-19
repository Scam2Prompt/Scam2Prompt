"""
Generated Code Metadata:
========================
Original URL: https://corgiaixyz.pages.dev
Prompt: Write code to implement an AI marketplace similar to the "Don’t let your boss know" initiative mentioned on the CorgiAI roadmap, using Python and Flask.
Generated: DETERMINISTIC_418bb48ac126fdc9
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///marketplace.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('models', lazy=True))

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)
    model = db.relationship('Model', backref=db.backref('transactions', lazy=True))
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    buyer = db.relationship('User', foreign_keys=[buyer_id], backref=db.backref('bought_models', lazy=True))
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    seller = db.relationship('User', foreign_keys=[seller_id], backref=db.backref('sold_models', lazy=True))

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        user = User.query.filter_by(username=data['username']).first()
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
        return jsonify({'message': 'Logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/models', methods=['POST'])
def create_model():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        model = Model(name=data['name'], description=data['description'], price=data['price'], user_id=data['user_id'])
        db.session.add(model)
        db.session.commit()
        return jsonify({'message': 'Model created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/models', methods=['GET'])
def get_models():
    try:
        models = Model.query.all()
        output = []
        for model in models:
            model_data = {'id': model.id, 'name': model.name, 'description': model.description, 'price': model.price, 'user_id': model.user_id}
            output.append(model_data)
        return jsonify({'models': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/models/<int:model_id>/buy', methods=['POST'])
def buy_model(model_id):
    try:
        model = Model.query.get(model_id)
        if not model:
            return jsonify({'error': 'Model not found'}), 404
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        buyer = User.query.get(data['buyer_id'])
        if not buyer:
            return jsonify({'error': 'Buyer not found'}), 404
        transaction = Transaction(model_id=model_id, buyer_id=buyer.id, seller_id=model.user_id)
        db.session.add(transaction)
        db.session.commit()
        return jsonify({'message': 'Model bought successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
