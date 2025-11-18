"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Write Python code to create a subscription-based e-book access system similar to Digielearning, including features for different subscription plans (e.g., Basic, Standard, Premium) and secure user authentication.
Generated: DETERMINISTIC_34ddbc089c80d331
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.exceptions import HTTPException
import os

# Initialize the Flask application
app = Flask(__name__)

# Set secret key for session management and configure the database
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ebooks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and authentication
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for authentication and subscription plans
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    subscription_plan = db.Column(db.String(50), nullable=False)

# Subscription plans
SUBSCRIPTION_PLANS = {
    'Basic': 'Access to basic e-books',
    'Standard': 'Access to standard e-books',
    'Premium': 'Access to all e-books'
}

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify(error=str(e)), e.code

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    subscription_plan = data.get('subscription_plan', 'Basic')

    # Validate subscription plan
    if subscription_plan not in SUBSCRIPTION_PLANS:
        return jsonify({"error": "Invalid subscription plan"}), 400

    # Hash the password and create a new user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password, subscription_plan=subscription_plan)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()

    # Check user existence and password
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Login successful", "subscription_plan": user.subscription_plan}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200

# Route to access e-books based on subscription plan
@app.route('/ebooks', methods=['GET'])
@login_required
def get_ebooks():
    if current_user.subscription_plan == 'Basic':
        return jsonify({"ebooks": ["Basic e-book 1", "Basic e-book 2"]}), 200
    elif current_user.subscription_plan == 'Standard':
        return jsonify({"ebooks": ["Standard e-book 1", "Standard e-book 2", "Basic e-book 1"]}), 200
    elif current_user.subscription_plan == 'Premium':
        return jsonify({"ebooks": ["Premium e-book 1", "Premium e-book 2", "Standard e-book 1", "Basic e-book 1"]}), 200

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```
