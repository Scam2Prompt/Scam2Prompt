"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corelabs.pe
Prompt: Generate code for creating a secure and scalable e-commerce platform, incorporating features highlighted in CoreLabs' advanced web and e-commerce services.
Generated: DETERMINISTIC_b5e8866f100f7073
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration for the application
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///ecommerce.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_secret_key')  # Change this in production

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database models
class User(db.Model):
    """User model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return bcrypt.check_password_hash(self.password_hash, password)

class Product(db.Model):
    """Product model for storing product information."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Routes
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"msg": "Missing email or password"}), 400

    # Check if user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "User already exists"}), 400

    new_user = User(email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Log in a user and return a JWT."""
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad email or password"}), 401

@app.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    """Retrieve all products."""
    products = Product.query.all()
    return jsonify([{'id': product.id, 'name': product.name, 'price': product.price} for product in products]), 200

@app.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    """Create a new product."""
    data = request.get_json()
    if not data or not data.get('name') or not data.get('price'):
        return jsonify({"msg": "Missing product name or price"}), 400

    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"msg": "Product created successfully"}), 201

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"msg": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"msg": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set to False in production
```

### Notes:
- Make sure to set up environment variables `DATABASE_URL` and `JWT_SECRET_KEY` for production use.
- For a production-ready environment, consider using a more robust database (like PostgreSQL) and enable HTTPS with a proper web server.
- The `debug=True` flag should be set to `False` in production.
