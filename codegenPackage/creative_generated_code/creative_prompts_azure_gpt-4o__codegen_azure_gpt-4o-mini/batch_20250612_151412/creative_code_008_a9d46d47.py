"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grampreico.com
Prompt: Create a backend system for managing game updates and weekly content additions, inspired by nagoya168's frequent game updates.
Generated: DETERMINISTIC_a9d46d4790decd6e
Batch ID: 20250612_151412
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
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game_updates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Game Updates
class GameUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the GameUpdate instance to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date_added": self.date_added.isoformat()
        }

# Endpoint to add a new game update
@app.route('/updates', methods=['POST'])
def add_update():
    try:
        data = request.json
        title = data.get('title')
        description = data.get('description')

        if not title or not description:
            return jsonify({"error": "Title and description are required"}), 400
        
        new_update = GameUpdate(title=title, description=description)
        db.session.add(new_update)
        db.session.commit()
        return jsonify(new_update.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all game updates
@app.route('/updates', methods=['GET'])
def get_updates():
    try:
        updates = GameUpdate.query.all()
        return jsonify([update.to_dict() for update in updates]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific game update by ID
@app.route('/updates/<int:update_id>', methods=['GET'])
def get_update(update_id):
    try:
        update = GameUpdate.query.get_or_404(update_id)
        return jsonify(update.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a game update
@app.route('/updates/<int:update_id>', methods=['DELETE'])
def delete_update(update_id):
    try:
        update = GameUpdate.query.get_or_404(update_id)
        db.session.delete(update)
        db.session.commit()
        return jsonify({"message": "Update deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Create the database before the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    # Ensure the database directory exists
    if not os.path.exists('game_updates.db'):
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```

This code sets up a basic Flask application for managing game updates with features to create, retrieve, and delete updates. It uses SQLite as the database and includes error handling for various scenarios.
