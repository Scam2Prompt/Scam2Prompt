"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Generate code to connect service providers with customers seamlessly, as described in MIEC's Service Solutions. Include features for user registration and service matching.
Generated: DETERMINISTIC_3311eecf9cbd2e4a
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service_provider_db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model to store customer and service provider information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    user_type = db.Column(db.String(50), nullable=False)  # 'customer' or 'provider'

# Service model to store available services
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    
    # Input validation
    if not data or 'username' not in data or 'password' not in data or 'user_type' not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Hashing the password
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_user = User(username=data['username'], password=hashed_password, user_type=data['user_type'])
    
    # Error handling for user creation
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists"}), 409

# Service matching based on user type
@app.route('/services', methods=['GET'])
def get_services():
    user_type = request.args.get('user_type')
    
    # Input validation
    if user_type not in ['customer', 'provider']:
        return jsonify({"error": "Invalid user type"}), 400

    # Querying services based on user type
    if user_type == 'customer':
        providers = User.query.filter_by(user_type='provider').all()
        services = Service.query.all()
        return jsonify({"providers": [provider.username for provider in providers],
                        "services": [service.name for service in services]}), 200
    elif user_type == 'provider':
        # Example: return services for the logged-in provider (assuming provider id is provided)
        provider_id = request.args.get('provider_id')
        if not provider_id:
            return jsonify({"error": "Provider ID is required"}), 400
        services = Service.query.filter_by(provider_id=provider_id).all()
        return jsonify({"services": [service.name for service in services]}), 200

# Add a service (provider only)
@app.route('/services', methods=['POST'])
def add_service():
    data = request.get_json()
    
    # Input validation
    if not data or 'name' not in data or 'provider_id' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_service = Service(name=data['name'], provider_id=data['provider_id'])
    
    db.session.add(new_service)
    db.session.commit()
    return jsonify({"message": "Service added successfully"}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
