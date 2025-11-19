"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: "Develop a simple web application using Flask that provides a guided meditation and eye exercise program for reducing eye strain and improving vision, incorporating techniques from the Klar Sehen website."
Generated: DETERMINISTIC_03809f11d280e1de
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, jsonify
import time

# Initialize the Flask application
app = Flask(__name__)

# Routes
@app.route('/')
def home():
    """
    Home route that renders the main page.
    """
    return render_template('index.html')

@app.route('/meditation', methods=['GET'])
def guided_meditation():
    """
    Route for guided meditation instructions.
    """
    meditation_steps = [
        "Sit comfortably and close your eyes.",
        "Take a deep breath in through your nose and exhale slowly through your mouth.",
        "Focus on your breathing. Inhale deeply, hold for a few seconds, and exhale.",
        "Visualize a peaceful place, such as a beach or forest.",
        "Continue this process for 5-10 minutes."
    ]
    return jsonify({"steps": meditation_steps})

@app.route('/eye_exercises', methods=['GET'])
def eye_exercises():
    """
    Route for eye exercise instructions.
    """
    eye_exercise_steps = [
        "Blink your eyes slowly 10 times.",
        "Look up, down, left, and right without moving your head.",
        "Focus on a distant object for 20 seconds, then a nearby object for 20 seconds.",
        "Rub your palms together to generate heat and place them gently over your closed eyes.",
        "Repeat these exercises 2-3 times daily."
    ]
    return jsonify({"steps": eye_exercise_steps})

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler.
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom 500 error handler.
    """
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML Templates

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guided Meditation and Eye Exercises</title>
</head>
<body>
    <h1>Welcome to the Guided Meditation and Eye Exercise Program</h1>
    <p>Choose an option below:</p>
    <ul>
        <li><a href="/meditation">Guided Meditation</a></li>
        <li><a href="/eye_exercises">Eye Exercises</a></li>
    </ul>
</body>
</html>
```

#### `templates/404.html`
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
    <a href="/">Go back to the homepage</a>
</body>
</html>
```

#### `templates/500.html`
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
    <a href="/">Go back to the homepage</a>
</body>
</html>
```
