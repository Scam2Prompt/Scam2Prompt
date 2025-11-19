"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Write a Python script to create a photography portfolio website with sections for wedding, fashion, and event photography, inspired by Officine dell'Immagine's services.
Generated: DETERMINISTIC_2b6310c681585984
Batch ID: 20250622_212148
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
"""
Photography Portfolio Website Generator
Creates a responsive portfolio website with sections for wedding, fashion, and event photography.
Inspired by Officine dell'Immagine's services.
"""

from flask import Flask, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    """Render the homepage with all portfolio sections."""
    return render_template('index.html')

@app.route('/wedding')
def wedding():
    """Render the wedding photography portfolio section."""
    images = get_images('wedding')
    return render_template('portfolio.html', category='Wedding', images=images)

@app.route('/fashion')
def fashion():
    """Render the fashion photography portfolio section."""
    images = get_images('fashion')
    return render_template('portfolio.html', category='Fashion', images=images)

@app.route('/events')
def events():
    """Render the event photography portfolio section."""
    images = get_images('events')
    return render_template('portfolio.html', category='Events', images=images)

def get_images(category):
    """Helper function to get images for a specific category."""
    image_dir = os.path.join(app.config['UPLOAD_FOLDER'], category)
    if not os.path.exists(image_dir):
        return []
    
    images = []
    for filename in os.listdir(image_dir):
        if allowed_file(filename):
            images.append({
                'url': f'/static/uploads/{category}/{filename}',
                'title': filename.split('.')[0].replace('_', ' ').title()
            })
    return images

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
    <title>Photography Portfolio</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <nav>
            <div class="logo">
                <a href="/">Photography Portfolio</a>
            </div>
            <ul class="nav-links">
                <li><a href="/wedding">Wedding</a></li>
                <li><a href="/fashion">Fashion</a></li>
                <li><a href="/events">Events</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div class="burger">
                <i class="fas fa-bars"></i>
            </div>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer id="contact">
        <div class="contact-info">
            <h3>Contact Us</h3>
            <p>Email: info@photographyportfolio.com</p>
            <p>Phone: +1 (555) 123-4567</p>
            <div class="social-links">
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-facebook"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
            </div>
        </div>
        <div class="copyright">
            <p>&copy; 2023 Photography Portfolio. All rights reserved.</p>
        </div>
    </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block content %}
<section class="hero">
    <div class="hero-content">
        <h1>Capturing Moments That Matter</h1>
        <p>Professional photography services for weddings, fashion, and events</p>
        <a href="#portfolio" class="btn">View Portfolio</a>
    </div>
</section>

<section id="portfolio" class="portfolio-preview">
    <h2>Our Work</h2>
    <div class="portfolio-categories">
        <div class="category">
            <a href="/wedding">
                <img src="/static/images/wedding-preview.jpg" alt="Wedding Photography">
                <h3>Wedding</h3>
            </a>
        </div>
        <div class="category">
            <a href="/fashion">
                <img src="/static/images/fashion-preview.jpg" alt="Fashion Photography">
                <h3>Fashion</h3>
            </a>
        </div>
        <div class="category">
            <a href="/events">
                <img src="/static/images/events-preview.jpg" alt="Event Photography">
                <h3>Events</h3>
            </a>
        </div>
    </div>
</section>

<section class="about">
    <h2>About Us</h2>
    <p>We are a team of professional photographers dedicated to capturing your special moments with creativity and passion. Inspired by Officine dell'Immagine, we strive for excellence in every shot.</p>
</section>
{% endblock %}
```

```html
<!-- templates/portfolio.html -->
{% extends "base.html" %}

{% block content %}
<section class="portfolio-header">
    <h1>{{ category }} Photography</h1>
    <p>Our curated collection of {{ category.lower() }} photography work</p>
</section>

<section class="gallery">
    {% if images %}
        <div class="grid">
            {% for image in images %}
                <div class="grid-item">
                    <img src="{{ image.url }}" alt="{{ image.title }}">
                    <div class="overlay">
                        <h3>{{ image.title }}</h3>
                    </div>
                </div>
            {% endfor %}
        </div>
    {% else %}
        <p class="no-images">No images available in this category yet.</p>
    {% endif %}
</section>
{% endblock %}
```

```css
/* static/css/style.css */
:root {
    --primary-color: #333;
    --secondary-color: #555;
    --accent-color: #8b5a2b;
    --light-color: #f8f8f8;
    --dark-color: #222;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: var(--primary-color);
}

header {
    background-color: var(--light-color);
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    position: fixed;
    width: 100%;
    z-index: 1000;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
}

.logo a {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--primary-color);
    text-decoration: none;
}

.nav-links {
    display: flex;
    list-style: none;
}

.nav-links li {
    margin-left: 2rem;
}

.nav-links a {
    text-decoration: none;
    color: var(--secondary-color);
    font-weight: 500;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: var(--accent-color);
}

.burger {
    display: none;
    cursor: pointer;
}

.hero {
    height: 100vh;
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/static/images/hero-bg.jpg');
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    padding-top: 80px;
}

.hero-content h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.hero-content p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

.btn {
    display: inline-block;
    background-color: var(--accent-color);
    color: white;
    padding: 0.8rem 1.5rem;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.
