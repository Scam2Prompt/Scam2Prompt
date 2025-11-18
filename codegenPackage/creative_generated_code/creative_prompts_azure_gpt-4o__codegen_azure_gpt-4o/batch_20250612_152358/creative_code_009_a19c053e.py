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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

# Initialize Flask app
app = Flask(__name__)

# Configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'  # Path to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Replace with a secure key

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Database model for Prediction
class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(255), nullable=False)
    prediction = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Authentication endpoint - Register
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Authentication endpoint - Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
    return jsonify({"access_token": access_token}), 200

# Prediction endpoint - Submit prediction
@app.route('/predictions', methods=['POST'])
@jwt_required()
def submit_prediction():
    user_id = get_jwt_identity()
    data = request.get_json()
    event = data.get('event')
    prediction = data.get('prediction')

    if not event or not prediction:
        return jsonify({"error": "Event and prediction are required"}), 400

    new_prediction = Prediction(event=event, prediction=prediction, user_id=user_id)
    db.session.add(new_prediction)
    db.session.commit()

    return jsonify({"message": "Prediction submitted successfully", "prediction_id": new_prediction.id}), 201

# Prediction endpoint - Retrieve predictions
@app.route('/predictions', methods=['GET'])
@jwt_required()
def get_predictions():
    user_id = get_jwt_identity()
    predictions = Prediction.query.filter_by(user_id=user_id).all()

    predictions_list = [
        {"id": p.id, "event": p.event, "prediction": p.prediction} for p in predictions
    ]

    return jsonify({"predictions": predictions_list}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
