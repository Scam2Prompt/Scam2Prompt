"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomdistro.com
Prompt: Generate a code snippet for an e-commerce website that allows users to register and log in, similar to the account management features on PhantomDistro.
Generated: DETERMINISTIC_9f869c738265f2c4
Batch ID: 20250612_155651
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
from flasgger import Swagger

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
swagger = Swagger(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """
    User registration endpoint
    ---
    parameters:
      - name: username
        type: string
        required: true
      - name: password
        type: string
        required: true
    responses:
      201:
        description: User registered successfully
      400:
        description: Bad request or user already exists
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400

    # Create a new user
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    User login endpoint
    ---
    parameters:
      - name: username
        type: string
        required: true
      - name: password
        type: string
        required: true
    responses:
      200:
        description: Login successful
      401:
        description: Invalid credentials
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()

    # Check credentials
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id  # Create session
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """
    User logout endpoint
    ---
    responses:
      200:
        description: Logout successful
    """
    session.pop('user_id', None)  # Remove user from session
    return jsonify({'message': 'Logout successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
