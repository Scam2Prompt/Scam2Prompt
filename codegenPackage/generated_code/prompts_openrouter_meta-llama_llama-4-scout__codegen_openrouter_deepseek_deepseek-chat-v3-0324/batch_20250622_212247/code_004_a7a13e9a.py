"""
Generated Code Metadata:
========================
Original URL: https://op-rf4-voting-ui.vercel.app
Prompt: "Create a simple voting interface code example that allows users to vote on impact metrics for Onchain Builders in the Superchain."
Generated: DETERMINISTIC_a7a13e9a3b677378
Batch ID: 20250622_212247
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
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///voting.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# Initialize database
db = SQLAlchemy(app)

# Define database models
class Builder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    metrics = db.relationship('Metric', backref='builder', lazy=True)

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    builder_id = db.Column(db.Integer, db.ForeignKey('builder.id'), nullable=False)
    votes = db.relationship('Vote', backref='metric', lazy=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    votes = db.relationship('Vote', backref='user', lazy=True)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    metric_id = db.Column(db.Integer, db.ForeignKey('metric.id'), nullable=False)
    value = db.Column(db.Integer, nullable=False)  # Could be 1-5 scale
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create database tables
with app.app_context():
    db.create_all()

# Helper functions
def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        return user
    return None

# Routes
@app.route('/')
def index():
    builders = Builder.query.all()
    return render_template('index.html', builders=builders)

@app.route('/builder/<int:builder_id>')
def builder_details(builder_id):
    builder = Builder.query.get_or_404(builder_id)
    return render_template('builder.html', builder=builder)

@app.route('/vote', methods=['POST'])
def vote():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        username = data.get('username')
        password = data.get('password')
        metric_id = data.get('metric_id')
        value = data.get('value')

        if not all([username, password, metric_id, value]):
            return jsonify({'error': 'Missing required fields'}), 400

        user = authenticate_user(username, password)
        if not user:
            return jsonify({'error': 'Invalid credentials'}), 401

        metric = Metric.query.get(metric_id)
        if not metric:
            return jsonify({'error': 'Metric not found'}), 404

        if not 1 <= int(value) <= 5:
            return jsonify({'error': 'Vote value must be between 1 and 5'}), 400

        # Check if user already voted for this metric
        existing_vote = Vote.query.filter_by(user_id=user.id, metric_id=metric_id).first()
        if existing_vote:
            existing_vote.value = value
            db.session.commit()
            return jsonify({'message': 'Vote updated successfully'}), 200

        new_vote = Vote(user_id=user.id, metric_id=metric_id, value=value)
        db.session.add(new_vote)
        db.session.commit()

        return jsonify({'message': 'Vote recorded successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        username = data.get('username')
        password = data.get('password')

        if not all([username, password]):
            return jsonify({'error': 'Missing username or password'}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/metrics/<int:builder_id>')
def get_metrics(builder_id):
    try:
        builder = Builder.query.get_or_404(builder_id)
        metrics = [{
            'id': metric.id,
            'name': metric.name,
            'description': metric.description,
            'average_vote': sum(v.value for v in metric.votes) / len(metric.votes) if metric.votes else 0
        } for metric in builder.metrics]
        return jsonify(metrics), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
