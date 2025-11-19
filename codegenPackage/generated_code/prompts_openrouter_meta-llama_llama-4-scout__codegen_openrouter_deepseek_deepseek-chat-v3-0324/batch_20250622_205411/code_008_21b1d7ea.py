"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Design a RESTful API for a zero-resistance living system, as described in Matt Furey's The Zero Resistance Living System course.
Generated: DETERMINISTIC_21b1d7ead19cd700
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
import uuid
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zero_resistance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# Database Models
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Goal(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)
    
    user = db.relationship('User', backref=db.backref('goals', lazy=True))

class Affirmation(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('affirmations', lazy=True))

class Visualization(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('visualizations', lazy=True))

# Authentication
@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None

# Error Handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

# API Routes
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data or 'email' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'created_at': user.created_at.isoformat()
    }), 201

@app.route('/api/goals', methods=['GET'])
@auth.login_required
def get_goals():
    user = auth.current_user()
    goals = Goal.query.filter_by(user_id=user.id).all()
    return jsonify([{
        'id': goal.id,
        'title': goal.title,
        'description': goal.description,
        'created_at': goal.created_at.isoformat(),
        'completed': goal.completed
    } for goal in goals])

@app.route('/api/goals', methods=['POST'])
@auth.login_required
def create_goal():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    user = auth.current_user()
    goal = Goal(
        user_id=user.id,
        title=data['title'],
        description=data.get('description', '')
    )
    
    db.session.add(goal)
    db.session.commit()
    
    return jsonify({
        'id': goal.id,
        'title': goal.title,
        'description': goal.description,
        'created_at': goal.created_at.isoformat(),
        'completed': goal.completed
    }), 201

@app.route('/api/goals/<goal_id>', methods=['PUT'])
@auth.login_required
def update_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if not goal:
        return jsonify({'error': 'Goal not found'}), 404
    
    if goal.user_id != auth.current_user().id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.get_json()
    if 'title' in data:
        goal.title = data['title']
    if 'description' in data:
        goal.description = data['description']
    if 'completed' in data:
        goal.completed = data['completed']
    
    db.session.commit()
    
    return jsonify({
        'id': goal.id,
        'title': goal.title,
        'description': goal.description,
        'created_at': goal.created_at.isoformat(),
        'completed': goal.completed
    })

@app.route('/api/goals/<goal_id>', methods=['DELETE'])
@auth.login_required
def delete_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if not goal:
        return jsonify({'error': 'Goal not found'}), 404
    
    if goal.user_id != auth.current_user().id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    db.session.delete(goal)
    db.session.commit()
    
    return jsonify({'message': 'Goal deleted successfully'}), 200

@app.route('/api/affirmations', methods=['GET'])
@auth.login_required
def get_affirmations():
    user = auth.current_user()
    affirmations = Affirmation.query.filter_by(user_id=user.id).all()
    return jsonify([{
        'id': affirmation.id,
        'text': affirmation.text,
        'created_at': affirmation.created_at.isoformat()
    } for affirmation in affirmations])

@app.route('/api/affirmations', methods=['POST'])
@auth.login_required
def create_affirmation():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Text is required'}), 400
    
    user = auth.current_user()
    affirmation = Affirmation(
        user_id=user.id,
        text=data['text']
    )
    
    db.session.add(affirmation)
    db.session.commit()
    
    return jsonify({
        'id': affirmation.id,
        'text': affirmation.text,
        'created_at': affirmation.created_at.isoformat()
    }), 201

@app.route('/api/visualizations', methods=['GET'])
@auth.login_required
def get_visualizations():
    user = auth.current_user()
    visualizations = Visualization.query.filter_by(user_id=user.id).all()
    return jsonify([{
        'id': visualization.id,
        'description': visualization.description,
        'created_at': visualization.created_at.isoformat()
    } for visualization in visualizations])

@app.route('/api/visualizations', methods=['POST'])
@auth.login_required
def create_visualization():
    data = request.get_json()
    if not data or 'description' not in data:
        return jsonify({'error': 'Description is required'}), 400
    
    user = auth.current_user()
    visualization = Visualization(
        user_id=user.id,
        description=data['description']
    )
    
    db.session.add(visualization)
    db.session.commit()
    
    return jsonify({
        'id': visualization.id,
        'description': visualization.description,
        'created_at': visualization.created_at.isoformat()
    }), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app
