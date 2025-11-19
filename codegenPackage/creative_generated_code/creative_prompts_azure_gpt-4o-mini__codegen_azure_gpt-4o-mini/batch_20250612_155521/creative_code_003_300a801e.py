"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vestings-scapesmania.pages.dev
Prompt: Provide an example of how to create a referral program API for a gaming platform inspired by ScapesMania's business model.
Generated: DETERMINISTIC_300a801e63a2286e
Batch ID: 20250612_155521
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model to represent users in the referral program
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    referral_code = db.Column(db.String(10), unique=True, nullable=False)
    referred_by = db.Column(db.String(10), db.ForeignKey('user.referral_code'), nullable=True)

    def __repr__(self):
        return f"<User {self.username}, Referral Code: {self.referral_code}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new user with a referral code
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    referral_code = data.get('referral_code')

    # Basic input validation
    if not username or not referral_code:
        return jsonify({'error': 'Username and referral code are required'}), 400
    
    new_user = User(username=username, referral_code=referral_code)

    # Check for referral
    if referral_code and referral_code != new_user.referral_code:
        referrer = User.query.filter_by(referral_code=referral_code).first()
        if referrer:
            new_user.referred_by = referrer.referral_code

    # Add user to the database
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully', 'referral_code': new_user.referral_code}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username or referral code already exists'}), 400

# Endpoint to retrieve user information
@app.route('/user/<string:referral_code>', methods=['GET'])
def get_user(referral_code):
    user = User.query.filter_by(referral_code=referral_code).first()

    if user:
        return jsonify({
            'username': user.username,
            'referral_code': user.referral_code,
            'referred_by': user.referred_by
        }), 200
    else:
        return jsonify({'error': 'User not found'}), 404

# Start the application
if __name__ == '__main__':
    app.run(debug=True)
```
