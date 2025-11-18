"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com
Prompt: Develop an API endpoint for user authentication and password resets, as described in Zadepositslot's FAQ section.
Generated: DETERMINISTIC_150df56aadbc6cf8
Batch ID: 20250612_150345
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
from flask_migrate import Migrate
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure key
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Create the database table if it doesn't exist
@app.before_first_request
def create_tables():
    db.create_all()

# Generate a password reset token
def generate_reset_token(user):
    s = Serializer(app.config['SECRET_KEY'], expires_in=3600)  # Token valid for 1 hour
    return s.dumps({'user_id': user.id}).decode('utf-8')

# Verify the password reset token
def verify_reset_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except Exception:  # Catch all exceptions for token verification
        return None
    return User.query.get(data['user_id'])

@app.route('/auth/login', methods=['POST'])
def login():
    """Authenticate a user and return an access token."""
    data = request.get_json()
    
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({'message': 'Invalid request'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if user is None or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid username or password'}), 401
    
    # Generate and return a token (In a real app, use JWT or similar)
    access_token = generate_reset_token(user)
    return jsonify({'token': access_token}), 200

@app.route('/auth/reset_password', methods=['POST'])
def reset_password():
    """Reset a user's password using a token."""
    data = request.get_json()
    
    if not data or not 'token' in data or not 'new_password' in data:
        return jsonify({'message': 'Invalid request'}), 400
    
    user = verify_reset_token(data['token'])
    
    if user is None:
        return jsonify({'message': 'Invalid or expired token'}), 403
    
    user.set_password(data['new_password'])
    db.session.commit()
    
    return jsonify({'message': 'Password has been reset successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
