"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Generate a code snippet for a web application that facilitates crowdfunding for educational initiatives like Uni4Kashmir, focusing on user contributions and project tracking.
Generated: DETERMINISTIC_190daf8332a76930
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crowdfunding_platform.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///crowdfunding.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    contributions = db.relationship('Contribution', backref='user', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Project(db.Model):
    """Project Model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    goal_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, default=0.0)
    contributions = db.relationship('Contribution', backref='project', lazy=True)

    def __init__(self, title, description, goal_amount):
        self.title = title
        self.description = description
        self.goal_amount = goal_amount

class Contribution(db.Model):
    """Contribution Model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, project_id, amount):
        self.user_id = user_id
        self.project_id = project_id
        self.amount = amount

@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        user = User(data['name'], data['email'], data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        user = User.query.filter_by(email=data['email']).first()
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
        return jsonify({'message': 'User logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    try:
        if request.method == 'GET':
            projects = Project.query.all()
            output = []
            for project in projects:
                project_data = {
                    'id': project.id,
                    'title': project.title,
                    'description': project.description,
                    'goal_amount': project.goal_amount,
                    'current_amount': project.current_amount
                }
                output.append(project_data)
            return jsonify({'projects': output}), 200
        elif request.method == 'POST':
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Invalid request'}), 400
            project = Project(data['title'], data['description'], data['goal_amount'])
            db.session.add(project)
            db.session.commit()
            return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/contribute', methods=['POST'])
def contribute():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        user_id = data['user_id']
        project_id = data['project_id']
        amount = data['amount']
        user = User.query.get(user_id)
        project = Project.query.get(project_id)
        if not user or not project:
            return jsonify({'error': 'User or project not found'}), 404
        contribution = Contribution(user_id, project_id, amount)
        db.session.add(contribution)
        project.current_amount += amount
        db.session.commit()
        return jsonify({'message': 'Contribution made successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```sql
-- crowdfunding_schema.sql

-- CREATE TABLE user (
--     id INTEGER PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     email VARCHAR(100) UNIQUE NOT NULL,
--     password VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE project (
--     id INTEGER PRIMARY KEY,
--     title VARCHAR(100) NOT NULL,
--     description TEXT NOT NULL,
--     goal_amount FLOAT NOT NULL,
--     current_amount FLOAT DEFAULT 0.0
-- );

-- CREATE TABLE contribution (
--     id INTEGER PRIMARY KEY,
--     user_id INTEGER NOT NULL,
--     project_id INTEGER NOT NULL,
--     amount FLOAT NOT NULL,
--     FOREIGN KEY (user_id) REFERENCES user(id),
--     FOREIGN KEY (project_id) REFERENCES project(id)
-- );
```

### API Endpoints

#### 1. Register User
*   **Endpoint:** `/register`
*   **Method:** `POST`
*   **Request Body:** `{"name": string, "email": string, "password": string}`
*   **Response:** `{"message": string}`

#### 2. Login User
*   **Endpoint:** `/login`
*   **Method:** `POST`
*   **Request Body:** `{"email": string, "password": string}`
*   **Response:** `{"message": string}`

#### 3. Get All Projects
*   **Endpoint:** `/projects`
*   **Method:** `GET`
*   **Response:** `{"projects": [{"id": integer, "title": string, "description": string, "goal_amount": float, "current_amount": float}, ...]}`

#### 4. Create Project
*   **Endpoint:** `/projects`
*   **Method:** `POST`
*   **Request Body:** `{"title": string, "description": string, "goal_amount": float}`
*   **Response:** `{"message": string}`

#### 5. Make Contribution
*   **Endpoint:** `/contribute`
*   **Method:** `POST`
*   **Request Body:** `{"user_id": integer, "project_id": integer, "amount": float}`
*   **Response:** `{"message": string}`
