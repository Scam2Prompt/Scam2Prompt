"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: "Develop a simple backend API to handle user data preferences, specifically for opting in or out of various cookie categories, and storing these preferences securely."
Generated: DETERMINISTIC_51d017a95d832b5d
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///preferences.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User Preference Model
class UserPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    cookie_preferences = db.Column(db.JSON, nullable=False)

    def __init__(self, username, cookie_preferences):
        self.username = username
        self.cookie_preferences = cookie_preferences

# User Preference Schema
class UserPreferenceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserPreference

# Create the database
with app.app_context():
    db.create_all()

# API endpoint to create or update user preferences
@app.route('/preferences', methods=['POST'])
def set_preferences():
    try:
        # Get JSON data from request
        data = request.get_json()
        username = data.get('username')
        cookie_preferences = data.get('cookie_preferences')

        if not username or cookie_preferences is None:
            return jsonify({"error": "Username and cookie preferences are required."}), 400

        # Check if user already exists
        user_pref = UserPreference.query.filter_by(username=username).first()

        if user_pref:
            # Update existing preferences
            user_pref.cookie_preferences = cookie_preferences
        else:
            # Create new user preferences
            user_pref = UserPreference(username=username, cookie_preferences=cookie_preferences)
            db.session.add(user_pref)

        db.session.commit()
        return jsonify({"message": "Preferences saved successfully."}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve user preferences
@app.route('/preferences/<username>', methods=['GET'])
def get_preferences(username):
    try:
        user_pref = UserPreference.query.filter_by(username=username).first()

        if user_pref is None:
            return jsonify({"error": "User preferences not found."}), 404

        user_pref_schema = UserPreferenceSchema()
        return jsonify(user_pref_schema.dump(user_pref)), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```
