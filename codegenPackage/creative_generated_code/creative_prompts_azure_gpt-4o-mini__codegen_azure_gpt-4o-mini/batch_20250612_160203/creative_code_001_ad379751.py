"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Generate an API that allows users to explore unique experiences at an eco-lodge, such as nature walks and art workshops, similar to those offered by the Boomgardi Sunland accommodation.
Generated: DETERMINISTIC_ad37975156956863
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Set up the database URI (replace with your actual database configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eco_lodge.db'  # Example using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Experience model
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Experience object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all experiences
@app.route('/api/experiences', methods=['GET'])
def get_experiences():
    """Fetch all unique experiences available at the eco-lodge."""
    try:
        experiences = Experience.query.all()
        return jsonify([exp.to_dict() for exp in experiences]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to add a new experience
@app.route('/api/experiences', methods=['POST'])
def add_experience():
    """Add a new unique experience to the eco-lodge."""
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Bad Request: Missing required fields'}), 400

    new_experience = Experience(
        title=data['title'],
        description=data['description'],
        price=data['price']
    )

    try:
        db.session.add(new_experience)
        db.session.commit()
        return jsonify(new_experience.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to get a specific experience by ID
@app.route('/api/experiences/<int:experience_id>', methods=['GET'])
def get_experience(experience_id):
    """Fetch a specific experience by its ID."""
    experience = Experience.query.get(experience_id)
    if experience is None:
        return jsonify({'error': 'Experience not found'}), 404
    return jsonify(experience.to_dict()), 200

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({'error': 'Internal Server Error'}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
