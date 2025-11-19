"""
Generated Code Metadata:
========================
Original URL: https://getupenergy.co.uk
Prompt: Generate a sample code for a simple health and wellness website that includes sections for blog posts, testimonials, and service descriptions, similar to the Get Up Energy website.
Generated: DETERMINISTIC_a5790fbd2b706d40
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask application for a simple health and wellness website
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for the website
blog_posts = [
    {"id": 1, "title": "5 Tips for a Healthier Lifestyle", "content": "Start your day with a healthy breakfast..."},
    {"id": 2, "title": "The Benefits of Regular Exercise", "content": "Exercise improves mental health..."},
]

testimonials = [
    {"id": 1, "name": "John Doe", "message": "This website changed my life!"},
    {"id": 2, "name": "Jane Smith", "message": "I feel healthier and more energetic every day."},
]

services = [
    {"id": 1, "name": "Personalized Nutrition Plans", "description": "Get a custom meal plan tailored to your needs."},
    {"id": 2, "name": "Fitness Coaching", "description": "Work with a professional coach to achieve your goals."},
]

@app.route('/')
def home():
    """
    Home page route.
    Displays the main sections of the website: blog posts, testimonials, and services.
    """
    return render_template('index.html', blog_posts=blog_posts, testimonials=testimonials, services=services)

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    """
    Blog post route.
    Displays a specific blog post based on its ID.
    """
    post = next((post for post in blog_posts if post["id"] == post_id), None)
    if not post:
        return jsonify({"error": "Blog post not found"}), 404
    return render_template('blog_post.html', post=post)

@app.route('/testimonials')
def testimonials_page():
    """
    Testimonials route.
    Displays all testimonials.
    """
    return render_template('testimonials.html', testimonials=testimonials)

@app.route('/services')
def services_page():
    """
    Services route.
    Displays all available services.
    """
    return render_template('services.html', services=services)

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (Place these in a `templates` folder)

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health and Wellness</title>
</head>
<body>
    <h1>Welcome to Our Health and Wellness Website</h1>
    <h2>Blog Posts</h2>
    <ul>
        {% for post in blog_posts %}
        <li><a href="/blog/{{ post.id }}">{{ post.title }}</a></li>
        {% endfor %}
    </ul>

    <h2>Testimonials</h2>
    <ul>
        {% for testimonial in testimonials %}
        <li>{{ testimonial.name }}: "{{ testimonial.message }}"</li>
        {% endfor %}
    </ul>

    <h2>Services</h2>
    <ul>
        {% for service in services %}
        <li>{{ service.name }}: {{ service.description }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `blog_post.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `testimonials.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Testimonials</title>
</head>
<body>
    <h1>Testimonials</h1>
    <ul>
        {% for testimonial in testimonials %}
        <li>{{ testimonial.name }}: "{{ testimonial.message }}"</li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `services.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Services</title>
</head>
<body>
    <h1>Our Services</h1>
    <ul>
        {% for service in services %}
        <li>{{ service.name }}: {{ service.description }}</li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```
