"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cidautos.com
Prompt: Write code to implement a customer login system for accessing personalized vehicle financing options, inspired by the "Acceso Clientes" section on Cid Autos.
Generated: DETERMINISTIC_3102078bf6029031
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'  # Using SQLite for simplicity
db = SQLAlchemy(app)

# Database model for Customer
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password against provided password."""
        return check_password_hash(self.password_hash, password)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new customer."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    if Customer.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists."}), 400

    new_customer = Customer(username=username)
    new_customer.set_password(password)
    db.session.add(new_customer)
    db.session.commit()

    return jsonify({"message": "Registration successful."}), 201

@app.route('/login', methods=['POST'])
def login():
    """Log in an existing customer."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    customer = Customer.query.filter_by(username=username).first()

    if customer is None or not customer.check_password(password):
        return jsonify({"error": "Invalid username or password."}), 401

    session['customer_id'] = customer.id  # Store customer ID in session
    return jsonify({"message": "Login successful."}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current customer."""
    session.pop('customer_id', None)
    return jsonify({"message": "Logout successful."}), 200

@app.route('/financing-options', methods=['GET'])
def financing_options():
    """Get personalized vehicle financing options for the logged-in customer."""
    if 'customer_id' not in session:
        return jsonify({"error": "Unauthorized access."}), 403

    # Placeholder: Replace with actual financing options logic
    options = {
        "options": [
            {"type": "Loan", "rate": "3.5%", "term": "5 years"},
            {"type": "Lease", "rate": "2.5%", "term": "3 years"}
        ]
    }
    return jsonify(options), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
