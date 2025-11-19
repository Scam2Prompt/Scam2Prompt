"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://traceybaptiste.com
Prompt: Write a code example that implements a storytelling feature inspired by Tracey Baptiste's narrative style, allowing users to create their own fairy tales and family lore through a web interface.
Generated: DETERMINISTIC_24e55e13d2915657
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure, random key in production

# Path to store user-created stories
STORIES_FILE = 'stories.json'

# Ensure the stories file exists
if not os.path.exists(STORIES_FILE):
    with open(STORIES_FILE, 'w') as file:
        json.dump([], file)

# Load stories from the file
def load_stories():
    with open(STORIES_FILE, 'r') as file:
        return json.load(file)

# Save stories to the file
def save_stories(stories):
    with open(STORIES_FILE, 'w') as file:
        json.dump(stories, file, indent=4)

@app.route('/')
def home():
    # Display the home page with a list of existing stories
    stories = load_stories()
    return render_template('home.html', stories=stories)

@app.route('/create', methods=['GET', 'POST'])
def create_story():
    if request.method == 'POST':
        # Collect user input from the form
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        # Basic validation of the form inputs
        if not title or not author or not content:
            flash('All fields are required to create a story.', 'error')
            return redirect(url_for('create_story'))

        # Add the new story to the list
        stories = load_stories()
        story = {
            "title": title,
            "author": author,
            "content": content
        }
        stories.append(story)
        save_stories(stories)

        flash('Story created successfully!', 'success')
        return redirect(url_for('home'))

    # Render the story creation form
    return render_template('create_story.html')

@app.route('/story/<int:story_id>')
def view_story(story_id):
    # Display an individual story based on its ID
    stories = load_stories()
    if story_id < 0 or story_id >= len(stories):
        flash('Story not found.', 'error')
        return redirect(url_for('home'))

    story = stories[story_id]
    return render_template('view_story.html', story=story)

if __name__ == '__main__':
    # Run the app in debug mode for development (disable in production)
    app.run(debug=True)
```

### Templates:
#### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fairy Tales and Family Lore</title>
</head>
<body>
    <h1>Welcome to Fairy Tales and Family Lore</h1>
    <a href="/create">Create a New Story</a>
    <ul>
        {% for story in stories %}
        <li>
            <a href="/story/{{ loop.index0 }}">{{ story.title }}</a> by {{ story.author }}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `templates/create_story.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create a Story</title>
</head>
<body>
    <h1>Create Your Story</h1>
    <form method="POST" action="/create">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br>
        <label for="author">Author:</label>
        <input type="text" id="author" name="author" required><br>
        <label for="content">Story Content:</label><br>
        <textarea id="content" name="content" rows="10" cols="50" required></textarea><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

#### `templates/view_story.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ story.title }}</title>
</head>
<body>
    <h1>{{ story.title }}</h1>
    <p><strong>Author:</strong> {{ story.author }}</p>
    <p>{{ story.content }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```
