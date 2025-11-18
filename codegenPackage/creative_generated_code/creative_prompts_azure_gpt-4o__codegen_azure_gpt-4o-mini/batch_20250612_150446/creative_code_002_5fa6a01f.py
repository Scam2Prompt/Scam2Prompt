"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lambo.beta.coinlist.yachts
Prompt: Generate a Python script to manage token services using an admin interface with Google Workspace sign-in, inspired by the CoinList "Lambo Beta Admin" platform.
Generated: DETERMINISTIC_5fa6a01f6459f3a3
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from google.oauth2 import id_token
from google.auth.transport import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    """User model for storing user information."""
    id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"


@login_manager.user_loader
def load_user(user_id):
    """Load a user from the database by ID."""
    return User.query.get(user_id)


@app.route('/login', methods=['POST'])
def login():
    """Handle Google sign-in and log the user into the application."""
    token = request.json.get('token')
    
    try:
        # Verify the token with Google
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), os.getenv("GOOGLE_CLIENT_ID"))
        email = idinfo['email']
        
        # Check if the user already exists, otherwise create a new user
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(id=idinfo['sub'], email=email)
            db.session.add(user)
            db.session.commit()
        
        # Log the user in
        login_user(user)
        return jsonify({"message": "Login successful", "email": email}), 200

    except ValueError as e:
        return jsonify({"error": "Invalid token"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/logout')
@login_required
def logout():
    """Log the user out of the application."""
    logout_user()
    return jsonify({"message": "Logout successful"}), 200


@app.route('/dashboard')
@login_required
def dashboard():
    """Render the admin dashboard."""
    return render_template('dashboard.html', user=current_user)


@app.route('/api/tokens', methods=['GET', 'POST'])
@login_required
def manage_tokens():
    """Manage token services (list/create)."""
    if request.method == 'POST':
        token_data = request.json
        # Here we would add logic to create a token
        # This is a placeholder for token creation
        return jsonify({"message": "Token created", "data": token_data}), 201
    else:
        # Placeholder for fetching tokens
        # Ideally, fetch from a database or another service
        return jsonify({"tokens": []}), 200


if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()

    # Run the Flask app
    app.run(debug=True)
```

**.env file should include:**
```
SECRET_KEY=your_secret_key
DATABASE_URI=sqlite:///tokens.db
GOOGLE_CLIENT_ID=your_google_client_id
```
