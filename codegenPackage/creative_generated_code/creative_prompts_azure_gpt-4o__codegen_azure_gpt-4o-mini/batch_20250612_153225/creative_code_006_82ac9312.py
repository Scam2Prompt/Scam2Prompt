"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Develop a secure survey system that uses token-gated access and includes a feature to collect feedback from a specific community, inspired by Moonbirds Holder Survey.
Generated: DETERMINISTIC_82ac931293646b23
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)

# Set the database URI and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///survey.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    community = db.Column(db.String(120), nullable=False)

# Schema for User
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Model for SurveyResponse
class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    feedback = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Schema for SurveyResponse
class SurveyResponseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SurveyResponse

# Token required decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
            if current_user is None:
                raise Exception("User not found")
        except Exception as e:
            return jsonify({'message': f'Invalid token! {str(e)}'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    community = request.json.get('community')

    if not username or not password or not community:
        return jsonify({'message': 'Missing fields!'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password, community=community)
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401

# Endpoint for submitting survey response
@app.route('/survey', methods=['POST'])
@token_required
def submit_survey(current_user):
    feedback = request.json.get('feedback')

    if not feedback:
        return jsonify({'message': 'Feedback cannot be empty!'}), 400

    new_response = SurveyResponse(user_id=current_user.id, feedback=feedback)
    db.session.add(new_response)
    db.session.commit()

    return jsonify({'message': 'Survey response submitted successfully!'}), 201

# Endpoint to view feedback from the same community
@app.route('/community_feedback', methods=['GET'])
@token_required
def community_feedback(current_user):
    responses = SurveyResponse.query.join(User).filter(User.community == current_user.community).all()
    response_schema = SurveyResponseSchema(many=True)
    return jsonify(response_schema.dump(responses)), 200

# Error handling for the database
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'message': str(e)}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables if they don't exist
    app.run(debug=False)  # Set to False for production
```

Make sure to set up your environment variables and install the required packages using:
```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow PyJWT
```
