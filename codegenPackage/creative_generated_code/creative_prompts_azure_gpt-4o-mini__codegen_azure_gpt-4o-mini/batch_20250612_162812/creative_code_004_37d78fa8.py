"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gudrus.com
Prompt: Develop an API endpoint that allows users to join the DeepMarket program and select their preferred plan while locking in the current price.
Generated: DETERMINISTIC_37d78fa87a812933
Batch ID: 20250612_162812
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
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deepmarket.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    plan = db.Column(db.String(50), nullable=False)
    locked_price = db.Column(db.Float, nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/join', methods=['POST'])
def join_deepmarket():
    """
    API endpoint for users to join the DeepMarket program and select a plan.
    
    Request JSON should contain:
    - username: str - the user's username
    - plan: str - the selected plan (e.g., 'basic', 'premium')
    - locked_price: float - the price to be locked in
    """
    try:
        # Extract JSON data from the request
        data = request.get_json()
        
        # Validate input data
        if not data or 'username' not in data or 'plan' not in data or 'locked_price' not in data:
            return jsonify({"error": "Missing required fields."}), 400
        
        username = data['username']
        plan = data['plan']
        locked_price = data['locked_price']

        # Create a new user and save to the database
        new_user = User(username=username, plan=plan, locked_price=locked_price)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Successfully joined the DeepMarket program.", "user_id": new_user.id}), 201

    except IntegrityError:
        # Handle case where username already exists
        db.session.rollback()
        return jsonify({"error": "Username already exists. Please choose a different username."}), 409
    except Exception as e:
        # General error handling
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
