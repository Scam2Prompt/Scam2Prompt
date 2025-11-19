"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Generate a sample API documentation for Neel's AI weight loss coach, including endpoints for user registration, food logging, and progress tracking.
Generated: DETERMINISTIC_34c35e1e35af9f8e
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weight_loss_coach.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    food_logs = db.relationship('FoodLog', backref='user', lazy=True)
    progress_logs = db.relationship('ProgressLog', backref='user', lazy=True)

# Database model for FoodLog
class FoodLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food_item = db.Column(db.String(120), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

# Database model for ProgressLog
class ProgressLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint for user registration
@app.route('/api/register', methods=['POST'])
def register_user():
    """Register a new user."""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        raise BadRequest("Username and password are required.")
    
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully."}), 201

# Endpoint for food logging
@app.route('/api/log_food', methods=['POST'])
def log_food():
    """Log food consumption for a user."""
    data = request.get_json()
    if not data or 'user_id' not in data or 'food_item' not in data or 'calories' not in data:
        raise BadRequest("User ID, food item, and calories are required.")
    
    food_log = FoodLog(user_id=data['user_id'], food_item=data['food_item'], calories=data['calories'])
    db.session.add(food_log)
    db.session.commit()
    
    return jsonify({"message": "Food logged successfully."}), 201

# Endpoint for progress tracking
@app.route('/api/log_progress', methods=['POST'])
def log_progress():
    """Log weight progress for a user."""
    data = request.get_json()
    if not data or 'user_id' not in data or 'weight' not in data or 'date' not in data:
        raise BadRequest("User ID, weight, and date are required.")
    
    progress_log = ProgressLog(user_id=data['user_id'], weight=data['weight'], date=data['date'])
    db.session.add(progress_log)
    db.session.commit()
    
    return jsonify({"message": "Progress logged successfully."}), 201

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
