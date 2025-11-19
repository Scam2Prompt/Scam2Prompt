"""
Generated Code Metadata:
========================
Original URL: https://bandadorada.com
Prompt: Generate a code snippet for a web application that allows users to book live music services for weddings and corporate events, similar to the offerings of Orquesta Dorada in Trujillo.
Generated: DETERMINISTIC_75839fb565d54d18
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
import re
from functools import wraps
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    event_location = db.Column(db.String(200), nullable=False)
    guest_count = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.Text)
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Helper functions
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            return jsonify({'error': 'Admin access required'}), 403
        return f(*args, **kwargs)
    return decorated_function

# User management
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing required fields'}), 400

    if not validate_email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 409

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 409

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Missing username or password'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401

    login_user(user)
    return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

# Booking routes
@app.route('/bookings', methods=['POST'])
@login_required
def create_booking():
    data = request.get_json()
    required_fields = ['event_type', 'event_date', 'event_location', 'guest_count']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        event_date = datetime.datetime.strptime(data['event_date'], '%Y-%m-%d').date()
        if event_date < datetime.date.today():
            return jsonify({'error': 'Event date cannot be in the past'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

    booking = Booking(
        event_type=data['event_type'],
        event_date=event_date,
        event_location=data['event_location'],
        guest_count=data['guest_count'],
        special_requests=data.get('special_requests', ''),
        user_id=current_user.id
    )
    db.session.add(booking)
    db.session.commit()

    return jsonify({'message': 'Booking created successfully', 'booking_id': booking.id}), 201

@app.route('/bookings', methods=['GET'])
@login_required
def get_user_bookings():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    result = []
    for booking in bookings:
        result.append({
            'id': booking.id,
            'event_type': booking.event_type,
            'event_date': booking.event_date.strftime('%Y-%m-%d'),
            'event_location': booking.event_location,
            'guest_count': booking.guest_count,
            'special_requests': booking.special_requests,
            'status': booking.status,
            'created_at': booking.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result), 200

@app.route('/admin/bookings', methods=['GET'])
@login_required
@admin_required
def get_all_bookings():
    bookings = Booking.query.all()
    result = []
    for booking in bookings:
        result.append({
            'id': booking.id,
            'event_type': booking.event_type,
            'event_date': booking.event_date.strftime('%Y-%m-%d'),
            'event_location': booking.event_location,
            'guest_count': booking.guest_count,
            'special_requests': booking.special_requests,
            'status': booking.status,
            'user_id': booking.user_id,
            'created_at': booking.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result), 200

@app.route('/admin/bookings/<int:booking_id>', methods=['PUT'])
@login_required
@admin_required
def update_booking_status(booking_id):
    data = request.get_json()
    if not data or not data.get('status'):
        return jsonify({'error': 'Missing status field'}), 400

    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404

    valid_statuses = ['Pending', 'Confirmed', 'Cancelled', 'Completed']
    if data['status'] not in valid_statuses:
        return jsonify({'error': 'Invalid status'}), 400

    booking.status = data['status']
    db.session.commit()

    return jsonify({'message': 'Booking status updated successfully'}), 200

# Frontend routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    return render_template('admin.html')

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
