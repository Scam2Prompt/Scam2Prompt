"""
Generated Code Metadata:
========================
Original URL: https://mint.fuckopensea.art
Prompt: Generate code for a form submission system that collects user horror stories about OpenSea, similar to the rewards submission form described on the "Fuck OpenSea" website.
Generated: DETERMINISTIC_63111786b6ba2968
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# horror_story_submitter.py

import os
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///horror_stories.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class HorrorStory(db.Model):
    """Represents a horror story about OpenSea."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    story = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'HorrorStory({self.name}, {self.email})'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'story': self.story
        }

@app.route('/submit', methods=['POST'])
def submit_horror_story():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400

        name = data.get('name')
        email = data.get('email')
        story = data.get('story')

        if not all([name, email, story]):
            return jsonify({'error': 'Please fill out all fields'}), 400

        horror_story = HorrorStory(name=name, email=email, story=story)
        db.session.add(horror_story)
        db.session.commit()

        logger.info(f'Horror story submitted by {name} ({email})')
        return jsonify({'message': 'Horror story submitted successfully'}), 201
    except Exception as e:
        logger.error(f'Error submitting horror story: {e}')
        db.session.rollback()
        return jsonify({'error': 'Failed to submit horror story'}), 500

@app.route('/stories', methods=['GET'])
def get_horror_stories():
    try:
        stories = HorrorStory.query.all()
        return jsonify([story.to_dict() for story in stories]), 200
    except Exception as e:
        logger.error(f'Error fetching horror stories: {e}')
        return jsonify({'error': 'Failed to fetch horror stories'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=os.environ.get('DEBUG', False))
```

```python
# requirements.txt
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
```

```python
# .env
DATABASE_URL=sqlite:///horror_stories.db
DEBUG=True
```
