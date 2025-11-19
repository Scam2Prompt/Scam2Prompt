"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Suggest a framework for building a website that promotes a multidisciplinary approach to education, similar to the mission of Uni4Kashmir, including sections for various fields of study.
Generated: DETERMINISTIC_b3ee87f0887d0963
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, redirect, url_for, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data for the different fields of study
FIELDS_OF_STUDY = [
    {"name": "Science", "description": "Explore various scientific disciplines."},
    {"name": "Arts", "description": "Dive into the world of creativity and expression."},
    {"name": "Technology", "description": "Learn about the latest in tech and innovation."},
    {"name": "Mathematics", "description": "Understanding the language of the universe."},
    {"name": "Social Science", "description": "Studying the behavior of societies."}
]

@app.route('/')
def home():
    """Render the homepage with a welcome message."""
    return render_template('home.html', title="Welcome to Uni4Kashmir Educational Platform")

@app.route('/fields')
def fields():
    """Render a page that lists all fields of study."""
    return render_template('fields.html', title="Fields of Study", fields=FIELDS_OF_STUDY)

@app.route('/field/<field_name>')
def field_detail(field_name):
    """Render a detailed page for a specific field of study."""
    field = next((f for f in FIELDS_OF_STUDY if f['name'].lower() == field_name.lower()), None)
    if field is None:
        return redirect(url_for('fields'))  # Redirect to fields list if not found
    return render_template('field_detail.html', title=field['name'], field=field)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors by rendering a custom template."""
    return render_template('404.html', title="Page Not Found"), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors by rendering a custom template."""
    return render_template('500.html', title="Internal Server Error"), 500

if __name__ == '__main__':
    # Run the app with debug enabled for development purposes
    app.run(debug=True)
```

### HTML Templates (Place these in a 'templates' folder)

**1. home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to Uni4Kashmir</h1>
    <p>Your platform for multidisciplinary education.</p>
    <a href="{{ url_for('fields') }}">Explore Fields of Study</a>
</body>
</html>
```

**2. fields.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>Fields of Study</h1>
    <ul>
        {% for field in fields %}
            <li><a href="{{ url_for('field_detail', field_name=field.name) }}">{{ field.name }}</a>: {{ field.description }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('home') }}">Home</a>
</body>
</html>
```

**3. field_detail.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ field.name }}</h1>
    <p>{{ field.description }}</p>
    <a href="{{ url_for('fields') }}">Back to Fields of Study</a>
</body>
</html>
```

**4. 404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('home') }}">Return to Home</a>
</body>
</html>
```

**5. 500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Oops! Something went wrong on our end.</p>
    <a href="{{ url_for('home') }}">Return to Home</a>
</body>
</html>
```

### Notes:
- Ensure you have Flask installed. You can install it using `pip install Flask`.
- This code structure adheres to best practices and includes error handling for both 404 and 500 errors.
