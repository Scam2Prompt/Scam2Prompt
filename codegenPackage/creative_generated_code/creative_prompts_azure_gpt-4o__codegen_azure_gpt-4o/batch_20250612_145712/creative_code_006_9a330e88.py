"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Develop a web application feature to allow registered users to contribute genealogical data, similar to the user registration system on the Meyer/Seim family site.
Generated: DETERMINISTIC_9a330e8818c401dc
Batch ID: 20250612_145712
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
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from datetime import datetime
from functools import wraps

# Initialize Flask app and configure
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///genealogy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class GenealogicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    full_name = db.Column(db.String(150), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    death_date = db.Column(db.Date, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Decorator to check authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated_function

# User registration route
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not username or not email or not password:
            return jsonify({'error': 'All fields are required'}), 400

        # Check if user already exists
        if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
            return jsonify({'error': 'User already exists'}), 409

        # Hash password and create user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

# User login route
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({'error': 'All fields are required'}), 400

        # Find user by email
        user = User.query.filter_by(email=email).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid credentials'}), 401

        # Save user ID in session
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful'}), 200
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

# User logout route
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

# Add genealogical record route
@app.route('/genealogical-records', methods=['POST'])
@login_required
def add_genealogical_record():
    try:
        data = request.get_json()
        full_name = data.get('full_name')
        birth_date = data.get('birth_date')
        death_date = data.get('death_date')
        notes = data.get('notes')

        # Validate input
        if not full_name:
            return jsonify({'error': 'Full name is required'}), 400

        # Parse dates
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date() if birth_date else None
        death_date = datetime.strptime(death_date, '%Y-%m-%d').date() if death_date else None

        # Create new genealogical record
        new_record = GenealogicalRecord(
            user_id=session['user_id'],
            full_name=full_name,
            birth_date=birth_date,
            death_date=death_date,
            notes=notes
        )
        db.session.add(new_record)
        db.session.commit()

        return jsonify({'message': 'Genealogical record added successfully'}), 201
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

# Fetch all genealogical records for authenticated user
@app.route('/genealogical-records', methods=['GET'])
@login_required
def get_genealogical_records():
    try:
        user_id = session['user_id']
        records = GenealogicalRecord.query.filter_by(user_id=user_id).all()
        records_list = [
            {
                'id': record.id,
                'full_name': record.full_name,
                'birth_date': str(record.birth_date) if record.birth_date else None,
                'death_date': str(record.death_date) if record.death_date else None,
                'notes': record.notes,
                'created_at': record.created_at.isoformat()
            }
            for record in records
        ]
        return jsonify(records_list), 200
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

# Initialize database
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
