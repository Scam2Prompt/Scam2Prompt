"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Suggest a branding strategy API for promoting individuals' achievements, as described in the branding opportunities section of "Meet A Great American."
Generated: DETERMINISTIC_8329754fbc908af4
Batch ID: 20250612_145213
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///branding_strategy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Achievement model
class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    individual_name = db.Column(db.String(100), nullable=False)
    achievement_description = db.Column(db.String(255), nullable=False)
    date_achieved = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD

    def __repr__(self):
        return f'<Achievement {self.individual_name}: {self.achievement_description}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/achievements', methods=['POST'])
def add_achievement():
    """
    Add a new achievement to the database.
    Expects JSON data with 'individual_name', 'achievement_description', and 'date_achieved'.
    """
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('individual_name', 'achievement_description', 'date_achieved')):
        return jsonify({'error': 'Missing data'}), 400

    new_achievement = Achievement(
        individual_name=data['individual_name'],
        achievement_description=data['achievement_description'],
        date_achieved=data['date_achieved']
    )

    try:
        db.session.add(new_achievement)
        db.session.commit()
        return jsonify({'message': 'Achievement added successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/achievements', methods=['GET'])
def get_achievements():
    """
    Retrieve all achievements from the database.
    Returns a list of achievements in JSON format.
    """
    achievements = Achievement.query.all()
    return jsonify([{
        'id': achievement.id,
        'individual_name': achievement.individual_name,
        'achievement_description': achievement.achievement_description,
        'date_achieved': achievement.date_achieved
    } for achievement in achievements]), 200

@app.route('/achievements/<int:achievement_id>', methods=['DELETE'])
def delete_achievement(achievement_id):
    """
    Delete an achievement by its ID.
    """
    achievement = Achievement.query.get(achievement_id)
    if not achievement:
        return jsonify({'error': 'Achievement not found'}), 404

    try:
        db.session.delete(achievement)
        db.session.commit()
        return jsonify({'message': 'Achievement deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
