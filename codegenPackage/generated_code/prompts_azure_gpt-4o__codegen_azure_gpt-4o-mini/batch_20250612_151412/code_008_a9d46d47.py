"""
Generated Code Metadata:
========================
Original URL: https://grampreico.com
Prompt: Create a backend system for managing game updates and weekly content additions, inspired by nagoya168's frequent game updates.
Generated: DETERMINISTIC_a9d46d4790decd6e
Batch ID: 20250612_151412
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
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///game_updates.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the GameUpdate model
class GameUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the GameUpdate object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/updates', methods=['POST'])
def add_update():
    """Endpoint to add a new game update."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Title and content are required.'}), 400

    new_update = GameUpdate(title=data['title'], content=data['content'])
    
    try:
        db.session.add(new_update)
        db.session.commit()
        return jsonify(new_update.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/updates', methods=['GET'])
def get_updates():
    """Endpoint to retrieve all game updates."""
    updates = GameUpdate.query.all()
    return jsonify([update.to_dict() for update in updates]), 200

@app.route('/updates/<int:update_id>', methods=['GET'])
def get_update(update_id):
    """Endpoint to retrieve a specific game update by ID."""
    update = GameUpdate.query.get(update_id)
    if update is None:
        return jsonify({'error': 'Update not found.'}), 404
    return jsonify(update.to_dict()), 200

@app.route('/updates/<int:update_id>', methods=['PUT'])
def update_update(update_id):
    """Endpoint to update an existing game update."""
    data = request.get_json()
    update = GameUpdate.query.get(update_id)

    if update is None:
        return jsonify({'error': 'Update not found.'}), 404

    if 'title' in data:
        update.title = data['title']
    if 'content' in data:
        update.content = data['content']

    try:
        db.session.commit()
        return jsonify(update.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/updates/<int:update_id>', methods=['DELETE'])
def delete_update(update_id):
    """Endpoint to delete a game update."""
    update = GameUpdate.query.get(update_id)
    if update is None:
        return jsonify({'error': 'Update not found.'}), 404

    try:
        db.session.delete(update)
        db.session.commit()
        return jsonify({'message': 'Update deleted successfully.'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
