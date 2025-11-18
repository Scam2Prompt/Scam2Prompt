"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: Recommend software solutions to build a social-first networking platform like Sync Connects, focusing on features for member authentication, event management, and community engagement.
Generated: DETERMINISTIC_7134eba88e345304
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize Flask app and extensions
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_network.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not authenticated

# User model for member authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Event model for event management
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False)

# Community Engagement model (e.g., comments, likes)
class Engagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    comment = db.Column(db.Text, nullable=True)

# Load user for login management
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        abort(400, description="Invalid input data")
    
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        abort(400, description="Invalid input data")
    
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    else:
        abort(401, description="Invalid credentials")

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200

# Route to create a new event
@app.route('/event', methods=['POST'])
@login_required
def create_event():
    data = request.get_json()
    if not data or 'title' not in data or 'date' not in data:
        abort(400, description="Invalid input data")
    
    new_event = Event(title=data['title'], description=data.get('description'), date=data['date'])
    db.session.add(new_event)
    db.session.commit()
    
    return jsonify({"message": "Event created successfully"}), 201

# Route to get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{"id": event.id, "title": event.title, "description": event.description, "date": event.date} for event in events])

# Route to engage with an event (comment)
@app.route('/engage', methods=['POST'])
@login_required
def engage():
    data = request.get_json()
    if not data or 'event_id' not in data or 'comment' not in data:
        abort(400, description="Invalid input data")
    
    new_engagement = Engagement(user_id=current_user.id, event_id=data['event_id'], comment=data['comment'])
    db.session.add(new_engagement)
    db.session.commit()
    
    return jsonify({"message": "Engagement added successfully"}), 201

# Error handler for invalid requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": str(error)}), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```
