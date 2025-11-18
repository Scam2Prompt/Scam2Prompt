"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-unity-profit.com
Prompt: Create a REST API for a platform like Juros Xyro that allows users to register, input their preferences, and receive matched investment education firms.
Generated: DETERMINISTIC_edc93617bfa4fdac
Batch ID: 20250612_150854
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    preferences = db.Column(db.Text, nullable=True)

# User Schema for validation
class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    preferences = fields.Str(required=False)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Helper function to get matched firms based on preferences
def match_investment_firms(preferences):
    # Simulate matching logic (returning dummy data for this example)
    return [{"firm_name": "InvestSmart", "score": 95}, {"firm_name": "WealthBuilders", "score": 90}]

# Register User Endpoint
@app.route('/register', methods=['POST'])
def register():
    try:
        # Validate incoming data
        user_schema = UserSchema()
        user_data = user_schema.load(request.json)

        # Hash the password
        hashed_password = generate_password_hash(user_data['password'], method='sha256')

        # Create a new user
        new_user = User(username=user_data['username'], password=hashed_password, preferences=user_data.get('preferences'))
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully!"}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Preference Update Endpoint
@app.route('/preferences/<int:user_id>', methods=['PUT'])
def update_preferences(user_id):
    try:
        user = User.query.get_or_404(user_id)
        preferences = request.json.get('preferences')

        user.preferences = preferences
        db.session.commit()

        return jsonify({"message": "Preferences updated successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Match Firms Endpoint
@app.route('/match/<int:user_id>', methods=['GET'])
def match_firms(user_id):
    try:
        user = User.query.get_or_404(user_id)
        preferences = user.preferences

        # Get matched firms based on preferences
        matched_firms = match_investment_firms(preferences)

        return jsonify({"matched_firms": matched_firms}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', default=False))
```

### Requirements
To run the above code, ensure you have the following Python packages installed:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
```

### Note
Ensure to set up your environment correctly for production deployment, including secure password storage, database configuration, and proper error logging.
