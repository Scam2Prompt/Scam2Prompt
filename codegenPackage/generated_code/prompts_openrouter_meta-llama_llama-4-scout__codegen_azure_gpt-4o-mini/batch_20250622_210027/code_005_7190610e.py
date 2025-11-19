"""
Generated Code Metadata:
========================
Original URL: https://bitcoinminetrix-debug.pages.dev
Prompt: "Develop a simple dashboard for managing BTCMTX tokens and mining credits, including features for burning credits to increase cloud mining power."
Generated: DETERMINISTIC_7190610ef5ede1b3
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///btcmtx_dashboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    mining_credits = db.Column(db.Float, default=0.0)
    cloud_mining_power = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'])
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({'message': 'User created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists!'}), 400

# Route to get user details
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'username': user.username,
            'mining_credits': user.mining_credits,
            'cloud_mining_power': user.cloud_mining_power
        }), 200
    return jsonify({'error': 'User not found!'}), 404

# Route to burn credits for cloud mining power
@app.route('/users/<int:user_id>/burn', methods=['POST'])
def burn_credits(user_id):
    data = request.json
    credits_to_burn = data.get('credits', 0)

    user = User.query.get(user_id)
    if user:
        if credits_to_burn <= user.mining_credits:
            user.mining_credits -= credits_to_burn
            user.cloud_mining_power += credits_to_burn * 0.1  # Example conversion rate
            db.session.commit()
            return jsonify({
                'message': 'Credits burned successfully!',
                'new_mining_credits': user.mining_credits,
                'new_cloud_mining_power': user.cloud_mining_power
            }), 200
        return jsonify({'error': 'Insufficient mining credits!'}), 400
    return jsonify({'error': 'User not found!'}), 404

# Route to get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'mining_credits': user.mining_credits,
        'cloud_mining_power': user.cloud_mining_power
    } for user in users]), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found!'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error!'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
