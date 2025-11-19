"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Generate code to facilitate communication between ERP freelancers and employers using live chat functionality, as described on ERPIFY.
Generated: DETERMINISTIC_cd7cd116209b6137
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
from flask import Flask, render_template, request, jsonify, session
from flask_socketio import SocketIO, emit, join_room, leave_room
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///erpify.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
socketio = SocketIO(app)

# Database Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    user_type = db.Column(db.String(20), nullable=False)  # 'freelancer' or 'employer'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class ChatRoom(db.Model):
    __tablename__ = 'chat_rooms'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    freelancer_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    employer_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    freelancer = db.relationship('User', foreign_keys=[freelancer_id])
    employer = db.relationship('User', foreign_keys=[employer_id])

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    room_id = db.Column(db.String(36), db.ForeignKey('chat_rooms.id'), nullable=False)
    sender_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)

    room = db.relationship('ChatRoom')
    sender = db.relationship('User')

# Create database tables
with app.app_context():
    db.create_all()

# Authentication routes
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user_type = data.get('user_type')

        if not all([username, email, password, user_type]):
            return jsonify({'error': 'Missing required fields'}), 400

        if user_type not in ['freelancer', 'employer']:
            return jsonify({'error': 'Invalid user type'}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400

        user = User(username=username, email=email, user_type=user_type)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully', 'user_id': user.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not all([username, password]):
            return jsonify({'error': 'Missing username or password'}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid username or password'}), 401

        session['user_id'] = user.id
        session['user_type'] = user.user_type

        return jsonify({
            'message': 'Login successful',
            'user_id': user.id,
            'user_type': user.user_type
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'}), 200

# Chat routes
@app.route('/chat/rooms', methods=['GET'])
def get_chat_rooms():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'Unauthorized'}), 401

        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        if user.user_type == 'freelancer':
            rooms = ChatRoom.query.filter_by(freelancer_id=user_id).all()
        else:
            rooms = ChatRoom.query.filter_by(employer_id=user_id).all()

        room_list = []
        for room in rooms:
            other_user = room.freelancer if user.user_type == 'employer' else room.employer
            last_message = Message.query.filter_by(room_id=room.id).order_by(Message.created_at.desc()).first()
            
            room_data = {
                'room_id': room.id,
                'other_user': {
                    'id': other_user.id,
                    'username': other_user.username,
                    'user_type': other_user.user_type
                },
                'last_message': {
                    'content': last_message.content if last_message else None,
                    'timestamp': last_message.created_at.isoformat() if last_message else None,
                    'is_read': last_message.is_read if last_message else None
                },
                'updated_at': room.updated_at.isoformat()
            }
            room_list.append(room_data)

        return jsonify({'rooms': room_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chat/messages/<room_id>', methods=['GET'])
def get_messages(room_id):
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'Unauthorized'}), 401

        room = ChatRoom.query.get(room_id)
        if not room:
            return jsonify({'error': 'Room not found'}), 404

        if user_id not in [room.freelancer_id, room.employer_id]:
            return jsonify({'error': 'Unauthorized access to room'}), 403

        messages = Message.query.filter_by(room_id=room_id).order_by(Message.created_at.asc()).all()
        message_list = []
        for message in messages:
            message_list.append({
                'id': message.id,
                'sender_id': message.sender_id,
                'content': message.content,
                'timestamp': message.created_at.isoformat(),
                'is_read': message.is_read
            })

        # Mark messages as read
        Message.query.filter_by(room_id=room_id, is_read=False).filter(Message.sender_id != user_id).update({'is_read': True})
        db.session.commit()

        return jsonify({'messages': message_list}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/chat/create', methods=['POST'])
def create_chat_room():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'Unauthorized'}), 401

        data = request.get_json()
        other_user_id = data.get('other_user_id')
        if not other_user_id:
            return jsonify({'error': 'Missing other_user_id'}), 400

        user = User.query.get(user_id)
        other_user = User.query.get(other_user_id)
        if not user or not other_user:
            return jsonify({'error': 'User not found'}), 404

        # Check if room already exists
        if user.user_type == 'freelancer':
            room = ChatRoom.query.filter_by(freelancer_id=user_id, employer_id=other_user_id).first()
        else:
            room = ChatRoom.query.filter_by(freelancer_id=other_user_id, employer
