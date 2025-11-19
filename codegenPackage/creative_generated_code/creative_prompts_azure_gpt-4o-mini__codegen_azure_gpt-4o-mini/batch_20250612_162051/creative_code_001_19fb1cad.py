"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unimeleducacion.org
Prompt: How can I implement a digital learning environment using resources from the "Curso online de Generación de Actividades y Uso de PDI con Tablets y Dispositivos Móviles" provided by Unimel Educación?
Generated: DETERMINISTIC_19fb1cad9f2409a6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learning_environment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)

# User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Lesson model to store learning resources
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['POST'])
def register():
    """Endpoint to register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists!'}), 400

    # Create a new user and add to the database
    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    # Check username and password
    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'error': 'Invalid username or password!'}), 401

@app.route('/logout')
@login_required
def logout():
    """Endpoint for user logout."""
    logout_user()
    return jsonify({'message': 'Logged out successfully!'}), 200

@app.route('/lessons', methods=['GET', 'POST'])
@login_required
def manage_lessons():
    """Endpoint to retrieve or create lessons."""
    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        
        # Validate input
        if not title or not content:
            return jsonify({'error': 'Title and content are required!'}), 400

        # Create a new lesson and add it to the database
        new_lesson = Lesson(title=title, content=content)
        db.session.add(new_lesson)
        db.session.commit()

        return jsonify({'message': 'Lesson created successfully!'}), 201

    # Retrieve all lessons
    lessons = Lesson.query.all()
    return jsonify([{'id': lesson.id, 'title': lesson.title} for lesson in lessons]), 200

@app.route('/lessons/<int:lesson_id>', methods=['GET'])
@login_required
def get_lesson(lesson_id):
    """Endpoint to retrieve a specific lesson by ID."""
    lesson = Lesson.query.get_or_404(lesson_id)
    return jsonify({'id': lesson.id, 'title': lesson.title, 'content': lesson.content}), 200

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
