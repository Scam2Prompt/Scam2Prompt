"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ehajj.ph
Prompt: Recommend a library or API to implement secure user authentication for a portal like Hajj Portal Philippines.
Generated: DETERMINISTIC_0b134cb6cb62f625
Batch ID: 20250612_145213
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
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError

# Initialize Flask app, database, bcrypt, and login manager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Replace with your preferred database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if unauthorized

# User model for the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user
    new_user = User(username=username, password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully."}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Username already exists."}), 409
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    
    # Check if user exists and password is correct
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)  # Log in the user
        return jsonify({"message": "Login successful."}), 200
    else:
        return jsonify({"message": "Invalid username or password."}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful."}), 200

# Route for checking user status
@app.route('/status', methods=['GET'])
@login_required
def status():
    return jsonify({"username": current_user.username, "message": "User is logged in."}), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Resource not found."}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message": "An internal error occurred."}), 500

# Main function to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug=False for production
```
