"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Develop a web application for personalized online coaching, integrating features like progress tracking, nutrition guidance, and sport-specific training plans as outlined by Blaise Strong.
Generated: DETERMINISTIC_8493b4acdd08e5ed
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coaching_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    progress = db.relationship('Progress', backref='user', lazy=True)

# Define the Progress model
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Float, nullable=True)
    workout_details = db.Column(db.String(200), nullable=True)

# Define the Nutrition model
class Nutrition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meal_plan = db.Column(db.String(200), nullable=False)

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        raise BadRequest("Username and email are required.")
    
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "username": new_user.username}), 201

# Route to track user progress
@app.route('/users/<int:user_id>/progress', methods=['POST'])
def track_progress(user_id):
    data = request.get_json()
    if not data or 'date' not in data:
        raise BadRequest("Date is required.")
    
    user = User.query.get(user_id)
    if not user:
        raise NotFound("User not found.")
    
    new_progress = Progress(user_id=user_id, date=data['date'], weight=data.get('weight'), workout_details=data.get('workout_details'))
    db.session.add(new_progress)
    db.session.commit()
    return jsonify({"id": new_progress.id, "date": new_progress.date}), 201

# Route to get user progress
@app.route('/users/<int:user_id>/progress', methods=['GET'])
def get_progress(user_id):
    user = User.query.get(user_id)
    if not user:
        raise NotFound("User not found.")
    
    progress_records = Progress.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": p.id, "date": p.date, "weight": p.weight, "workout_details": p.workout_details} for p in progress_records]), 200

# Route to provide nutrition guidance
@app.route('/users/<int:user_id>/nutrition', methods=['POST'])
def add_nutrition(user_id):
    data = request.get_json()
    if not data or 'meal_plan' not in data:
        raise BadRequest("Meal plan is required.")
    
    user = User.query.get(user_id)
    if not user:
        raise NotFound("User not found.")
    
    new_nutrition = Nutrition(user_id=user_id, meal_plan=data['meal_plan'])
    db.session.add(new_nutrition)
    db.session.commit()
    return jsonify({"id": new_nutrition.id, "meal_plan": new_nutrition.meal_plan}), 201

# Error handling for 404
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for 400
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```
