"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formulir.site
Prompt: Create a code snippet for a user authentication system with "Log In" and "Sign Up" functionality, inspired by the interface on formulir.site.
Generated: DETERMINISTIC_8bcc663de798a776
Batch ID: 20250612_154927
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a strong secret key
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/signup', methods=['POST'])
def signup():
    """Handle user signup."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check for missing fields
    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    # Hash the password for security
    hashed_password = generate_password_hash(password)

    # Create a new user
    new_user = User(username=username, password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check for missing fields
    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    user = User.query.filter_by(username=username).first()

    # Verify user existence and password
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({"message": "Login successful."}), 200
    else:
        return jsonify({"error": "Invalid username or password."}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Handle user logout."""
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({"message": "Logout successful."}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Requirements
Make sure you have the following libraries installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Cors Werkzeug
``` 

### Note
- Adjust the `SECRET_KEY` to a strong random value for production.
- Make sure to handle and log errors appropriately in a production environment.
