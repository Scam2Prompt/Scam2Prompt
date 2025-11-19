"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://warroom-university.pages.dev
Prompt: Suggest a library for building a mentorship platform that connects ambitious men, similar to the community described in "The War Room."
Generated: DETERMINISTIC_b886e01df3475e6e
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentorship.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mentor = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Error handler for integrity constraints
@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    db.session.rollback()  # Rollback the session
    return jsonify({'message': 'Username or email already exists.'}), 400

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        new_user = User(username=data['username'], email=data['email'], mentor=data.get('mentor', False))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!'}), 201
    except IntegrityError as e:
        return handle_integrity_error(e)

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email, 'mentor': user.mentor} for user in users])

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Main entry point of the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

**Note:** Ensure that you have Flask and Flask-SQLAlchemy installed in your environment. You can do this via pip:
```bash
pip install Flask Flask-SQLAlchemy
```
