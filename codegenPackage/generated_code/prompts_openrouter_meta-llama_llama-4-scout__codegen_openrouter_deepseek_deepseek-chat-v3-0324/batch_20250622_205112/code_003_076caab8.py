"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: "Design a networking app for coworking spaces in Switzerland, incorporating features mentioned in NetCoworking's articles on optimizing networking."
Generated: DETERMINISTIC_076caab898cfd6c5
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
NetCoworking Switzerland - Networking App for Coworking Spaces

Features:
- User profiles with professional details
- Space listings with amenities
- Event management
- Networking recommendations
- Messaging system
- Analytics dashboard
"""

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    profession = db.Column(db.String(100))
    company = db.Column(db.String(100))
    bio = db.Column(db.Text)
    skills = db.Column(db.String(200))
    interests = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    spaces = db.relationship('Space', backref='owner', lazy=True)
    events = db.relationship('Event', backref='organizer', lazy=True)
    messages_sent = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy=True)
    messages_received = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient', lazy=True)
    connections = db.relationship('Connection', foreign_keys='Connection.user_id', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Space(db.Model):
    __tablename__ = 'spaces'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    canton = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    amenities = db.Column(db.String(200))
    capacity = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    events = db.relationship('Event', backref='space', lazy=True)

class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    space_id = db.Column(db.Integer, db.ForeignKey('spaces.id'), nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    max_attendees = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    attendees = db.relationship('EventAttendee', backref='event', lazy=True)

class EventAttendee(db.Model):
    __tablename__ = 'event_attendees'
    
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)

class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject = db.Column(db.String(100))
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)

class Connection(db.Model):
    __tablename__ = 'connections'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    connected_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    connected_at = db.Column(db.DateTime, default=datetime.utcnow)
    strength = db.Column(db.Integer, default=1)  # 1-5 scale
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'connected_user_id', name='unique_connection'),
    )

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            password = request.form.get('password')
            
            if not all([email, first_name, last_name, password]):
                return jsonify({'error': 'Missing required fields'}), 400
            
            if User.query.filter_by(email=email).first():
                return jsonify({'error': 'Email already registered'}), 400
            
            user = User(
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            
            login_user(user)
            return jsonify({'message': 'Registration successful'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')
            
            if not all([email, password]):
                return jsonify({'error': 'Missing email or password'}), 400
            
            user = User.query.filter_by(email=email).first()
            
            if not user or not user.check_password(password):
                return jsonify({'error': 'Invalid credentials'}), 401
            
            login_user(user)
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            return jsonify({'message': 'Login successful'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        try:
            data = request.form
            current_user.profession = data.get('profession')
            current_user.company = data.get('company')
            current_user.bio = data.get('bio')
            current_user.skills = data.get('skills')
            current_user.interests = data.get('interests')
            db.session.commit()
            return jsonify({'message': 'Profile updated successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    return render_template('profile.html', user=current_user)

@app.route('/spaces', methods=['GET'])
def list_spaces():
    try:
        canton = request.args.get('canton')
        query = Space.query
        
        if canton:
            query = query.filter_by(canton=canton)
        
        spaces = query.all()
        return jsonify([{
            'id': space.id,
            'name': space.name,
            'address': space.address,
            'city': space.city,
            'canton': space.canton,
            'description': space.description,
            'amenities': space.amenities.split(',') if space.amenities else []
        } for space in spaces]),
