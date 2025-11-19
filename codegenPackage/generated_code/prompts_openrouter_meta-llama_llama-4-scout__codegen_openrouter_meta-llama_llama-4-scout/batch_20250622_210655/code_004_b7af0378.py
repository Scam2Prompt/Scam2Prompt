"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Create a freelancer platform API to connect businesses with Oracle ERP experts.
Generated: DETERMINISTIC_b7af03782b4a4161
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Freelancer Platform API**
==========================

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """Base user model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Business(db.Model):
    """Business model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('businesses', lazy=True))

class Expert(db.Model):
    """Oracle ERP expert model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('expert_profile', lazy=True))

class Project(db.Model):
    """Project model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    business = db.relationship('Business', backref=db.backref('projects', lazy=True))
    expert_id = db.Column(db.Integer, db.ForeignKey('expert.id'), nullable=True)
    expert = db.relationship('Expert', backref=db.backref('assigned_projects', lazy=True))
    status = db.Column(db.String(50), nullable=False, default='open')

class Bid(db.Model):
    """Bid model"""
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('bids', lazy=True))
    expert_id = db.Column(db.Integer, db.ForeignKey('expert.id'), nullable=False)
    expert = db.relationship('Expert', backref=db.backref('bids', lazy=True))
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
```

**routes.py**
```python
from flask import Flask, request, jsonify
from models import db, User, Business, Expert, Project, Bid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///freelancer.db'
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    user = User(name=data['name'], email=data['email'], role=data['role'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Login a user"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/businesses', methods=['POST'])
def create_business():
    """Create a new business"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    business = Business(name=data['name'], description=data['description'], user_id=data['user_id'])
    db.session.add(business)
    db.session.commit()
    return jsonify({'message': 'Business created successfully'}), 201

@app.route('/experts', methods=['POST'])
def create_expert():
    """Create a new Oracle ERP expert"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    expert = Expert(name=data['name'], description=data['description'], skills=data['skills'], user_id=data['user_id'])
    db.session.add(expert)
    db.session.commit()
    return jsonify({'message': 'Expert created successfully'}), 201

@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    project = Project(title=data['title'], description=data['description'], business_id=data['business_id'])
    db.session.add(project)
    db.session.commit()
    return jsonify({'message': 'Project created successfully'}), 201

@app.route('/projects/<int:project_id>/bids', methods=['POST'])
def create_bid(project_id):
    """Create a new bid for a project"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    bid = Bid(project_id=project_id, expert_id=data['expert_id'], amount=data['amount'], description=data['description'])
    db.session.add(bid)
    db.session.commit()
    return jsonify({'message': 'Bid created successfully'}), 201

@app.route('/projects/<int:project_id>/assign', methods=['PATCH'])
def assign_expert(project_id):
    """Assign an expert to a project"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    expert = Expert.query.get(data['expert_id'])
    if not expert:
        return jsonify({'error': 'Expert not found'}), 404
    project.expert_id = data['expert_id']
    project.status = 'assigned'
    db.session.commit()
    return jsonify({'message': 'Expert assigned successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
```

**.gitignore**
```
freelancer.db
```

**README.md**
```markdown
# Freelancer Platform API

## Endpoints

### Register
* **POST /register**: Register a new user
* Request Body: `name`, `email`, `password`, `role`

### Login
* **POST /login**: Login a user
* Request Body: `email`, `password`

### Businesses
* **POST /businesses**: Create a new business
* Request Body: `name`, `description`, `user_id`

### Experts
* **POST /experts**: Create a new Oracle ERP expert
* Request Body: `name`, `description`, `skills`, `user_id`

### Projects
* **POST /projects**: Create a new project
* Request Body: `title`, `description`, `business_id`

### Bids
* **POST /projects/<int:project_id>/bids**: Create a new bid for a project
* Request Body: `expert_id`, `amount`, `description`

### Assign Expert
* **PATCH /projects/<int:project_id>/assign**: Assign an expert to a project
* Request Body: `expert_id`
```
