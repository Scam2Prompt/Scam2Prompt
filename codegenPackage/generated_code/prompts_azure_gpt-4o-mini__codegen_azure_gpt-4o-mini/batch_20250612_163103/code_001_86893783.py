"""
Generated Code Metadata:
========================
Original URL: https://www.drmanishmaladkar.com
Prompt: Create a REST API that serves inspirational short stories similar to those found in Dr. Maladkar's "Drishti – An Insight for Soul Enrichment" for a wellness app.
Generated: DETERMINISTIC_86893783b3082b40
Batch ID: 20250612_163103
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Story model
class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Story object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/stories', methods=['GET'])
def get_stories():
    """Retrieve all stories from the database."""
    stories = Story.query.all()
    return jsonify([story.to_dict() for story in stories]), 200

@app.route('/stories', methods=['POST'])
def add_story():
    """Add a new story to the database."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Title and content are required.'}), 400

    new_story = Story(title=data['title'], content=data['content'])
    
    try:
        db.session.add(new_story)
        db.session.commit()
        return jsonify(new_story.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Story could not be added.'}), 500

@app.route('/stories/<int:story_id>', methods=['GET'])
def get_story(story_id):
    """Retrieve a specific story by its ID."""
    story = Story.query.get(story_id)
    if story is None:
        return jsonify({'error': 'Story not found.'}), 404
    return jsonify(story.to_dict()), 200

@app.route('/stories/<int:story_id>', methods=['PUT'])
def update_story(story_id):
    """Update an existing story."""
    data = request.get_json()
    story = Story.query.get(story_id)

    if story is None:
        return jsonify({'error': 'Story not found.'}), 404

    if 'title' in data:
        story.title = data['title']
    if 'content' in data:
        story.content = data['content']

    db.session.commit()
    return jsonify(story.to_dict()), 200

@app.route('/stories/<int:story_id>', methods=['DELETE'])
def delete_story(story_id):
    """Delete a story by its ID."""
    story = Story.query.get(story_id)
    if story is None:
        return jsonify({'error': 'Story not found.'}), 404

    db.session.delete(story)
    db.session.commit()
    return jsonify({'message': 'Story deleted successfully.'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
