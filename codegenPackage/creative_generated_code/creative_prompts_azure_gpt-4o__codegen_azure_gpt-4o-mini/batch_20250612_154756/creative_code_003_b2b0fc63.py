"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepn-walkin.com
Prompt: Develop a REST API that tracks a user's progress in STEPN, including their energy levels and costs for leveling up, as outlined in the blog.
Generated: DETERMINISTIC_b2b0fc6340a5b98b
Batch ID: 20250612_154756
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

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stepn_progress.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model to represent user progress
class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), unique=True, nullable=False)
    energy_level = db.Column(db.Integer, nullable=False)
    level_cost = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<UserProgress {self.user_id}>'

# Error handling for database integrity
@app.errorhandler(IntegrityError)
def handle_integrity_error(e):
    db.session.rollback()
    return jsonify({"error": "User ID must be unique."}), 409

# API route to create or update user progress
@app.route('/api/progress', methods=['POST'])
def create_or_update_progress():
    data = request.get_json()

    if not data or 'user_id' not in data or 'energy_level' not in data or 'level_cost' not in data:
        return jsonify({"error": "Invalid input."}), 400

    user_id = data['user_id']
    energy_level = data['energy_level']
    level_cost = data['level_cost']

    # Try to find existing user progress; if not found, create a new one
    user_progress = UserProgress.query.filter_by(user_id=user_id).first()
    if user_progress:
        # Update existing record
        user_progress.energy_level = energy_level
        user_progress.level_cost = level_cost
    else:
        # Create a new record
        user_progress = UserProgress(user_id=user_id, energy_level=energy_level, level_cost=level_cost)
        db.session.add(user_progress)

    # Commit changes to the database
    db.session.commit()

    return jsonify({"message": "Progress updated successfully."}), 200

# API route to retrieve user progress
@app.route('/api/progress/<string:user_id>', methods=['GET'])
def get_user_progress(user_id):
    user_progress = UserProgress.query.filter_by(user_id=user_id).first()

    if not user_progress:
        return jsonify({"error": "User not found."}), 404

    return jsonify({
        "user_id": user_progress.user_id,
        "energy_level": user_progress.energy_level,
        "level_cost": user_progress.level_cost
    }), 200

# Run the application
if __name__ == '__main__':
    # Create all tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Note**: Make sure to install the required packages before running the code:
```bash
pip install Flask Flask-SQLAlchemy
```
