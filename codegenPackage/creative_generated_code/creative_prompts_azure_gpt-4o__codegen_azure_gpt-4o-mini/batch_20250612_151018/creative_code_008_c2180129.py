"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Suggest tools or frameworks to build a directory search feature for FOSS@RIT profiles, allowing users to find members by their programming language preferences (e.g., Rust, Python).
Generated: DETERMINISTIC_c2180129891592fb
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (e.g., SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foss_rit_profiles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the UserProfile model
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    programming_languages = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<UserProfile {self.name}>"

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to search for profiles by programming language
@app.route('/search', methods=['GET'])
def search_profiles():
    """
    Search for user profiles by programming language.
    Query parameter `language` must be provided.
    Returns a JSON list of profiles matching the language.
    """
    language = request.args.get('language')
    
    if not language:
        return jsonify({"error": "No programming language provided."}), 400

    try:
        # Query the database for profiles that contain the specified language
        results = UserProfile.query.filter(UserProfile.programming_languages.like(f"%{language}%")).all()
        profiles = [{"id": profile.id, "name": profile.name, "programming_languages": profile.programming_languages} for profile in results]

        return jsonify(profiles), 200

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session in case of an error
        return jsonify({"error": str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
