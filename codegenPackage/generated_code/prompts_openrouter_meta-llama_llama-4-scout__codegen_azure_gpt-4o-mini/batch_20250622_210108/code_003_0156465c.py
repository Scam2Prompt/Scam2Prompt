"""
Generated Code Metadata:
========================
Original URL: https://lifes.quest
Prompt: Design an API for a "spiritual growth" app that provides users with daily devotionals, prayer prompts, and scripture readings, using the content from lifes.quest as a reference.
Generated: DETERMINISTIC_0156465c482e8d32
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devotionals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Devotional model
class Devotional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)

    def to_dict(self):
        """Convert the Devotional object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'date': self.date.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/devotionals', methods=['GET'])
def get_devotionals():
    """Retrieve all devotionals."""
    devotionals = Devotional.query.all()
    return jsonify([devotional.to_dict() for devotional in devotionals]), 200

@app.route('/devotionals/<int:id>', methods=['GET'])
def get_devotional(id):
    """Retrieve a specific devotional by ID."""
    devotional = Devotional.query.get(id)
    if devotional is None:
        return jsonify({'error': 'Devotional not found'}), 404
    return jsonify(devotional.to_dict()), 200

@app.route('/devotionals', methods=['POST'])
def create_devotional():
    """Create a new devotional."""
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_devotional = Devotional(title=data['title'], content=data['content'])
    db.session.add(new_devotional)
    db.session.commit()
    return jsonify(new_devotional.to_dict()), 201

@app.route('/daily_prompt', methods=['GET'])
def daily_prompt():
    """Provide a random daily prayer prompt."""
    prompts = [
        "Pray for guidance in your daily decisions.",
        "Ask for strength to overcome challenges.",
        "Thank God for the blessings in your life.",
        "Pray for peace in your heart and mind."
    ]
    return jsonify({'prompt': random.choice(prompts)}), 200

@app.route('/scripture_reading', methods=['GET'])
def scripture_reading():
    """Provide a random scripture reading."""
    scriptures = [
        "Philippians 4:6-7",
        "Psalm 23:1-3",
        "Isaiah 40:31",
        "Romans 8:28"
    ]
    return jsonify({'scripture': random.choice(scriptures)}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
