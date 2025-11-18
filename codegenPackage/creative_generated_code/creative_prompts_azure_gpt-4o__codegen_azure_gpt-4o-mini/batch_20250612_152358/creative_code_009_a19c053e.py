"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poppredict.vercel.app
Prompt: Create a REST API endpoint for submitting and retrieving user predictions on pop culture events, including authentication and validation.
Generated: DETERMINISTIC_a19c053e7f185704
Batch ID: 20250612_152358
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
from flask import abort
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from marshmallow import Schema, fields, validate, ValidationError
from werkzeug.exceptions import HTTPException

# Initialize Flask application, database, bcrypt and JWT
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Database model for Prediction
class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event = db.Column(db.String(255), nullable=False)
    prediction = db.Column(db.String(255), nullable=False)

# Prediction schema for validation
class PredictionSchema(Schema):
    event = fields.Str(required=True, validate=validate.Length(min=1))
    prediction = fields.Str(required=True, validate=validate.Length(min=1))

prediction_schema = PredictionSchema()

# Error handling for validation
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check for existing user
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    # Hash password and create new user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg": "User created successfully"}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    
    # Validate user credentials
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

# Endpoint to submit predictions
@app.route('/predictions', methods=['POST'])
@jwt_required()
def submit_prediction():
    current_user_id = get_jwt_identity()
    data = request.json

    # Validate incoming prediction data
    try:
        prediction_data = prediction_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_prediction = Prediction(user_id=current_user_id, **prediction_data)
    db.session.add(new_prediction)
    db.session.commit()

    return jsonify({"msg": "Prediction submitted successfully"}), 201

# Endpoint to retrieve predictions for the current user
@app.route('/predictions', methods=['GET'])
@jwt_required()
def get_predictions():
    current_user_id = get_jwt_identity()
    predictions = Prediction.query.filter_by(user_id=current_user_id).all()
    result = [{"event": pred.event, "prediction": pred.prediction} for pred in predictions]
    
    return jsonify(result), 200

# Error handling for general HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({"msg": str(e.description)}), e.code

# Create the database and tables if they don't exist
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
