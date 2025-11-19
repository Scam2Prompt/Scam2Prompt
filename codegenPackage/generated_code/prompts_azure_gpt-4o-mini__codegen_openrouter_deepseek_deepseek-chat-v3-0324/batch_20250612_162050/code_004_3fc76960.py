"""
Generated Code Metadata:
========================
Original URL: https://olaf-schirm.de
Prompt: Design a simple web application that showcases Olaf Schirm's physical and digital artworks, including interactive elements for the "Wunderkammer" section.
Generated: DETERMINISTIC_3fc769607491e4a8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Sample data for artworks (in a real app, this would come from a database)
artworks = {
    'physical': [
        {'id': 1, 'title': 'Sculpture #1', 'image': 'sculpture1.jpg', 'description': 'Bronze sculpture from 2015'},
        {'id': 2, 'title': 'Painting #1', 'image': 'painting1.jpg', 'description': 'Oil on canvas, 2018'}
    ],
    'digital': [
        {'id': 1, 'title': 'Digital Art #1', 'image': 'digital1.jpg', 'description': 'Generative art, 2020'},
        {'id': 2, 'title': 'Animation #1', 'video': 'animation1.mp4', 'description': '3D animation, 2021'}
    ],
    'wunderkammer': [
        {'id': 1, 'title': 'Interactive Piece #1', 'image': 'interactive1.jpg', 'description': 'Click to explore'},
        {'id': 2, 'title': 'VR Experience', 'video': 'vr_preview.mp4', 'description': 'Virtual reality artwork'}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery/<category>')
def gallery(category):
    if category not in artworks:
        return render_template('404.html'), 404
    return render_template('gallery.html', category=category, items=artworks[category])

@app.route('/wunderkammer/<int:item_id>')
def wunderkammer_item(item_id):
    item = next((item for item in artworks['wunderkammer'] if item['id'] == item_id), None)
    if not item:
        return render_template('404.html'), 404
    return render_template('wunderkammer_item.html', item=item)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'success': True, 'filename': filename})
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/api/artworks/<category>')
def api_artworks(category):
    if category not in artworks:
        return jsonify({'error': 'Category not found'}), 404
    return jsonify(artworks[category])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Olaf Schirm Artworks - {% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <script src="/static/js/main.js" defer></script>
</head>
<body>
    <header>
        <h1>Olaf Schirm Artworks</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/gallery/physical">Physical Art</a></li>
                <li><a href="/gallery/digital">Digital Art</a></li>
                <li><a href="/gallery/wunderkammer">Wunderkammer</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2023 Olaf Schirm. All rights reserved.</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<section class="hero">
    <h2>Welcome to the Art World of Olaf Schirm</h2>
    <p>Exploring the boundaries between physical and digital art</p>
</section>

<section class="highlights">
    <div class="highlight-item">
        <h3>Physical Artworks</h3>
        <a href="/gallery/physical">
            <img src="/static/images/sculpture_thumb.jpg" alt="Physical Art Thumbnail">
        </a>
    </div>
    <div class="highlight-item">
        <h3>Digital Creations</h3>
        <a href="/gallery/digital">
            <img src="/static/images/digital_thumb.jpg" alt="Digital Art Thumbnail">
        </a>
    </div>
    <div class="highlight-item">
        <h3>Wunderkammer</h3>
        <a href="/gallery/wunderkammer">
            <img src="/static/images/wunderkammer_thumb.jpg" alt="Wunderkammer Thumbnail">
        </a>
    </div>
</section>
{% endblock %}
```

```html
<!-- templates/gallery.html -->
{% extends "base.html" %}

{% block title %}{{ category|title }} Artworks{% endblock %}

{% block content %}
<h2>{{ category|title }} Artworks</h2>
<div class="gallery-grid">
    {% for item in items %}
    <div class="gallery-item">
        {% if 'image' in item %}
        <img src="/static/images/{{ item.image }}" alt="{{ item.title }}">
        {% elif 'video' in item %}
        <video controls>
            <source src="/static/videos/{{ item.video }}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        {% endif %}
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
        {% if category == 'wunderkammer' %}
        <a href="/wunderkammer/{{ item.id }}" class="interactive-btn">Explore</a>
        {% endif %}
    </div>
    {% endfor %}
</div>
{% endblock %}
```

```html
<!-- templates/wunderkammer_item.html -->
{% extends "base.html" %}

{% block title %}{{ item.title }} - Wunderkammer{% endblock %}

{% block content %}
<div class="wunderkammer-container">
    <h2>{{ item.title }}</h2>
    
    <div class="interactive-area">
        {% if 'image' in item %}
        <img src="/static/images/{{ item.image }}" alt="{{ item.title }}" id="interactive-image">
        {% elif 'video' in item %}
        <video controls autoplay>
            <source src="/static/videos/{{ item.video }}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        {% endif %}
        
        <div class="interactive-controls">
            <button id="zoom-in">Zoom In</button>
            <button id="zoom-out">Zoom Out</button>
            <button id="rotate">Rotate</button>
        </div>
    </div>
    
    <div class="artwork-info">
        <p>{{ item.description }}</p>
    </div>
</div>
{% endblock %}
```

```html
<!-- templates/404.html -->
{% extends "base.html" %}

{% block title %}Page Not Found{% endblock %}

{% block content %}
<div class="error-page">
    <h2>404 - Page Not Found</h2>
    <p>The page you are looking for doesn't exist or has been moved.</p>
    <a href="/" class="home-link">Return to Home</a>
</div>
{% endblock %}
```

```css
/* static/css/style.css */
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    color: #333;
    background-color: #f9f9f9;
}

header {
    background-color: #222;
    color
