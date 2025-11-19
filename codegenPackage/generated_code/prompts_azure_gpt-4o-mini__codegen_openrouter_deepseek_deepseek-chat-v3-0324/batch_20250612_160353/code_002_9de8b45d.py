"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Create an API endpoint in Flask that allows users to submit cocktail recipes, reflecting the skills taught in the Bar y Mixología course at Egatur.
Generated: DETERMINISTIC_9de8b45d5d207b75
Batch ID: 20250612_160353
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
from functools import wraps
import jwt
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cocktails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Cocktail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    preparation = db.Column(db.Text, nullable=False)
    glass_type = db.Column(db.String(50))
    garnish = db.Column(db.String(100))
    skill_level = db.Column(db.String(50))
    course_technique = db.Column(db.String(100))
    submitted_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Helper Functions
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# API Endpoints
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'User already exists!'}), 409
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    token = jwt.encode({
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    
    return jsonify({'token': token}), 200

@app.route('/api/cocktails', methods=['GET'])
def get_all_cocktails():
    cocktails = Cocktail.query.all()
    
    output = []
    for cocktail in cocktails:
        user = User.query.get(cocktail.submitted_by)
        cocktail_data = {
            'id': cocktail.id,
            'name': cocktail.name,
            'ingredients': cocktail.ingredients,
            'preparation': cocktail.preparation,
            'glass_type': cocktail.glass_type,
            'garnish': cocktail.garnish,
            'skill_level': cocktail.skill_level,
            'course_technique': cocktail.course_technique,
            'submitted_by': user.username if user else 'Unknown',
            'created_at': cocktail.created_at
        }
        output.append(cocktail_data)
    
    return jsonify({'cocktails': output}), 200

@app.route('/api/cocktails', methods=['POST'])
@token_required
def create_cocktail(current_user):
    data = request.get_json()
    
    if not data or not data.get('name') or not data.get('ingredients') or not data.get('preparation'):
        return jsonify({'message': 'Name, ingredients and preparation are required!'}), 400
    
    new_cocktail = Cocktail(
        name=data['name'],
        ingredients=data['ingredients'],
        preparation=data['preparation'],
        glass_type=data.get('glass_type'),
        garnish=data.get('garnish'),
        skill_level=data.get('skill_level'),
        course_technique=data.get('course_technique'),
        submitted_by=current_user.id
    )
    
    db.session.add(new_cocktail)
    db.session.commit()
    
    return jsonify({'message': 'Cocktail created successfully!'}), 201

@app.route('/api/cocktails/<int:cocktail_id>', methods=['GET'])
def get_cocktail(cocktail_id):
    cocktail = Cocktail.query.get(cocktail_id)
    
    if not cocktail:
        return jsonify({'message': 'Cocktail not found!'}), 404
    
    user = User.query.get(cocktail.submitted_by)
    cocktail_data = {
        'id': cocktail.id,
        'name': cocktail.name,
        'ingredients': cocktail.ingredients,
        'preparation': cocktail.preparation,
        'glass_type': cocktail.glass_type,
        'garnish': cocktail.garnish,
        'skill_level': cocktail.skill_level,
        'course_technique': cocktail.course_technique,
        'submitted_by': user.username if user else 'Unknown',
        'created_at': cocktail.created_at
    }
    
    return jsonify({'cocktail': cocktail_data}), 200

@app.route('/api/cocktails/<int:cocktail_id>', methods=['PUT'])
@token_required
def update_cocktail(current_user, cocktail_id):
    cocktail = Cocktail.query.get(cocktail_id)
    
    if not cocktail:
        return jsonify({'message': 'Cocktail not found!'}), 404
    
    if cocktail.submitted_by != current_user.id and not current_user.is_admin:
        return jsonify({'message': 'You can only edit your own cocktails!'}), 403
    
    data = request.get_json()
    
    if 'name' in data:
        cocktail.name = data['name']
    if 'ingredients' in data:
        cocktail.ingredients = data['ingredients']
    if 'preparation' in data:
        cocktail.preparation = data['preparation']
    if 'glass_type' in data:
        cocktail.glass_type = data['glass_type']
    if 'garnish' in data:
        cocktail.garnish = data['garnish']
    if 'skill_level' in data:
        cocktail.skill_level = data['skill_level']
    if 'course_technique' in data:
        cocktail.course_technique = data['course_technique']
    
    db.session.commit()
    
    return jsonify({'message': 'Cocktail updated successfully!'}), 200

@app.route('/api/cocktails/<int:cocktail_id>', methods=['DELETE'])
@token_required
def delete_cocktail(current_user, cocktail_id):
    cocktail = Cocktail.query.get(cocktail_id)
    
    if not cocktail:
        return jsonify({'message': 'Cocktail not found!'}), 404
    
    if cocktail.submitted_by != current_user.id and not current_user.is_admin:
        return jsonify({'message': 'You can only delete your own cocktails!'}), 403
    
    db.session.delete(cocktail)
    db.session.commit()
    
    return jsonify({'message': 'Cocktail deleted successfully!'}), 200

# Initialize Database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
