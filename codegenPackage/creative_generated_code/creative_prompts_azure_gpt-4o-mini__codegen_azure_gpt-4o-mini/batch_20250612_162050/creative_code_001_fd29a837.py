"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: How can I use the DBT approach to create a mental health app that helps users manage emotional dysregulation? Include specific features based on the DBT methodology.
Generated: DETERMINISTIC_fd29a837577bb223
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mental_health_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a User model to store user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    emotion_logs = db.relationship('EmotionLog', backref='user', lazy=True)

# Define a model for logging emotional states
class EmotionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    emotion = db.Column(db.String(50), nullable=False)
    intensity = db.Column(db.Integer, nullable=False)  # 1 to 10 scale
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    try:
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to log emotions
@app.route('/log_emotion', methods=['POST'])
def log_emotion():
    data = request.get_json()
    try:
        user = User.query.get(data['user_id'])
        if not user:
            return jsonify({'error': 'User not found.'}), 404
        new_log = EmotionLog(user_id=data['user_id'], emotion=data['emotion'], intensity=data['intensity'])
        db.session.add(new_log)
        db.session.commit()
        return jsonify({'message': 'Emotion logged successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to retrieve emotion logs for a user
@app.route('/emotion_logs/<int:user_id>', methods=['GET'])
def get_emotion_logs(user_id):
    try:
        logs = EmotionLog.query.filter_by(user_id=user_id).all()
        return jsonify([{'emotion': log.emotion, 'intensity': log.intensity, 'timestamp': log.timestamp} for log in logs]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Error handling for general HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({'error': e.description}), e.code

# Error handling for unhandled exceptions
@app.errorhandler(Exception)
def handle_unhandled_exception(e):
    return jsonify({'error': 'An unexpected error occurred.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
