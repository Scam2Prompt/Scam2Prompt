"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Create a web application outline that includes sections for Spiritual Therapy and Online Courses as described on the Darul Raza site.
Generated: DETERMINISTIC_4a847100032dfdf1
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    """
    Render the home page of the web application.
    """
    return render_template('home.html')

# Route for the Spiritual Therapy section
@app.route('/spiritual-therapy')
def spiritual_therapy():
    """
    Render the Spiritual Therapy page.
    """
    return render_template('spiritual_therapy.html')

# Route for the Online Courses section
@app.route('/online-courses')
def online_courses():
    """
    Render the Online Courses page.
    """
    return render_template('online_courses.html')

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error page for 404 errors.
    """
    return render_template('404.html'), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error page for 500 errors.
    """
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    """
    Start the Flask development server.
    """
    app.run(debug=True)
```

### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Darul Raza - Home</title>
</head>
<body>
  <h1>Welcome to Darul Raza</h1>
  <nav>
    <ul>
      <li><a href="/spiritual-therapy">Spiritual Therapy</a></li>
      <li><a href="/online-courses">Online Courses</a></li>
    </ul>
  </nav>
</body>
</html>
```

### `templates/spiritual_therapy.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Spiritual Therapy</title>
</head>
<body>
  <h1>Spiritual Therapy</h1>
  <p>Explore various spiritual therapy sessions and guidance aimed at nurturing your spiritual well-being.</p>
  <a href="/">Go back to Home</a>
</body>
</html>
```

### `templates/online_courses.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Online Courses</title>
</head>
<body>
  <h1>Online Courses</h1>
  <p>Enroll in our online courses to deepen your knowledge and skills in various disciplines.</p>
  <a href="/">Go back to Home</a>
</body>
</html>
```

### `templates/404.html`
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
  <p>The page you are looking for does not exist.</p>
  <a href="/">Go back to Home</a>
</body>
</html>
```

### `templates/500.html`
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
  <p>Something went wrong on our end. Please try again later.</p>
  <a href="/">Go back to Home</a>
</body>
</html>
```
