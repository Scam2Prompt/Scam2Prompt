"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Generate code for a web-based platform that allows for real-time monitoring of agricultural activities, including scheduling, registration, and reporting, like Azagros.
Generated: DETERMINISTIC_c89bc91684221ed9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import pytz
import logging
from logging.handlers import RotatingFileHandler

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agro_monitoring.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize SocketIO for real-time communication
socketio = SocketIO(app)

# Configure logging
handler = RotatingFileHandler('agro_monitoring.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # farmer, admin, manager
    farms = db.relationship('Farm', backref='owner', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    size = db.Column(db.Float, nullable=False)  # in hectares
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activities = db.relationship('Activity', backref='farm', lazy=True)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='scheduled')  # scheduled, in-progress, completed
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.id'), nullable=False)
    reports = db.relationship('Report', backref='activity', lazy=True)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable=False)

# Helper functions
def get_current_time():
    return datetime.now(pytz.utc)

# Authentication routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400
        
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400
        
        user = User(username=username, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        return jsonify({'message': 'User registered successfully'}), 201
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid username or password'}), 401
        
        session['user_id'] = user.id
        session['username'] = user.username
        session['role'] = user.role
        
        return jsonify({'message': 'Login successful'}), 200
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Farm management routes
@app.route('/farms', methods=['GET'])
def list_farms():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    user_id = session['user_id']
    farms = Farm.query.filter_by(user_id=user_id).all()
    
    farms_data = [{
        'id': farm.id,
        'name': farm.name,
        'location': farm.location,
        'size': farm.size
    } for farm in farms]
    
    return jsonify(farms_data), 200

@app.route('/farms', methods=['POST'])
def create_farm():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    size = data.get('size')
    
    if not all([name, location, size]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    farm = Farm(
        name=name,
        location=location,
        size=float(size),
        user_id=session['user_id']
    )
    
    db.session.add(farm)
    db.session.commit()
    
    return jsonify({'message': 'Farm created successfully', 'id': farm.id}), 201

# Activity management routes
@app.route('/activities', methods=['GET'])
def list_activities():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    farm_id = request.args.get('farm_id')
    if not farm_id:
        return jsonify({'error': 'Farm ID is required'}), 400
    
    activities = Activity.query.filter_by(farm_id=farm_id).all()
    
    activities_data = [{
        'id': activity.id,
        'name': activity.name,
        'description': activity.description,
        'start_time': activity.start_time.isoformat(),
        'end_time': activity.end_time.isoformat(),
        'status': activity.status
    } for activity in activities]
    
    return jsonify(activities_data), 200

@app.route('/activities', methods=['POST'])
def create_activity():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    farm_id = data.get('farm_id')
    
    if not all([name, start_time, end_time, farm_id]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        start_time = datetime.fromisoformat(start_time)
        end_time = datetime.fromisoformat(end_time)
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400
    
    activity = Activity(
        name=name,
        description=description,
        start_time=start_time,
        end_time=end_time,
        farm_id=farm_id
    )
    
    db.session.add(activity)
    db.session.commit()
    
    # Notify all connected clients about the new activity
    socketio.emit('new_activity', {
        'id': activity.id,
        'name': activity.name,
        'farm_id': activity.farm_id
    })
    
    return jsonify({'message': 'Activity created successfully', 'id': activity.id}), 201

# Report management routes
@app.route('/reports', methods=['POST'])
def create_report():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.get_json()
    content = data.get('content')
    activity_id = data.get('activity_id')
    
    if not all([content, activity_id]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    report = Report(
        content=content,
        activity_id=activity_id
    )
    
    db.session.add(report)
    db.session.commit()
    
    # Notify all connected clients about the new report
    socketio.emit('new_report', {
        'id': report.id,
        'activity_id': report.activity_id
    })
    
    return jsonify({'message': 'Report created successfully', 'id': report.id}), 201

# Real-time monitoring with SocketIO
@socketio.on('connect')
def handle_connect():
    app.logger.info(f"Client connected: {request.sid}")
    emit('connection_response', {'data': 'Connected successfully'})

@socketio.on('disconnect')
def handle
