"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jups.io
Prompt: How can I implement a referral system for a crypto casino website, inspired by the promotions mentioned on Jups.io?
Generated: DETERMINISTIC_2377f6c3e70868bf
Batch ID: 20250612_163924
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
from sqlalchemy.exc import IntegrityError
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casino.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(80), nullable=False, unique=True)
    referral_code = db.Column(db.String(10), unique=True)
    referred_by = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Function to generate a unique referral code
def generate_referral_code():
    return str(uuid.uuid4())[:10]

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Accepts JSON with 'username' and optional 'referral_code'.
    """
    data = request.json
    username = data.get('username')
    referral_code = data.get('referral_code')

    if not username:
        return jsonify({'error': 'Username is required.'}), 400

    # Generate a unique referral code for the new user
    new_referral_code = generate_referral_code()

    # Handle referral
    referred_by = None
    if referral_code:
        referrer = User.query.filter_by(referral_code=referral_code).first()
        if referrer:
            referred_by = referrer.id

    new_user = User(username=username, referral_code=new_referral_code, referred_by=referred_by)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.', 'referral_code': new_referral_code}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists.'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/referral/<referral_code>', methods=['GET'])
def get_referral_info(referral_code):
    """
    Endpoint to get information about a referral code.
    Returns the user associated with the referral code.
    """
    user = User.query.filter_by(referral_code=referral_code).first()
    if user:
        return jsonify({'username': user.username, 'referred_by': user.referred_by}), 200
    else:
        return jsonify({'error': 'Referral code not found.'}), 404

if __name__ == '__main__':
    app.run(debug=False)
```

### Notes:
- This code defines a simple referral system for a crypto casino website.
- It uses Flask for the web framework and SQLAlchemy for ORM with a SQLite database.
- Proper error handling is implemented for various scenarios, including unique username conflicts.
- The code is organized and follows best practices for readability and maintainability.
