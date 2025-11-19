"""
Generated Code Metadata:
========================
Original URL: https://pandana.vip
Prompt: Design a simple RESTful API using Flask for a VIP membership system inspired by Pandana VIP.
Generated: DETERMINISTIC_dbd30932df1df404
Batch ID: 20250622_210840
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
import uuid
import datetime
from functools import wraps
import jwt

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vip_membership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)
    vip_level = db.Column(db.Integer)
    join_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class VIPBenefit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    discount_percentage = db.Column(db.Float)

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
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        public_id=str(uuid.uuid4()),
        username=data['username'],
        password=hashed_password,
        admin=False,
        vip_level=0
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'New user created!'}), 201

@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    
    if not auth or not auth['username'] or not auth['password']:
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(username=auth['username']).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if check_password_hash(user.password, auth['password']):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({'token': token})
    
    return jsonify({'message': 'Wrong credentials'}), 401

@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Admin access required!'}), 403
    
    users = User.query.all()
    output = []
    
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['username'] = user.username
        user_data['vip_level'] = user.vip_level
        user_data['join_date'] = user.join_date
        output.append(user_data)
    
    return jsonify({'users': output})

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Admin access required!'}), 403
    
    user = User.query.filter_by(public_id=public_id).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['username'] = user.username
    user_data['vip_level'] = user.vip_level
    user_data['join_date'] = user.join_date
    
    return jsonify({'user': user_data})

@app.route('/user/<public_id>/upgrade', methods=['PUT'])
@token_required
def upgrade_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Admin access required!'}), 403
    
    user = User.query.filter_by(public_id=public_id).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    data = request.get_json()
    user.vip_level = data['vip_level']
    db.session.commit()
    
    return jsonify({'message': 'User VIP level updated!'})

@app.route('/benefits', methods=['GET'])
def get_all_benefits():
    benefits = VIPBenefit.query.all()
    output = []
    
    for benefit in benefits:
        benefit_data = {}
        benefit_data['level'] = benefit.level
        benefit_data['name'] = benefit.name
        benefit_data['description'] = benefit.description
        benefit_data['discount_percentage'] = benefit.discount_percentage
        output.append(benefit_data)
    
    return jsonify({'benefits': output})

@app.route('/benefits/<level>', methods=['GET'])
def get_one_benefit(level):
    benefit = VIPBenefit.query.filter_by(level=level).first()
    
    if not benefit:
        return jsonify({'message': 'Benefit not found'}), 404
    
    benefit_data = {}
    benefit_data['level'] = benefit.level
    benefit_data['name'] = benefit.name
    benefit_data['description'] = benefit.description
    benefit_data['discount_percentage'] = benefit.discount_percentage
    
    return jsonify({'benefit': benefit_data})

@app.route('/benefits', methods=['POST'])
@token_required
def create_benefit(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Admin access required!'}), 403
    
    data = request.get_json()
    
    new_benefit = VIPBenefit(
        level=data['level'],
        name=data['name'],
        description=data['description'],
        discount_percentage=data['discount_percentage']
    )
    
    db.session.add(new_benefit)
    db.session.commit()
    
    return jsonify({'message': 'New VIP benefit created!'}), 201

@app.route('/benefits/<level>', methods=['PUT'])
@token_required
def update_benefit(current_user, level):
    if not current_user.admin:
        return jsonify({'message': 'Admin access required!'}), 403
    
    benefit = VIPBenefit.query.filter_by(level=level).first()
    
    if not benefit:
        return jsonify({'message': 'Benefit not found'}), 404
    
    data = request.get_json()
    
    benefit.name = data['name']
    benefit.description = data['description']
    benefit.discount_percentage = data['discount_percentage']
    
    db.session.commit()
    
    return jsonify({'message': 'VIP benefit updated!'})

@app.route('/benefits/<level>', methods=['DELETE'])
@token_required
def delete_benefit(current_user, level):
    if not current_user.admin:
        return jsonify({'message': 'Admin access required!'}), 403
    
    benefit = VIPBenefit.query.filter_by(level=level).first()
    
    if not benefit:
        return jsonify({'message': 'Benefit not found'}), 404
    
    db.session.delete(benefit)
    db.session.commit()
    
    return jsonify({'message': 'VIP benefit deleted!'})

# Initialize database tables
with app.app_context():
    db.create_all()

    # Add sample benefits if none exist
    if VIPBenefit.query.count() == 0:
        benefits = [
            VIPBenefit(level=1, name='Bronze', description='Basic VIP benefits', discount_percentage=5.0),
            VIPBenefit(level=2, name='Silver', description='Enhanced VIP benefits', discount_percentage=10.0),
            VIPBenefit(level=3, name='Gold', description='Premium VIP benefits', discount_percentage=15.0),
            VIPBenefit(level=4, name='Platinum', description='Exclusive VIP benefits', discount_percentage=20.0)
        ]
        db.session.bulk_save_objects(benefits)
        db.session.commit()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
