"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meowworldsnft.pages.dev
Prompt: Illustrate how to implement security best practices for managing Meow World NFTs in a web application.
Generated: DETERMINISTIC_a47c060af59d2686
Batch ID: 20250612_163200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

# Initialize Flask app
app = Flask(__name__)

# Security best practices: Configure environment variables for sensitive data
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///meow_world.db')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Secret key for JWT
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Define a User model (securely store passwords using hashing)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        # Hash the password before storing it
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        # Verify the password hash
        return bcrypt.check_password_hash(self.password_hash, password)

# Define an NFT model
class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route: User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        abort(400, description="Username and password are required.")  # Input validation

    if User.query.filter_by(username=username).first():
        abort(400, description="Username already exists.")

    new_user = User(username=username)
    new_user.set_password(password)  # Securely hash the password
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message="User registered successfully"), 201

# Route: User login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        abort(401, description="Invalid credentials.")  # Avoid revealing too much information

    access_token = create_access_token(identity=user.id)  # Generate JWT token
    return jsonify(access_token=access_token), 200

# Route: List the user's NFTs (Protected)
@app.route('/nfts', methods=['GET'])
@jwt_required()
def list_nfts():
    current_user_id = get_jwt_identity()  # Retrieve the user ID from the JWT
    user_nfts = NFT.query.filter_by(owner_id=current_user_id).all()

    nft_list = [{"id": nft.id, "name": nft.name} for nft in user_nfts]
    return jsonify(nfts=nft_list), 200

# Route: Create a new NFT (Protected)
@app.route('/nfts', methods=['POST'])
@jwt_required()
def create_nft():
    current_user_id = get_jwt_identity()  # Retrieve the user ID from the JWT
    data = request.get_json()
    nft_name = data.get('name')

    if not nft_name:
        abort(400, description="NFT name is required.")  # Input validation

    new_nft = NFT(name=nft_name, owner_id=current_user_id)
    db.session.add(new_nft)
    db.session.commit()

    return jsonify(message="NFT created successfully"), 201

# Route: Transfer an NFT to another user (Protected)
@app.route('/transfer_nft', methods=['POST'])
@jwt_required()
def transfer_nft():
    current_user_id = get_jwt_identity()  # Retrieve the user ID from the JWT
    data = request.get_json()
    nft_id = data.get('nft_id')
    recipient_username = data.get('recipient_username')

    nft = NFT.query.filter_by(id=nft_id, owner_id=current_user_id).first()
    if not nft:
        abort(404, description="NFT not found.")

    recipient = User.query.filter_by(username=recipient_username).first()
    if not recipient:
        abort(404, description="Recipient not found.")

    nft.owner_id = recipient.id
    db.session.commit()

    return jsonify(message="NFT transferred successfully"), 200

# Error Handling: Provide meaningful error messages
@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(404)
def handle_error(error):
    response = jsonify(message=error.description)
    response.status_code = error.code
    return response

# Main entry point
if __name__ == '__main__':
    # Use a proper production server in deployment (e.g., Gunicorn)
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```
