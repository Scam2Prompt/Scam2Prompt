"""
Generated Code Metadata:
========================
Original URL: https://maraboutreconnu.com
Prompt: Create a Python program using the Flask framework to showcase blog posts and services such as "Affaires de justice" and "Réussite Professionnelle," as described on the website.
Generated: DETERMINISTIC_a1406550136d6754
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, abort
from flask_caching import Cache

app = Flask(__name__)
app.config.from_object('config.Config')
cache = Cache(app)

# Sample in-memory data store for blog posts and services
blog_posts = [
    {'id': 1, 'title': 'Affaires de justice', 'content': 'Content for Affaires de justice'},
    {'id': 2, 'title': 'Réussite Professionnelle', 'content': 'Content for Réussite Professionnelle'},
]

services = [
    {'id': 1, 'name': 'Affaires de justice', 'description': 'Description for Affaires de justice'},
    {'id': 2, 'name': 'Réussite Professionnelle', 'description': 'Description for Réussite Professionnelle'},
]

@app.route('/')
def index():
    """Renders the homepage with blog posts and services"""
    return render_template('index.html', blog_posts=blog_posts, services=services)

@app.route('/blog-post/<int:post_id>')
def blog_post(post_id):
    """Renders a single blog post by ID"""
    post = next((post for post in blog_posts if post['id'] == post_id), None)
    if post is None:
        abort(404)
    return render_template('blog_post.html', post=post)

@app.route('/services')
def services_page():
    """Renders the services page"""
    return render_template('services.html', services=services)

@app.errorhandler(404)
def page_not_found(e):
    """Handles 404 errors"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Blog and Services</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <ul>
    {% for post in blog_posts %}
        <li><a href="{{ url_for('blog_post', post_id=post.id) }}">{{ post.title }}</a></li>
    {% endfor %}
    </ul>

    <h1>Services</h1>
    <ul>
    {% for service in services %}
        <li>{{ service.name }} - {{ service.description }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/blog_post.html -->

<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
</body>
</html>
```

```html
<!-- templates/services.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Services</title>
</head>
<body>
    <h1>Services</h1>
    <ul>
    {% for service in services %}
        <li>{{ service.name }} - {{ service.description }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

```python
# config.py

class Config:
    CACHE_TYPE = 'SimpleCache'
    CACHE_THRESHOLD = 1000
```

```bash
# requirements.txt

Flask==2.2.2
Flask-Caching==1.1.1
```
