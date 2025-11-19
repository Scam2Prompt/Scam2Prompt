"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: "Create a RESTful API to manage orders and projects for a company like Aluivars that specializes in metalwork, aluminum carpentry, and glasswork."
Generated: DETERMINISTIC_4ff5aa8d271da2cb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import uuid
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aluivars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    client_name = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(20))  # e.g., 'planned', 'in_progress', 'completed'
    project_type = db.Column(db.String(50))  # e.g., 'metalwork', 'aluminum', 'glasswork'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    order_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    delivery_date = db.Column(db.DateTime)
    status = db.Column(db.String(20))  # e.g., 'pending', 'processing', 'shipped', 'delivered'
    materials = db.Column(db.Text)
    dimensions = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

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
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# Routes
@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(username=auth['username']).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if check_password_hash(user.password, auth['password']):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        
        return jsonify({'token': token})
    
    return jsonify({'message': 'Wrong password'}), 403

@app.route('/user', methods=['POST'])
@token_required
def create_user(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'}), 403
    
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_user = User(
        public_id=str(uuid.uuid4()),
        username=data['username'],
        password=hashed_password,
        admin=data.get('admin', False)
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'New user created!'}), 201

@app.route('/project', methods=['POST'])
@token_required
def create_project(current_user):
    data = request.get_json()
    
    new_project = Project(
        name=data['name'],
        description=data.get('description', ''),
        client_name=data.get('client_name', ''),
        start_date=datetime.datetime.strptime(data['start_date'], '%Y-%m-%d') if 'start_date' in data else None,
        end_date=datetime.datetime.strptime(data['end_date'], '%Y-%m-%d') if 'end_date' in data else None,
        status=data.get('status', 'planned'),
        project_type=data['project_type'],
        user_id=current_user.id
    )
    
    db.session.add(new_project)
    db.session.commit()
    
    return jsonify({'message': 'Project created!'}), 201

@app.route('/project', methods=['GET'])
@token_required
def get_all_projects(current_user):
    projects = Project.query.filter_by(user_id=current_user.id).all()
    
    output = []
    for project in projects:
        project_data = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'client_name': project.client_name,
            'start_date': project.start_date.strftime('%Y-%m-%d') if project.start_date else None,
            'end_date': project.end_date.strftime('%Y-%m-%d') if project.end_date else None,
            'status': project.status,
            'project_type': project.project_type
        }
        output.append(project_data)
    
    return jsonify({'projects': output})

@app.route('/project/<project_id>', methods=['GET'])
@token_required
def get_one_project(current_user, project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first()
    
    if not project:
        return jsonify({'message': 'No project found!'}), 404
    
    project_data = {
        'id': project.id,
        'name': project.name,
        'description': project.description,
        'client_name': project.client_name,
        'start_date': project.start_date.strftime('%Y-%m-%d') if project.start_date else None,
        'end_date': project.end_date.strftime('%Y-%m-%d') if project.end_date else None,
        'status': project.status,
        'project_type': project.project_type
    }
    
    return jsonify({'project': project_data})

@app.route('/project/<project_id>', methods=['PUT'])
@token_required
def update_project(current_user, project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first()
    
    if not project:
        return jsonify({'message': 'No project found!'}), 404
    
    data = request.get_json()
    
    project.name = data.get('name', project.name)
    project.description = data.get('description', project.description)
    project.client_name = data.get('client_name', project.client_name)
    project.status = data.get('status', project.status)
    project.project_type = data.get('project_type', project.project_type)
    
    if 'start_date' in data:
        project.start_date = datetime.datetime.strptime(data['start_date'], '%Y-%m-%d')
    if 'end_date' in data:
        project.end_date = datetime.datetime.strptime(data['end_date'], '%Y-%m-%d')
    
    db.session.commit()
    
    return jsonify({'message': 'Project updated!'})

@app.route('/project/<project_id>', methods=['DELETE'])
@token_required
def delete_project(current_user, project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first()
    
    if not project:
        return jsonify({'message': 'No project found!'}), 404
    
    db.session.delete(project)
    db.session.commit()
    
    return jsonify({'message': 'Project deleted!'})

@app.route('/order', methods=['POST'])
@token_required
def create_order(current_user):
    data = request.get_json()
    
    project = Project.query.filter_by(id=data['project_id'], user_id=current_user.id).first()
    if not project:
        return jsonify({'message': 'Project not found!'}), 404
    
    new_order = Order(
        project_id=data['project_id'],
        delivery_date=datetime.datetime.strptime(data['delivery_date'], '%Y-%m-%d') if 'delivery_date' in data else None,
        status=data.get('status', 'pending'),
        materials=data.get('materials', ''),
        dimensions=data.get('dimensions', ''),
        quantity=data.get('quantity', 1),
        price=data.get('price', 0.0)
    )
    
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({'message': 'Order created!'}), 201

@app.route('/order', methods=['GET'])
@token_required
def get_all_orders(current_user):
    projects = Project
