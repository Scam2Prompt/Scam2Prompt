"""
Generated Code Metadata:
========================
Original URL: https://opterisglobal.com
Prompt: Illustrate how to implement a referral program in a web application, inspired by the rewards system mentioned on Opteris Global's website.
Generated: DETERMINISTIC_a0b1689beb3e8f52
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    referral_code = db.Column(db.String(10), unique=True, nullable=False)
    referred_by = db.Column(db.String(10), db.ForeignKey('user.referral_code'), nullable=True)
    rewards = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.email}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a new user with a referral code
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get('email')
    referral_code = data.get('referral_code')

    # Generate a unique referral code
    new_referral_code = generate_referral_code()

    # Create a new user
    new_user = User(email=email, referral_code=new_referral_code, referred_by=referral_code)

    # Handle potential errors during user creation
    try:
        db.session.add(new_user)
        db.session.commit()
        if referral_code:
            # Update the referrer’s rewards
            referrer = User.query.filter_by(referral_code=referral_code).first()
            if referrer:
                referrer.rewards += 10  # Reward for referring a new user
                db.session.commit()
        return jsonify({"message": "User registered successfully", "referral_code": new_referral_code}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email or referral code already exists"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Function to generate a unique referral code
def generate_referral_code(length=10):
    import random
    import string
    characters = string.ascii_letters + string.digits
    while True:
        referral_code = ''.join(random.choices(characters, k=length))
        if not User.query.filter_by(referral_code=referral_code).first():
            return referral_code

# Endpoint to get user rewards
@app.route('/rewards/<string:referral_code>', methods=['GET'])
def get_rewards(referral_code):
    user = User.query.filter_by(referral_code=referral_code).first()
    if user:
        return jsonify({"email": user.email, "rewards": user.rewards}), 200
    return jsonify({"error": "User not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have Flask and SQLAlchemy installed. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

### Running the Application
1. Save the code in a file named `referral_program.py`.
2. Run the application using the command:
   ```bash
   python referral_program.py
   ```
3. Use a tool like Postman or curl to interact with the API endpoints.
