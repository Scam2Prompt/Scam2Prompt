"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jups.io
Prompt: Implement a "refer a friend" feature for a crypto casino platform, similar to the affiliate program mentioned on Jups.io.
Generated: DETERMINISTIC_a8ae6bde02c3539d
Batch ID: 20250612_154412
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

# Database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    referral_code = db.Column(db.String(36), unique=True, nullable=False)
    referred_by = db.Column(db.String(36), nullable=True)

    def __init__(self, username, referred_by=None):
        self.username = username
        self.referral_code = str(uuid.uuid4())  # Generate a unique referral code
        self.referred_by = referred_by

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/refer', methods=['POST'])
def refer_user():
    """
    Endpoint to refer a new user to the platform.
    Expects JSON payload with 'username' and optional 'referral_code'.
    """

    data = request.get_json()
    username = data.get('username')
    referral_code = data.get('referral_code')

    # Validate input
    if not username:
        return jsonify({'error': 'Username is required.'}), 400

    # Check if the username is already taken
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists.'}), 400

    # Create a new user
    new_user = User(username=username, referred_by=referral_code)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'User referred successfully.',
            'referral_code': new_user.referral_code
        }), 201
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Referral code is invalid.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500

@app.route('/users', methods=['GET'])
def list_users():
    """
    Endpoint to list all users in the platform.
    """

    try:
        users = User.query.all()
        return jsonify([{
            'username': user.username,
            'referral_code': user.referral_code,
            'referred_by': user.referred_by
        } for user in users]), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
