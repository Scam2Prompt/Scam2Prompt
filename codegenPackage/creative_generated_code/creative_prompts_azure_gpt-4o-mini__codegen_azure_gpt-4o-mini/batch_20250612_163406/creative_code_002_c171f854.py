"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Create an API endpoint specification for a microloan service that includes user authentication and loan application submission, similar to the services offered by SGFC Finance.
Generated: DETERMINISTIC_c171f854581c34ff
Batch ID: 20250612_163406
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
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_optional
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microloan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a random secret

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database models
class User(db.Model):
    """Model for User."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class LoanApplication(db.Model):
    """Model for Loan Application."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')

# Schemas for validation
class UserSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3))
    password = fields.String(required=True, validate=validate.Length(min=6))

class LoanApplicationSchema(Schema):
    amount = fields.Float(required=True, validate=validate.Range(min=100, max=10000))

# User Registration Endpoint
@app.route('/register', methods=['POST'])
def register():
    """Registers a new user."""
    data = request.get_json()
    try:
        validated_data = UserSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    if User.query.filter_by(username=validated_data['username']).first():
        return jsonify({"message": "User already exists."}), 400

    hashed_password = bcrypt.generate_password_hash(validated_data['password']).decode('utf-8')
    new_user = User(username=validated_data['username'], password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully."}), 201

# User Login Endpoint
@app.route('/login', methods=['POST'])
def login():
    """Logs in a user and returns a JWT token."""
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    
    if user and bcrypt.check_password_hash(user.password, data.get('password')):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"message": "Invalid credentials."}), 401

# Loan Application Submission Endpoint
@app.route('/loan_application', methods=['POST'])
@jwt_required()
def apply_loan():
    """Submits a loan application."""
    data = request.get_json()
    try:
        validated_data = LoanApplicationSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    current_user_id = get_jwt_identity()
    loan_application = LoanApplication(user_id=current_user_id, amount=validated_data['amount'])
    
    db.session.add(loan_application)
    db.session.commit()
    
    return jsonify({"message": "Loan application submitted successfully.", "application_id": loan_application.id}), 201

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```
