"""
Generated Code Metadata:
========================
Original URL: https://samional.com
Prompt: Provide an example of a user-friendly web management panel that allows for easy content updates, similar to the functionality described on samional.com. Include code for basic CRUD operations.
Generated: DETERMINISTIC_5874580fc747a246
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Content model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Content {self.title}>'

# Route to render the management panel
@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

# Route to create new content
@app.route('/content', methods=['POST'])
def create_content():
    try:
        data = request.json
        new_content = Content(title=data['title'], body=data['body'])
        db.session.add(new_content)
        db.session.commit()
        return jsonify({'message': 'Content created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to read content
@app.route('/content/<int:content_id>', methods=['GET'])
def read_content(content_id):
    content = Content.query.get_or_404(content_id)
    return jsonify({'id': content.id, 'title': content.title, 'body': content.body})

# Route to update content
@app.route('/content/<int:content_id>', methods=['PUT'])
def update_content(content_id):
    try:
        data = request.json
        content = Content.query.get_or_404(content_id)
        content.title = data['title']
        content.body = data['body']
        db.session.commit()
        return jsonify({'message': 'Content updated successfully!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete content
@app.route('/content/<int:content_id>', methods=['DELETE'])
def delete_content(content_id):
    try:
        content = Content.query.get_or_404(content_id)
        db.session.delete(content)
        db.session.commit()
        return jsonify({'message': 'Content deleted successfully!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Content Management Panel</title>
</head>
<body>
    <h1>Content Management Panel</h1>
    <form id="contentForm">
        <input type="text" id="title" placeholder="Title" required>
        <textarea id="body" placeholder="Content" required></textarea>
        <button type="submit">Create Content</button>
    </form>
    <ul id="contentList">
        {% for content in contents %}
            <li>
                <strong>{{ content.title }}</strong>: {{ content.body }}
                <button onclick="deleteContent({{ content.id }})">Delete</button>
            </li>
        {% endfor %}
    </ul>

    <script>
        document.getElementById('contentForm').onsubmit = async function(event) {
            event.preventDefault();
            const title = document.getElementById('title').value;
            const body = document.getElementById('body').value;

            const response = await fetch('/content', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title, body })
            });

            if (response.ok) {
                location.reload();
            } else {
                alert('Error creating content');
            }
        };

        async function deleteContent(id) {
            const response = await fetch(`/content/${id}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                location.reload();
            } else {
                alert('Error deleting content');
            }
        }
    </script>
</body>
</html>
```

**Note:** Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```
