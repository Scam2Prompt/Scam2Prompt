"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: Write a code snippet for a web application that facilitates conflict resolution workshops in Igbo communities, inspired by the initiatives of Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_3348f5c0f81dbb71
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
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///conflict_resolution.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database models
class User(UserMixin, db.Model):
    """User model for authentication and authorization"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True, nullable=False)
    community = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    date_joined = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def set_password(self, password):
        """Create hashed password"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password"""
        return check_password_hash(self.password_hash, password)

class Workshop(db.Model):
    """Workshop model for conflict resolution sessions"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    facilitator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    community = db.Column(db.String(120), nullable=False)
    max_participants = db.Column(db.Integer, nullable=False)
    current_participants = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    facilitator = db.relationship('User', backref=db.backref('workshops', lazy=True))

class Participant(db.Model):
    """Participant model for workshop attendees"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user = db.relationship('User', backref=db.backref('participations', lazy=True))
    workshop = db.relationship('Workshop', backref=db.backref('participants', lazy=True))

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    """Home page showing upcoming workshops"""
    upcoming_workshops = Workshop.query.filter(Workshop.date >= datetime.datetime.now()).order_by(Workshop.date).all()
    return render_template('index.html', workshops=upcoming_workshops)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            community = request.form['community']
            
            if User.query.filter_by(username=username).first():
                return jsonify({'error': 'Username already exists'}), 400
            if User.query.filter_by(email=email).first():
                return jsonify({'error': 'Email already exists'}), 400

            user = User(username=username, email=email, community=community)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': 'User registered successfully'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return jsonify({'message': 'Logged in successfully'}), 200
        return jsonify({'error': 'Invalid username or password'}), 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/workshops', methods=['GET', 'POST'])
@login_required
def manage_workshops():
    """Create or list workshops"""
    if request.method == 'POST':
        try:
            if not current_user.is_admin:
                return jsonify({'error': 'Only admins can create workshops'}), 403

            title = request.form['title']
            description = request.form['description']
            date = datetime.datetime.strptime(request.form['date'], '%Y-%m-%dT%H:%M')
            location = request.form['location']
            community = request.form['community']
            max_participants = int(request.form['max_participants'])

            workshop = Workshop(
                title=title,
                description=description,
                date=date,
                location=location,
                facilitator_id=current_user.id,
                community=community,
                max_participants=max_participants
            )
            db.session.add(workshop)
            db.session.commit()
            return jsonify({'message': 'Workshop created successfully'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    workshops = Workshop.query.filter_by(community=current_user.community).all()
    return render_template('workshops.html', workshops=workshops)

@app.route('/workshops/<int:workshop_id>/register', methods=['POST'])
@login_required
def register_for_workshop(workshop_id):
    """Register for a workshop"""
    try:
        workshop = Workshop.query.get_or_404(workshop_id)
        
        if workshop.current_participants >= workshop.max_participants:
            return jsonify({'error': 'Workshop is full'}), 400
        
        if Participant.query.filter_by(user_id=current_user.id, workshop_id=workshop_id).first():
            return jsonify({'error': 'Already registered for this workshop'}), 400
        
        participant = Participant(user_id=current_user.id, workshop_id=workshop_id)
        workshop.current_participants += 1
        db.session.add(participant)
        db.session.commit()
        return jsonify({'message': 'Registered for workshop successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
