"""
Generated Code Metadata:
========================
Original URL: https://horizonblue.firstlight.am
Prompt: Suggest libraries for building a collaborative platform that allows users to view, comment, and contribute to market intelligence reports.
Generated: DETERMINISTIC_395a965d03889ad7
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for building a collaborative platform
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market_intelligence.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User model for authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Report model for market intelligence reports
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='report', lazy=True)

# Comment model for user comments on reports
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Load user for login management
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Error handling for existing user
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists!'}), 400
    
    # Create new user
    new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    # Error handling for invalid credentials
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    login_user(user)
    return jsonify({'message': 'Logged in successfully!'}), 200

# Route for creating a new report
@app.route('/reports', methods=['POST'])
@login_required
def create_report():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    new_report = Report(title=title, content=content, user_id=current_user.id)
    db.session.add(new_report)
    db.session.commit()
    return jsonify({'message': 'Report created successfully!'}), 201

# Route for commenting on a report
@app.route('/reports/<int:report_id>/comments', methods=['POST'])
@login_required
def comment_on_report(report_id):
    data = request.get_json()
    content = data.get('content')
    
    new_comment = Comment(content=content, report_id=report_id, user_id=current_user.id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({'message': 'Comment added successfully!'}), 201

# Route for viewing reports
@app.route('/reports', methods=['GET'])
def get_reports():
    reports = Report.query.all()
    return jsonify([{'id': report.id, 'title': report.title, 'content': report.content} for report in reports]), 200

# Route for logging out
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully!'}), 200

# Main entry point for the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```
