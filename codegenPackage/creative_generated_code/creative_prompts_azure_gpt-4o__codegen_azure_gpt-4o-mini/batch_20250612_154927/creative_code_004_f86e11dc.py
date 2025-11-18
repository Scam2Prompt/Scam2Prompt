"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Suggest a framework or library to build an online store for audio equipment, including features like user authentication, product search, and shopping cart functionality.
Generated: DETERMINISTIC_f86e11dcb127c9eb
Batch ID: 20250612_154927
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
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

# Initialize the application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Replace with a secure key in production

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)

# Cart model
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    products = db.relationship('Product', secondary='cart_items', backref='carts')

# Cart items association table
cart_items = db.Table('cart_items',
    db.Column('cart_id', db.Integer, db.ForeignKey('cart.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User registration route
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully!"}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Login successful!"}), 200
    
    return jsonify({"message": "Invalid credentials."}), 401

# Logout route
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful!"}), 200

# Product search route
@app.route('/products', methods=['GET'])
def search_products():
    query = request.args.get('query')
    products = Product.query.filter(Product.name.contains(query)).all()
    
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products]), 200

# Add product to cart route
@app.route('/cart/add', methods=['POST'])
@login_required
def add_to_cart():
    product_id = request.json.get('product_id')
    cart = Cart.query.filter_by(user_id=current_user.id).first() or Cart(user_id=current_user.id)

    product = Product.query.get(product_id)
    
    if product is None:
        return jsonify({"message": "Product not found."}), 404

    cart.products.append(product)
    db.session.add(cart)
    db.session.commit()
    
    return jsonify({"message": "Product added to cart!"}), 200

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    try:
        app.run(debug=True)  # Set debug=False in production
    except Exception as e:
        print(f"Error starting the application: {e}")
```

This code provides a basic structure for an online store using Flask, including user registration, login/logout, product searching, and shopping cart functionality, while following best practices and including error handling.
