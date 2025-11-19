"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.drmanishmaladkar.com
Prompt: Create a REST API that serves inspirational short stories similar to those found in Dr. Maladkar's "Drishti – An Insight for Soul Enrichment" for a wellness app.
Generated: DETERMINISTIC_86893783b3082b40
Batch ID: 20250612_163103
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Story model
class Story(db.Model):
    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Converts the Story object to a dictionary."""
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
    """Fetches all stories from the database."""
    stories = Story.query.all()
    return jsonify([story.to_dict() for story in stories]), 200

@app.route('/stories/<int:story_id>', methods=['GET'])
def get_story(story_id):
    """Fetches a single story by its ID."""
    story = Story.query.get_or_404(story_id)
    return jsonify(story.to_dict()), 200

@app.route('/stories', methods=['POST'])
def create_story():
    """Creates a new story."""
    data = request.json
    if not data or not 'title' in data or not 'content' in data:
        return jsonify({"error": "Title and content are required."}), 400

    new_story = Story(title=data['title'], content=data['content'])
    try:
        db.session.add(new_story)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Story could not be created."}), 500

    return jsonify(new_story.to_dict()), 201

@app.route('/stories/<int:story_id>', methods=['PUT'])
def update_story(story_id):
    """Updates an existing story."""
    story = Story.query.get_or_404(story_id)
    data = request.json

    if 'title' in data:
        story.title = data['title']
    if 'content' in data:
        story.content = data['content']

    db.session.commit()
    return jsonify(story.to_dict()), 200

@app.route('/stories/<int:story_id>', methods=['DELETE'])
def delete_story(story_id):
    """Deletes a story by its ID."""
    story = Story.query.get_or_404(story_id)
    db.session.delete(story)
    db.session.commit()
    return jsonify({"message": "Story deleted successfully."}), 204

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the application: {e}")

```

Make sure to install the required dependencies by running:
```bash
pip install Flask Flask-SQLAlchemy
```

To initialize the database, run the script once to create the `stories.db` file. After that, you can use tools like Postman or CURL to interact with the API.
