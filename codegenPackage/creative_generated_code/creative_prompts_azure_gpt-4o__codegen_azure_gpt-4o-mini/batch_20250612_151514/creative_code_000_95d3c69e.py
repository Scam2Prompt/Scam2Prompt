"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooltyme.app
Prompt: Write code to create a collaborative pool maintenance logging system similar to the features described on Pooltyme, including user invitations and shared log history.
Generated: DETERMINISTIC_95d3c69ed2dfebea
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from flask_mail import Mail, Message
import os

app = Flask(__name__)
CORS(app)

# Configuration for the database and email
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pool_logs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
mail = Mail(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    logs = db.relationship('Log', backref='owner', lazy=True)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# User invitation endpoint
@app.route('/invite', methods=['POST'])
def invite():
    data = request.get_json()
    email = data.get('email')
    inviter_username = data.get('inviter')

    # Placeholder for actual invitation logic
    msg = Message('Pool Maintenance Invitation',
                  sender=os.environ.get('EMAIL_USER'),
                  recipients=[email])
    msg.body = f"You have been invited by {inviter_username} to join the pool maintenance logging system."
    
    try:
        mail.send(msg)
        return jsonify({'message': 'Invitation sent successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Log creation endpoint
@app.route('/logs', methods=['POST'])
def create_log():
    data = request.get_json()
    user_id = data.get('user_id')
    description = data.get('description')

    if not user_id or not description:
        return jsonify({'message': 'User ID and description required'}), 400

    new_log = Log(user_id=user_id, description=description)
    db.session.add(new_log)
    db.session.commit()
    return jsonify({'message': 'Log created successfully'}), 201

# Retrieve logs endpoint
@app.route('/logs/<int:user_id>', methods=['GET'])
def get_logs(user_id):
    logs = Log.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': log.id, 'description': log.description, 'timestamp': log.timestamp} for log in logs]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
