"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Generate code for a secure user authentication system for a TMS (Transportation Management System) similar to MultiTMS.
Generated: DETERMINISTIC_74fd70a3be733f4b
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change to your database URI
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password using bcrypt and store it."""
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username and password."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists.'}), 400

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and start a session."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful.'}), 200
    return jsonify({'error': 'Invalid username or password.'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Log out a user by clearing the session."""
    session.pop('user_id', None)
    return jsonify({'message': 'You have been logged out.'}), 200

@app.route('/user', methods=['GET'])
def get_user():
    """Get the current authenticated user's information."""
    user_id = session.get('user_id')
    if user_id is None:
        return jsonify({'error': 'Unauthorized access.'}), 401

    user = User.query.get(user_id)
    return jsonify({'username': user.username}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

### Important Notes:
- Replace `'your_secret_key'` with a secure random key in production.
- Consider using a more robust database configuration instead of SQLite for production use.
- Use HTTPS in a production environment to ensure secure data transmission.
