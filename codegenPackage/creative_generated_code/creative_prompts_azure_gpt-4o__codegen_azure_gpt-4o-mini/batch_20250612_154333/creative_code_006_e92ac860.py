"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fansliebe.com
Prompt: Create a backend system for managing curated content creators with subscription options and direct messaging capabilities, inspired by Fansliebe's featured creators section.
Generated: DETERMINISTIC_e92ac86027137d42
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

# Initialize Flask app, database, migration, password hashing, and JWT manager
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///creators.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a secure key

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Models

class Creator(db.Model):
    """Model representing a content creator."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    content = db.relationship('Content', backref='creator', lazy=True)

class Content(db.Model):
    """Model representing curated content from a creator."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('creator.id'), nullable=False)

class Message(db.Model):
    """Model representing direct messages between users."""
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('creator.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('creator.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Routes

@app.route('/register', methods=['POST'])
def register():
    """Register a new content creator."""
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    
    new_creator = Creator(username=data['username'], email=data['email'], password_hash=hashed_password)
    
    try:
        db.session.add(new_creator)
        db.session.commit()
        return jsonify(message="Creator registered successfully."), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify(message="Username or email already exists."), 400

@app.route('/login', methods=['POST'])
def login():
    """Login for content creators and return JWT token."""
    data = request.get_json()
    creator = Creator.query.filter_by(email=data['email']).first()
    
    if creator and bcrypt.check_password_hash(creator.password_hash, data['password']):
        access_token = create_access_token(identity=creator.id)
        return jsonify(access_token=access_token), 200
    return jsonify(message="Invalid credentials."), 401

@app.route('/content', methods=['POST'])
@jwt_required()
def add_content():
    """Add new content for a creator."""
    current_creator_id = get_jwt_identity()
    data = request.get_json()
    
    new_content = Content(title=data['title'], body=data['body'], creator_id=current_creator_id)
    db.session.add(new_content)
    db.session.commit()
    
    return jsonify(message="Content added successfully."), 201

@app.route('/messages', methods=['POST'])
@jwt_required()
def send_message():
    """Send a direct message from one creator to another."""
    current_creator_id = get_jwt_identity()
    data = request.get_json()
    
    new_message = Message(sender_id=current_creator_id, recipient_id=data['recipient_id'], content=data['content'])
    db.session.add(new_message)
    db.session.commit()
    
    return jsonify(message="Message sent successfully."), 201

@app.route('/messages/<int:recipient_id>', methods=['GET'])
@jwt_required()
def get_messages(recipient_id):
    """Get messages sent to a specific creator."""
    current_creator_id = get_jwt_identity()
    messages = Message.query.filter_by(recipient_id=recipient_id).all()
    
    return jsonify(messages=[{'id': msg.id, 'content': msg.content} for msg in messages]), 200

# Error Handling

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify(message="Resource not found."), 404

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all other exceptions."""
    return jsonify(message="An error occurred."), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the Flask application
```
