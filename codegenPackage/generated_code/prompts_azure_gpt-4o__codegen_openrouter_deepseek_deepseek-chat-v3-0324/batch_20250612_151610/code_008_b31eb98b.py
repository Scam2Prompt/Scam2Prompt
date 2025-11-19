"""
Generated Code Metadata:
========================
Original URL: https://connectsonlinedapps.weebly.com
Prompt: Provide an example of customizing a ConnectsOnlineDApps template for a specific use case, such as a voting system.
Generated: DETERMINISTIC_b31eb98bbd6af159
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=False)
    voted_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

# Authentication routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password required'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400

    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password required'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity={'id': user.id, 'username': user.username, 'is_admin': user.is_admin})
    return jsonify({'access_token': access_token}), 200

# Poll routes
@app.route('/polls', methods=['GET'])
@jwt_required()
def get_polls():
    polls = Poll.query.filter_by(is_active=True).all()
    result = []
    for poll in polls:
        options = Option.query.filter_by(poll_id=poll.id).all()
        poll_data = {
            'id': poll.id,
            'title': poll.title,
            'description': poll.description,
            'options': [{'id': opt.id, 'text': opt.text} for opt in options]
        }
        result.append(poll_data)
    return jsonify(result), 200

@app.route('/polls', methods=['POST'])
@jwt_required()
def create_poll():
    current_user = get_jwt_identity()
    if not current_user['is_admin']:
        return jsonify({'message': 'Admin access required'}), 403

    data = request.get_json()
    if not data or 'title' not in data or 'options' not in data:
        return jsonify({'message': 'Title and options are required'}), 400

    poll = Poll(
        title=data['title'],
        description=data.get('description', ''),
        created_by=current_user['id']
    )
    db.session.add(poll)
    db.session.commit()

    for option_text in data['options']:
        option = Option(text=option_text, poll_id=poll.id)
        db.session.add(option)

    db.session.commit()
    return jsonify({'message': 'Poll created successfully', 'poll_id': poll.id}), 201

@app.route('/polls/<int:poll_id>/vote', methods=['POST'])
@jwt_required()
def vote(poll_id):
    current_user = get_jwt_identity()
    data = request.get_json()
    if not data or 'option_id' not in data:
        return jsonify({'message': 'Option ID required'}), 400

    # Check if user already voted in this poll
    existing_vote = Vote.query.join(Option).filter(
        Vote.user_id == current_user['id'],
        Option.poll_id == poll_id
    ).first()
    if existing_vote:
        return jsonify({'message': 'You have already voted in this poll'}), 400

    option = Option.query.filter_by(id=data['option_id'], poll_id=poll_id).first()
    if not option:
        return jsonify({'message': 'Invalid option'}), 404

    vote = Vote(user_id=current_user['id'], option_id=option.id)
    db.session.add(vote)
    db.session.commit()

    return jsonify({'message': 'Vote recorded successfully'}), 201

@app.route('/polls/<int:poll_id>/results', methods=['GET'])
@jwt_required()
def get_results(poll_id):
    poll = Poll.query.get(poll_id)
    if not poll:
        return jsonify({'message': 'Poll not found'}), 404

    options = Option.query.filter_by(poll_id=poll_id).all()
    results = []
    for option in options:
        vote_count = Vote.query.filter_by(option_id=option.id).count()
        results.append({
            'option_id': option.id,
            'text': option.text,
            'votes': vote_count
        })

    return jsonify({
        'poll_id': poll.id,
        'title': poll.title,
        'results': results
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
