"""
Generated Code Metadata:
========================
Original URL: https://www.hostalcasadelmar.es
Prompt: Create a RESTful API for a hotel management system that allows users to reserve rooms and view amenities, taking cues from the unique offerings of Hostal Casa del Mar.
Generated: DETERMINISTIC_5110de76dc199d07
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production

# Initialize database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(10), unique=True, nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    max_occupancy = db.Column(db.Integer, nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    description = db.Column(db.Text)

class Amenity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    is_available = db.Column(db.Boolean, default=True)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    check_in_date = db.Column(db.DateTime, nullable=False)
    check_out_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled

# Helper functions
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        return jsonify({'message': 'Username or email already exists!'}), 400
    
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    
    if not auth or not auth['username'] or not auth['password']:
        return jsonify({'message': 'Could not verify!'}), 401
    
    user = User.query.filter_by(username=auth['username']).first()
    
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    if check_password_hash(user.password, auth['password']):
        token = jwt.encode({
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        
        return jsonify({'token': token})
    
    return jsonify({'message': 'Wrong password!'}), 401

@app.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = Room.query.filter_by(is_available=True).all()
    
    output = []
    for room in rooms:
        room_data = {
            'id': room.id,
            'room_number': room.room_number,
            'room_type': room.room_type,
            'price_per_night': room.price_per_night,
            'max_occupancy': room.max_occupancy,
            'description': room.description
        }
        output.append(room_data)
    
    return jsonify({'rooms': output})

@app.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = Amenity.query.filter_by(is_available=True).all()
    
    output = []
    for amenity in amenities:
        amenity_data = {
            'id': amenity.id,
            'name': amenity.name,
            'description': amenity.description
        }
        output.append(amenity_data)
    
    return jsonify({'amenities': output})

@app.route('/reserve', methods=['POST'])
@token_required
def create_reservation(current_user):
    data = request.get_json()
    
    # Check if room exists and is available
    room = Room.query.filter_by(id=data['room_id'], is_available=True).first()
    if not room:
        return jsonify({'message': 'Room not available!'}), 400
    
    # Calculate total price
    check_in = datetime.datetime.strptime(data['check_in_date'], '%Y-%m-%d')
    check_out = datetime.datetime.strptime(data['check_out_date'], '%Y-%m-%d')
    nights = (check_out - check_in).days
    total_price = nights * room.price_per_night
    
    # Create reservation
    new_reservation = Reservation(
        user_id=current_user.id,
        room_id=room.id,
        check_in_date=check_in,
        check_out_date=check_out,
        total_price=total_price
    )
    
    try:
        db.session.add(new_reservation)
        db.session.commit()
    except:
        return jsonify({'message': 'Error creating reservation!'}), 500
    
    return jsonify({'message': 'Reservation created successfully!'}), 201

@app.route('/reservations', methods=['GET'])
@token_required
def get_user_reservations(current_user):
    reservations = Reservation.query.filter_by(user_id=current_user.id).all()
    
    output = []
    for reservation in reservations:
        room = Room.query.get(reservation.room_id)
        reservation_data = {
            'id': reservation.id,
            'room_number': room.room_number,
            'room_type': room.room_type,
            'check_in_date': reservation.check_in_date,
            'check_out_date': reservation.check_out_date,
            'total_price': reservation.total_price,
            'status': reservation.status
        }
        output.append(reservation_data)
    
    return jsonify({'reservations': output})

# Admin routes
@app.route('/admin/rooms', methods=['POST'])
@token_required
def add_room(current_user):
    if not current_user.is_admin:
        return jsonify({'message': 'Admin access required!'}), 403
    
    data = request.get_json()
    
    new_room = Room(
        room_number=data['room_number'],
        room_type=data['room_type'],
        price_per_night=data['price_per_night'],
        max_occupancy=data['max_occupancy'],
        description=data.get('description', '')
    )
    
    try:
        db.session.add(new_room)
        db.session.commit()
    except:
        return jsonify({'message': 'Room number already exists!'}), 400
    
    return jsonify({'message': 'Room added successfully!'}), 201

@app.route('/admin/amenities', methods=['POST'])
@token_required
def add_amenity(current_user):
    if not current_user.is_admin:
        return jsonify({'message': 'Admin access required!'}), 403
    
    data = request.get_json()
    
    new_amenity = Amenity(
        name=data['name'],
        description=data.get('description', '')
    )
    
    try:
        db.session.add(new_amenity)
        db.session.commit()
    except:
        return jsonify({'message': 'Error adding amenity!'}), 500
    
    return jsonify({'message': 'Amenity added successfully!'}), 201

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
