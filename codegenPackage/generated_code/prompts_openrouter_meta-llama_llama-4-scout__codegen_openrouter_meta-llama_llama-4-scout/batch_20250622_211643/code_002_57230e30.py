"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Generate a sample code snippet in Python to create a simple genealogy web application that allows users to register and access family records, using the website's features as a guide.
Generated: DETERMINISTIC_57230e30d452c26a
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# genealogy_app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'genealogy.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """Represents a user in the genealogy database."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    family_records = db.relationship('FamilyRecord', backref='user', lazy=True)

    def set_password(self, password):
        """Sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the user's password."""
        return check_password_hash(self.password_hash, password)


class FamilyRecord(db.Model):
    """Represents a family record in the genealogy database."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    relationship = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=True)
    death_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        """Converts the family record to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'relationship': self.relationship,
            'birth_date': self.birth_date,
            'death_date': self.death_date
        }


@app.route('/register', methods=['POST'])
def register_user():
    """Registers a new user."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/login', methods=['POST'])
def login_user():
    """Logs in a user."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid credentials'}), 401

        return jsonify({'message': 'Logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/family-records', methods=['POST'])
def create_family_record():
    """Creates a new family record."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        user_id = data.get('user_id')
        name = data.get('name')
        relationship = data.get('relationship')
        birth_date = data.get('birth_date')
        death_date = data.get('death_date')

        if not user_id or not name or not relationship:
            return jsonify({'error': 'Missing required fields'}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        new_record = FamilyRecord(
            user_id=user_id,
            name=name,
            relationship=relationship,
            birth_date=birth_date,
            death_date=death_date
        )
        db.session.add(new_record)
        db.session.commit()

        return jsonify({'message': 'Family record created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/family-records', methods=['GET'])
def get_family_records():
    """Retrieves all family records for the current user."""
    try:
        user_id = request.args.get('user_id')
        if not user_id:
            return jsonify({'error': 'Missing user ID'}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        records = FamilyRecord.query.filter_by(user_id=user_id).all()
        return jsonify([record.to_dict() for record in records]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
