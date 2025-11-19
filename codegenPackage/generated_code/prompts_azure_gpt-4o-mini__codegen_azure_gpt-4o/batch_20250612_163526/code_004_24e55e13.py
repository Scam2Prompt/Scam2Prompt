"""
Generated Code Metadata:
========================
Original URL: https://traceybaptiste.com
Prompt: Write a code example that implements a storytelling feature inspired by Tracey Baptiste's narrative style, allowing users to create their own fairy tales and family lore through a web interface.
Generated: DETERMINISTIC_24e55e13d2915657
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# storytelling_app.py

from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# In-memory storage for stories (in production, use a database)
stories = []

@app.route('/')
def home():
    """
    Render the homepage with a form for creating stories.
    """
    return render_template('index.html')

@app.route('/stories', methods=['GET'])
def get_stories():
    """
    Endpoint to retrieve all stories.
    """
    return jsonify({"stories": stories}), 200

@app.route('/stories', methods=['POST'])
def create_story():
    """
    Endpoint to create a new story.
    """
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        content = data.get('content')

        # Validate input
        if not title or not author or not content:
            return jsonify({"error": "Title, author, and content are required."}), 400

        # Create a new story object
        story = {
            "id": len(stories) + 1,
            "title": title,
            "author": author,
            "content": content
        }

        # Add the story to the in-memory storage
        stories.append(story)

        return jsonify({"message": "Story created successfully!", "story": story}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/stories/<int:story_id>', methods=['GET'])
def get_story(story_id):
    """
    Endpoint to retrieve a single story by ID.
    """
    story = next((s for s in stories if s['id'] == story_id), None)
    if story:
        return jsonify({"story": story}), 200
    else:
        return jsonify({"error": "Story not found."}), 404

@app.route('/stories/<int:story_id>', methods=['DELETE'])
def delete_story(story_id):
    """
    Endpoint to delete a story by ID.
    """
    global stories
    stories = [s for s in stories if s['id'] != story_id]
    return jsonify({"message": "Story deleted successfully."}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)

# index.html (to be placed in a 'templates' folder)
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Storytelling App</title>
</head>
<body>
    <h1>Welcome to the Storytelling App</h1>
    <form id="storyForm">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" required><br><br>
        <label for="author">Author:</label><br>
        <input type="text" id="author" name="author" required><br><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content" rows="5" required></textarea><br><br>
        <button type="submit">Submit Story</button>
    </form>
    <script>
        document.getElementById('storyForm').addEventListener('submit', async function(event) {
            event.preventDefault();
            const title = document.getElementById('title').value;
            const author = document.getElementById('author').value;
            const content = document.getElementById('content').value;

            const response = await fetch('/stories', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title, author, content })
            });

            const result = await response.json();
            if (response.ok) {
                alert('Story submitted successfully!');
            } else {
                alert(`Error: ${result.error}`);
            }
        });
    </script>
</body>
</html>
"""
```
