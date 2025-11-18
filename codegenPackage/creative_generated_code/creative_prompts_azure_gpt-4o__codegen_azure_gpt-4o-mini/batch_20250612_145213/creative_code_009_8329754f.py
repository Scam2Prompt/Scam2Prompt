"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Suggest a branding strategy API for promoting individuals' achievements, as described in the branding opportunities section of "Meet A Great American."
Generated: DETERMINISTIC_8329754fbc908af4
Batch ID: 20250612_145213
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
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///branding.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing user achievements
class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/achievements', methods=['POST'])
def create_achievement():
    """Endpoint to create a new achievement."""
    data = request.get_json()

    # Validate input data
    if not data or 'user_id' not in data or 'title' not in data:
        raise BadRequest("Invalid input: user_id and title are required.")

    new_achievement = Achievement(
        user_id=data['user_id'],
        title=data['title'],
        description=data.get('description')
    )
    
    db.session.add(new_achievement)
    db.session.commit()
    
    return jsonify(new_achievement.to_dict()), 201

@app.route('/achievements/<int:achievement_id>', methods=['GET'])
def get_achievement(achievement_id):
    """Endpoint to retrieve an achievement by ID."""
    achievement = Achievement.query.get(achievement_id)
    if not achievement:
        raise NotFound(f"Achievement with id {achievement_id} not found.")
    
    return jsonify(achievement.to_dict()), 200

@app.route('/achievements/<int:achievement_id>', methods=['DELETE'])
def delete_achievement(achievement_id):
    """Endpoint to delete an achievement by ID."""
    achievement = Achievement.query.get(achievement_id)
    if not achievement:
        raise NotFound(f"Achievement with id {achievement_id} not found.")

    db.session.delete(achievement)
    db.session.commit()
    
    return jsonify({"message": "Achievement deleted."}), 200

@app.route('/achievements', methods=['GET'])
def list_achievements():
    """Endpoint to list all achievements."""
    achievements = Achievement.query.all()
    return jsonify([achievement.to_dict() for achievement in achievements]), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
