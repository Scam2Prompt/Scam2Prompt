"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betlahze.vip
Prompt: Create an API endpoint for user registration that includes bonus incentives, reflecting the quick sign-up process mentioned on the BaxBet site.
Generated: DETERMINISTIC_3ce1a59303982e1a
Batch ID: 20250612_155849
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
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    bonus_incentive = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/register', methods=['POST'])
def register_user():
    """API endpoint for user registration."""
    data = request.get_json()

    # Validate incoming data
    if not data or not all(key in data for key in ['username', 'email', 'password']):
        return jsonify({'error': 'Missing required fields'}), 400

    username = data['username']
    email = data['email']
    password = data['password']

    # Check for existing user
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return jsonify({'error': 'Username or email already exists'}), 409

    # Hash the password for security
    hashed_password = generate_password_hash(password, method='sha256')

    # Create a new user instance
    new_user = User(username=username, email=email, password=hashed_password)

    # Assign a bonus incentive for quick sign-up
    new_user.bonus_incentive = 10.0  # Example incentive amount

    try:
        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully', 'bonus': new_user.bonus_incentive}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': 'Registration failed', 'details': str(e)}), 500
    finally:
        db.session.close()  # Ensure the session is closed

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```
