"""
Generated Code Metadata:
========================
Original URL: https://pandana.vip
Prompt: Design a simple RESTful API using Flask for a VIP membership system inspired by Pandana VIP.
Generated: DETERMINISTIC_dbd30932df1df404
Batch ID: 20250622_210840
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
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vip.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    membership_level = db.Column(db.String(100), default='bronze')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


class VIPMembership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    membership_level = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, membership_level):
        self.user_id = user_id
        self.membership_level = membership_level


# Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class VIPMembershipSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VIPMembership


# Routes
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'message': 'Please provide all required fields'}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'Email already exists'}), 400

        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Please provide all required fields'}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid credentials'}), 401

        return jsonify({'message': 'User logged in successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route('/upgrade-membership', methods=['POST'])
def upgrade_membership():
    try:
        data = request.json
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        user_id = data.get('user_id')
        membership_level = data.get('membership_level')

        if not user_id or not membership_level:
            return jsonify({'message': 'Please provide all required fields'}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        existing_membership = VIPMembership.query.filter_by(user_id=user_id).first()
        if existing_membership:
            existing_membership.membership_level = membership_level
            db.session.commit()
        else:
            new_membership = VIPMembership(user_id, membership_level)
            db.session.add(new_membership)
            db.session.commit()

        return jsonify({'message': 'Membership upgraded successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        user_schema = UserSchema(many=True)
        return jsonify(user_schema.dump(users)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route('/memberships', methods=['GET'])
def get_memberships():
    try:
        memberships = VIPMembership.query.all()
        membership_schema = VIPMembershipSchema(many=True)
        return jsonify(membership_schema.dump(memberships)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
