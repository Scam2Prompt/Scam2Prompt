"""
Generated Code Metadata:
========================
Original URL: https://jasmynetwork.org
Prompt: Write code to create a personalized content discovery feed similar to the functionality described on the Stumble! ® platform, ensuring no ads are displayed and users can submit and share web finds.
Generated: DETERMINISTIC_fdad0c4096dba23b
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content_feed.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing user-submitted content
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Content {self.title}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to submit new content
@app.route('/submit', methods=['POST'])
def submit_content():
    data = request.json
    title = data.get('title')
    url = data.get('url')
    description = data.get('description')

    if not title or not url:
        return jsonify({'error': 'Title and URL are required.'}), 400

    new_content = Content(title=title, url=url, description=description)

    try:
        db.session.add(new_content)
        db.session.commit()
        return jsonify({'message': 'Content submitted successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Content with this URL already exists.'}), 409

# Route to get a random piece of content
@app.route('/discover', methods=['GET'])
def discover_content():
    content_list = Content.query.all()
    if not content_list:
        return jsonify({'message': 'No content available.'}), 404

    random_content = random.choice(content_list)
    return jsonify({
        'id': random_content.id,
        'title': random_content.title,
        'url': random_content.url,
        'description': random_content.description
    })

# Route to get all submitted content
@app.route('/content', methods=['GET'])
def get_all_content():
    content_list = Content.query.all()
    return jsonify([
        {
            'id': content.id,
            'title': content.title,
            'url': content.url,
            'description': content.description
        } for content in content_list
    ])

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found.'}), 404

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
