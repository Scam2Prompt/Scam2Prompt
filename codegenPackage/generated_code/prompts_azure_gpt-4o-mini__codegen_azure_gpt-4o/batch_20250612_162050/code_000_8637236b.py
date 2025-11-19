"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Generate a code snippet for a web application that showcases the unique features of Shelter's Bioethanol Fireplaces using Planika BEV Technology™.
Generated: DETERMINISTIC_8637236be4bfa8f0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask application to showcase Shelter's Bioethanol Fireplaces using Planika BEV Technology™

from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data representing unique features of Shelter's Bioethanol Fireplaces
fireplace_features = [
    {
        "title": "Eco-Friendly Design",
        "description": "Powered by Planika BEV Technology™, these fireplaces use bioethanol fuel, producing no smoke, ash, or soot."
    },
    {
        "title": "Safety First",
        "description": "Advanced sensors and automatic shut-off mechanisms ensure maximum safety during operation."
    },
    {
        "title": "Smart Control",
        "description": "Control your fireplace remotely via a mobile app or integrated smart home systems."
    },
    {
        "title": "Customizable Aesthetics",
        "description": "Available in various designs and finishes to complement any interior style."
    },
    {
        "title": "Efficient Heating",
        "description": "Provides effective heating while maintaining a clean and sustainable energy source."
    }
]

@app.route('/')
def home():
    """
    Render the homepage showcasing the unique features of Shelter's Bioethanol Fireplaces.
    """
    return render_template('index.html', features=fireplace_features)

@app.route('/api/features')
def api_features():
    """
    API endpoint to fetch the unique features of Shelter's Bioethanol Fireplaces.
    """
    return jsonify(fireplace_features)

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom message.
    """
    return render_template('404.html'), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors with a custom message.
    """
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML Templates (to be placed in a `templates` folder):

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shelter's Bioethanol Fireplaces</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .feature {
            margin-bottom: 20px;
        }
        .feature h2 {
            color: #555;
        }
        .feature p {
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Shelter's Bioethanol Fireplaces</h1>
        {% for feature in features %}
        <div class="feature">
            <h2>{{ feature.title }}</h2>
            <p>{{ feature.description }}</p>
        </div>
        {% endfor %}
    </div>
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
</body>
</html>
```

#### `500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Oops! Something went wrong on our end. Please try again later.</p>
</body>
</html>
```
