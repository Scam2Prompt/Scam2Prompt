"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-mantra.net
Prompt: What are the best practices for building a web application that mimics the Stumble!® experience of discovering interesting content?
Generated: DETERMINISTIC_08865d1ce6d95f6f
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, redirect, url_for, request, jsonify
from random import choice
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the content model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Content {self.title}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to display a random piece of content
@app.route('/')
def index():
    try:
        # Fetch a random content entry
        content_list = Content.query.all()
        if not content_list:
            return render_template('index.html', error="No content available.")
        selected_content = choice(content_list)
        return render_template('index.html', content=selected_content)
    except Exception as e:
        return render_template('index.html', error=str(e))

# Route to add new content
@app.route('/add', methods=['POST'])
def add_content():
    try:
        # Get data from the request
        title = request.form.get('title')
        url = request.form.get('url')

        # Validate input
        if not title or not url:
            return jsonify({"error": "Title and URL are required."}), 400
        
        # Create and add new content instance
        new_content = Content(title=title, url=url)
        db.session.add(new_content)
        db.session.commit()
        
        return jsonify({"message": "Content added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete content by ID
@app.route('/delete/<int:content_id>', methods=['DELETE'])
def delete_content(content_id):
    try:
        # Find the content entry by ID
        content_to_delete = Content.query.get(content_id)
        if not content_to_delete:
            return jsonify({"error": "Content not found."}), 404
        
        # Delete the content entry
        db.session.delete(content_to_delete)
        db.session.commit()

        return jsonify({"message": "Content deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stumble!® Experience</title>
</head>
<body>
    <h1>Discover Interesting Content</h1>
    
    {% if content %}
        <h2>{{ content.title }}</h2>
        <a href="{{ content.url }}" target="_blank">Visit Content</a>
    {% elif error %}
        <p>{{ error }}</p>
    {% endif %}

    <h3>Add New Content</h3>
    <form action="/add" method="post">
        <input type="text" name="title" placeholder="Content Title" required>
        <input type="url" name="url" placeholder="Content URL" required>
        <button type="submit">Add Content</button>
    </form>
</body>
</html>
```

This code provides a Flask web application with basic functionality to add, view, and delete content similar to the Stumble!® experience. It includes error handling and validation to ensure robust operation.
