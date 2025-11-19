"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: Write a Python script to create a webpage showcasing the amenities of Dens Haven villas, including features like a swimming pool, clubhouse, landscaped garden, and CCTV monitoring system.
Generated: DETERMINISTIC_af39486e0fd1bb50
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template

app = Flask(__name__)

# Amenities data
AMENITIES = [
    {
        'name': 'Swimming Pool',
        'description': 'A large, well-maintained swimming pool for residents to relax and enjoy.',
        'image': 'pool.jpg'
    },
    {
        'name': 'Clubhouse',
        'description': 'Spacious clubhouse with modern facilities for events and gatherings.',
        'image': 'clubhouse.jpg'
    },
    {
        'name': 'Landscaped Garden',
        'description': 'Beautifully designed gardens with lush greenery and walking paths.',
        'image': 'garden.jpg'
    },
    {
        'name': 'CCTV Monitoring',
        'description': '24/7 CCTV surveillance for enhanced security and peace of mind.',
        'image': 'cctv.jpg'
    }
]

@app.route('/')
def home():
    """Render the homepage with amenities."""
    return render_template('index.html', amenities=AMENITIES)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dens Haven Villas - Amenities</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
        }
        header {
            background: #0056b3;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: 2rem 0;
        }
        .amenity {
            margin-bottom: 2rem;
            border-bottom: 1px solid #e4e4e4;
            padding-bottom: 1rem;
        }
        .amenity img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }
        h1, h2 {
            color: #0056b3;
        }
        footer {
            text-align: center;
            padding: 1rem 0;
            background: #0056b3;
            color: #fff;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Dens Haven Villas</h1>
        <p>Luxury living with premium amenities</p>
    </header>

    <div class="container">
        <h2>Our Amenities</h2>
        
        {% for amenity in amenities %}
        <div class="amenity">
            <h3>{{ amenity.name }}</h3>
            <img src="{{ url_for('static', filename='images/' + amenity.image) }}" alt="{{ amenity.name }}">
            <p>{{ amenity.description }}</p>
        </div>
        {% endfor %}
    </div>

    <footer>
        <p>&copy; 2023 Dens Haven Villas. All rights reserved.</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            font-size: 50px;
            color: #0056b3;
        }
        p {
            font-size: 20px;
        }
        a {
            color: #0056b3;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <h1>404</h1>
    <p>Oops! The page you're looking for doesn't exist.</p>
    <p><a href="{{ url_for('home') }}">Return to Home</a></p>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            font-size: 50px;
            color: #d9534f;
        }
        p {
            font-size: 20px;
        }
        a {
            color: #0056b3;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <h1>500</h1>
    <p>Something went wrong on our end. We're working to fix it!</p>
    <p><a href="{{ url_for('home') }}">Return to Home</a></p>
</body>
</html>
```
