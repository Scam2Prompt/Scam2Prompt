"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-aphrodao.web.app
Prompt: Generate code for creating a raffle system where users can sign in and verify their entries, inspired by the raffle functionality described on the Atlas3 website.
Generated: DETERMINISTIC_a097c963fadedbb2
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///raffle.db'
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    entries = db.Column(db.Integer, default=0)

    def set_password(self, password):
        """Hash and set the password for the user."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Database model for Raffle Entry
class RaffleEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    entry_number = db.Column(db.String(10), unique=True, nullable=False)

    user = db.relationship('User', backref=db.backref('entries', lazy=True))

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists.'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Log a user in."""
    username = request.json.get('username')
    password = request.json.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password.'}), 401
    
    session['user_id'] = user.id
    return jsonify({'message': 'Logged in successfully!'}), 200

@app.route('/enter_raffle', methods=['POST'])
def enter_raffle():
    """Allow logged-in users to enter the raffle."""
    if 'user_id' not in session:
        return jsonify({'error': 'You must be logged in to enter the raffle.'}), 403

    user = User.query.get(session['user_id'])
    
    # Generate a unique raffle entry number
    entry_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    
    new_entry = RaffleEntry(user_id=user.id, entry_number=entry_number)
    db.session.add(new_entry)
    user.entries += 1
    db.session.commit()
    
    return jsonify({'message': 'Raffle entry successful!', 'entry_number': entry_number}), 201

@app.route('/entries', methods=['GET'])
def get_entries():
    """Get user's raffle entries."""
    if 'user_id' not in session:
        return jsonify({'error': 'You must be logged in to view your entries.'}), 403

    user = User.query.get(session['user_id'])
    entries = [{'entry_number': entry.entry_number} for entry in user.entries]

    return jsonify({'entries': entries}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """Log a user out."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
