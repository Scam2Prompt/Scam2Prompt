"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Create an API endpoint specification for a microloan service that includes user authentication and loan application submission, similar to the services offered by SGFC Finance.
Generated: DETERMINISTIC_c171f854581c34ff
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microloan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key in production

# Initialize database and JWT manager
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    term = db.Column(db.Integer, nullable=False)  # Term in months
    status = db.Column(db.String(50), default="Pending")  # Status: Pending, Approved, Rejected

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'Username already exists'}), 400

        # Hash password and save the user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        # Find the user by username
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid username or password'}), 401

        # Generate JWT token
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Loan application submission endpoint
@app.route('/apply-loan', methods=['POST'])
@jwt_required()
def apply_loan():
    try:
        data = request.get_json()
        user_id = request.json.get('user_id')
        amount = data['amount']
        term = data['term']

        # Ensure valid data
        if amount <= 0 or term <= 0:
            return jsonify({'message': 'Invalid loan amount or term'}), 400

        # Create a loan application
        loan_application = LoanApplication(user_id=user_id, amount=amount, term=term)
        db.session.add(loan_application)
        db.session.commit()

        return jsonify({'message': 'Loan application submitted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

**Notes for deployment:**
- Replace `your_secret_key` with an actual secret key in production.
- Use a production-grade database instead of SQLite.
- Deploy using a WSGI server like Gunicorn if hosting on a production environment.
