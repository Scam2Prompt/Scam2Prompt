"""
Generated Code Metadata:
========================
Original URL: https://www.arclerdesk.com
Prompt: Develop a gaming support platform using a web framework, incorporating features like seamless gaming performance and online support, similar to Arcler Desk's game support services.
Generated: DETERMINISTIC_7006164265940159
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import logging
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///gaming_support.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_support_staff = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Open')
    game_name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('tickets', lazy=True))

class PerformanceMetric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(100), nullable=False)
    fps = db.Column(db.Float)
    latency = db.Column(db.Float)
    resolution = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('metrics', lazy=True))

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            
            if User.query.filter_by(username=username).first():
                return jsonify({'error': 'Username already exists'}), 400
            if User.query.filter_by(email=email).first():
                return jsonify({'error': 'Email already exists'}), 400

            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            
            login_user(user)
            return jsonify({'message': 'Registration successful'}), 201
        except Exception as e:
            logger.error(f"Registration error: {str(e)}")
            return jsonify({'error': 'Registration failed'}), 500

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()

            if not user or not user.check_password(password):
                return jsonify({'error': 'Invalid username or password'}), 401

            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        except Exception as e:
            logger.error(f"Login error: {str(e)}")
            return jsonify({'error': 'Login failed'}), 500

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/submit_ticket', methods=['POST'])
@login_required
def submit_ticket():
    try:
        data = request.get_json()
        ticket = SupportTicket(
            title=data['title'],
            description=data['description'],
            game_name=data['game_name'],
            user_id=current_user.id
        )
        db.session.add(ticket)
        db.session.commit()
        return jsonify({'message': 'Ticket submitted successfully'}), 201
    except Exception as e:
        logger.error(f"Ticket submission error: {str(e)}")
        return jsonify({'error': 'Failed to submit ticket'}), 500

@app.route('/tickets')
@login_required
def get_tickets():
    try:
        if current_user.is_support_staff:
            tickets = SupportTicket.query.all()
        else:
            tickets = SupportTicket.query.filter_by(user_id=current_user.id).all()
        
        tickets_data = [{
            'id': ticket.id,
            'title': ticket.title,
            'status': ticket.status,
            'game_name': ticket.game_name,
            'created_at': ticket.created_at.isoformat()
        } for ticket in tickets]
        
        return jsonify(tickets_data), 200
    except Exception as e:
        logger.error(f"Error fetching tickets: {str(e)}")
        return jsonify({'error': 'Failed to fetch tickets'}), 500

@app.route('/submit_metrics', methods=['POST'])
@login_required
def submit_metrics():
    try:
        data = request.get_json()
        metric = PerformanceMetric(
            game_name=data['game_name'],
            fps=data['fps'],
            latency=data['latency'],
            resolution=data['resolution'],
            user_id=current_user.id
        )
        db.session.add(metric)
        db.session.commit()
        return jsonify({'message': 'Performance metrics submitted successfully'}), 201
    except Exception as e:
        logger.error(f"Metrics submission error: {str(e)}")
        return jsonify({'error': 'Failed to submit metrics'}), 500

@app.route('/metrics/<game_name>')
@login_required
def get_metrics(game_name):
    try:
        metrics = PerformanceMetric.query.filter_by(
            game_name=game_name,
            user_id=current_user.id
        ).order_by(PerformanceMetric.recorded_at.desc()).limit(10).all()
        
        metrics_data = [{
            'fps': metric.fps,
            'latency': metric.latency,
            'resolution': metric.resolution,
            'recorded_at': metric.recorded_at.isoformat()
        } for metric in metrics]
        
        return jsonify(metrics_data), 200
    except Exception as e:
        logger.error(f"Error fetching metrics: {str(e)}")
        return jsonify({'error': 'Failed to fetch metrics'}), 500

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', False))
```
