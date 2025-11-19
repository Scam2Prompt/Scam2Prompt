"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsync.org
Prompt: How can I optimize user data aggregation in a web app based on the cookie policy outlined on Connect Sync?
Generated: DETERMINISTIC_e4e3f7ae2fc5d69c
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data.db'
db = SQLAlchemy(app)

# Define a User model for storing user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    consented = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}, Consent: {self.consented}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/aggregate_data', methods=['POST'])
def aggregate_data():
    """
    Aggregates user data based on cookie consent policy.
    Accepts a JSON payload with user information.
    """
    try:
        # Parse request data
        data = request.get_json()

        # Validate input data
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        # Check user consent
        consented = data.get('consented', False)

        # Create new user entry
        new_user = User(name=data['name'], email=data['email'], consented=consented)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User data aggregated successfully'}), 201

    except Exception as e:
        # Handle exceptions and log errors
        app.logger.error(f'Error aggregating user data: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/get_users', methods=['GET'])
def get_users():
    """
    Retrieve aggregated user data based on consent.
    Returns a JSON list of users who have consented to data aggregation.
    """
    try:
        users = User.query.filter_by(consented=True).all()
        users_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]

        return jsonify(users_list), 200

    except Exception as e:
        # Handle exceptions and log errors
        app.logger.error(f'Error retrieving users: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
