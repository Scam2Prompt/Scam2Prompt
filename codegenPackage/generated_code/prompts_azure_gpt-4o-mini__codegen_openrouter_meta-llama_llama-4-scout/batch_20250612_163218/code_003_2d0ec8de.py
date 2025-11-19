"""
Generated Code Metadata:
========================
Original URL: https://square-bear.co.uk
Prompt: Develop a simple web application that showcases a discography of a dance music producer, incorporating elements similar to those found on Square Bear's site.
Generated: DETERMINISTIC_2d0ec8dec1b22b09
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Discography Web Application**
=====================================

### Directory Structure
```markdown
discography-app/
|---- app.py
|---- templates/
|       |---- base.html
|       |---- discography.html
|       |---- album.html
|---- static/
|       |---- styles.css
|       |---- script.js
|---- data/
|       |---- albums.json
|---- requirements.txt
|---- README.md
```

### requirements.txt
```markdown
Flask==2.2.2
```

### data/albums.json
```json
[
  {
    "id": 1,
    "title": "Album 1",
    "release_date": "2020-01-01",
    "tracks": [
      {
        "id": 1,
        "title": "Track 1",
        "duration": "3:30"
      },
      {
        "id": 2,
        "title": "Track 2",
        "duration": "4:00"
      }
    ]
  },
  {
    "id": 2,
    "title": "Album 2",
    "release_date": "2021-01-01",
    "tracks": [
      {
        "id": 1,
        "title": "Track 1",
        "duration": "3:30"
      },
      {
        "id": 2,
        "title": "Track 2",
        "duration": "4:00"
      }
    ]
  }
]
```

### app.py
```python
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load albums data from JSON file
try:
    with open('data/albums.json') as f:
        albums_data = json.load(f)
except FileNotFoundError:
    print("Error: albums.json file not found.")
    albums_data = []

# Route for home page
@app.route('/')
def index():
    return render_template('base.html')

# Route for discography page
@app.route('/discography')
def discography():
    return render_template('discography.html', albums=albums_data)

# Route for album page
@app.route('/album/<int:album_id>')
def album(album_id):
    album = next((album for album in albums_data if album['id'] == album_id), None)
    if album is None:
        return render_template('404.html'), 404
    return render_template('album.html', album=album)

# API route for albums data
@app.route('/api/albums')
def albums_api():
    return jsonify(albums_data)

if __name__ == '__main__':
    app.run(debug=True)
```

### templates/base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discography App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('discography') }}">Discography</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
```

### templates/discography.html
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Discography</h1>
    <ul>
    {% for album in albums %}
        <li>
            <a href="{{ url_for('album', album_id=album.id) }}">{{ album.title }} ({{ album.release_date }})</a>
        </li>
    {% endfor %}
    </ul>
{% endblock %}
```

### templates/album.html
```html
{% extends 'base.html' %}

{% block content %}
    <h1>{{ album.title }} ({{ album.release_date }})</h1>
    <h2>Tracks:</h2>
    <ul>
    {% for track in album.tracks %}
        <li>{{ track.title }} ({{ track.duration }})</li>
    {% endfor %}
    </ul>
{% endblock %}
```

### static/styles.css
```css
body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav li {
    display: inline-block;
    margin-right: 20px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

h1, h2 {
    color: #333;
}

ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

a {
    text-decoration: none;
    color: #337ab7;
}

a:hover {
    color: #23527c;
}
```

### static/script.js
```javascript
// Add event listeners or other JavaScript functionality here
console.log('Script loaded');
```

### templates/404.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error: Page Not Found</h1>
</body>
</html>
```
