"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wufis.com
Prompt: Recommend an API or library for implementing a secure online booking system for pet sitters, as outlined on WUFIS.
Generated: DETERMINISTIC_4d6f55246e6287d5
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pet_sitters.db'  # Use SQLite for simplicity
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a stronger secret in production
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Database model for Booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_sitter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pet_owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    details = db.Column(db.String(200), nullable=True)

# Token authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(data['username'], *args, **kwargs)
    return decorated

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'message': str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    
    if user and check_password_hash(user.password, data.get('password')):
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                           app.config['SECRET_KEY'])
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid username or password!'}), 401

# Route for creating a booking
@app.route('/book', methods=['POST'])
@token_required
def book(username):
    data = request.get_json()
    if not data or not data.get('pet_sitter_id') or not data.get('date'):
        return jsonify({'message': 'Pet sitter ID and date are required!'}), 400

    new_booking = Booking(pet_sitter_id=data['pet_sitter_id'], 
                          pet_owner_id=username, 
                          date=datetime.datetime.fromisoformat(data['date']),
                          details=data.get('details'))

    try:
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Booking created successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'message': str(e)}), 500

# Route for viewing bookings (for pet owners)
@app.route('/my_bookings', methods=['GET'])
@token_required
def my_bookings(username):
    bookings = Booking.query.filter_by(pet_owner_id=username).all()
    return jsonify([{'id': b.id, 'pet_sitter_id': b.pet_sitter_id, 'date': b.date, 'details': b.details} for b in bookings]), 200

# Error handler for application
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'An internal error occurred!'}), 500

# Run the app
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```
