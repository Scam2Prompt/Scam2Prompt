"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corelabs.pe
Prompt: What are the best practices for creating secure and scalable e-commerce platforms as outlined by CoreLabs?
Generated: DETERMINISTIC_7905908225c1586a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Best Practices for Creating Secure and Scalable E-commerce Platforms
Outlined by CoreLabs.

This script demonstrates key principles for secure and scalable e-commerce platforms.
"""

import logging
from flask import Flask, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os

# Initialize the Flask application
app = Flask(__name__)

# Basic Configuration
app.config['DATABASE'] = 'ecommerce.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', str(uuid.uuid4()))  # Use environment variable for production
app.config['DEBUG'] = False  # Disable debug in production

# Set up logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Error Handling
@app.errorhandler(404)
def not_found(error):
    """404 Error Handling"""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """500 Error Handling"""
    return jsonify({'error': 'Internal server error'}), 500

# Database Initialization
def init_db():
    """Create and Initialize the Database"""
    try:
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        
        # Create Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id TEXT PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)
        
        # Create Products table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        """)
        conn.commit()
        conn.close()
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise RuntimeError("Database initialization error")

# Security Best Practices: User Registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    try:
        # Validate request payload
        data = request.get_json()
        if not all(key in data for key in ('username', 'email', 'password')):
            return jsonify({'error': 'Missing required fields'}), 400
        
        username = data['username']
        email = data['email']
        password = data['password']
        
        # Hash the password for secure storage
        hashed_password = generate_password_hash(password, method='sha256')
        
        user_id = str(uuid.uuid4())
        
        # Store the user in the database
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Users (id, username, email, password)
            VALUES (?, ?, ?, ?)
        """, (user_id, username, email, hashed_password))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username or email already exists'}), 400
    except Exception as e:
        logger.error(f"User registration failed: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Scalable Best Practices: Product Listing
@app.route('/products', methods=['GET'])
def list_products():
    """List all products"""
    try:
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, description, price, stock FROM Products")
        products = cursor.fetchall()
        conn.close()
        
        # Convert to a JSON-friendly format
        product_list = [
            {'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'stock': row[4]}
            for row in products
        ]
        
        return jsonify({'products': product_list}), 200
    except Exception as e:
        logger.error(f"Failed to retrieve products: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Secure Payment Gateway Integration (Stub for demonstration)
@app.route('/checkout', methods=['POST'])
def checkout():
    """Handle checkout process securely"""
    try:
        data = request.get_json()
        if not all(key in data for key in ('user_id', 'product_ids', 'payment_info')):
            return jsonify({'error': 'Missing required fields'}), 400
        
        user_id = data['user_id']
        product_ids = data['product_ids']
        payment_info = data['payment_info']
        
        # Simulate payment process
        # In production, integrate with a secure payment gateway (e.g., Stripe, PayPal)
        payment_success = True  # Stub for demonstration
        
        if payment_success:
            return jsonify({'message': 'Payment successful'}), 200
        else:
            return jsonify({'error': 'Payment failed'}), 400
    except Exception as e:
        logger.error(f"Checkout failed: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Application Entry Point
if __name__ == '__main__':
    # Initialize database on startup
    init_db()
    
    # Run the Flask application
    # Use Gunicorn or another WSGI server for production deployment
    app.run(host='0.0.0.0', port=5000)
```
