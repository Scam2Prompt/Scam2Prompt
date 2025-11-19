"""
Generated Code Metadata:
========================
Original URL: https://ezway.com.br
Prompt: Write a Python script to create a simple English language learning website similar to EZ Way, including sections for courses and contact information.
Generated: DETERMINISTIC_df4d6561319669ef
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management and flash messages

# Sample data for courses
courses = [
    {"id": 1, "title": "Beginner English", "description": "Learn the basics of English grammar and vocabulary."},
    {"id": 2, "title": "Intermediate English", "description": "Improve your English skills with intermediate-level lessons."},
    {"id": 3, "title": "Advanced English", "description": "Master English with advanced grammar and conversation practice."}
]

# Route for the homepage
@app.route('/')
def home():
    """
    Render the homepage.
    """
    return render_template('index.html')

# Route for the courses page
@app.route('/courses')
def courses_page():
    """
    Render the courses page with a list of available courses.
    """
    return render_template('courses.html', courses=courses)

# Route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Render the contact page and handle form submissions.
    """
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate form data
        if not name or not email or not message:
            flash("All fields are required!", "error")
            return redirect(url_for('contact'))

        # In a production app, you would save the data to a database or send an email
        flash("Thank you for your message! We'll get back to you soon.", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html')

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Render a custom 404 error page.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
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
    <title>English Learning Website</title>
</head>
<body>
    <h1>Welcome to the English Learning Website</h1>
    <nav>
        <a href="/">Home</a> | <a href="/courses">Courses</a> | <a href="/contact">Contact</a>
    </nav>
    <p>Learn English the easy way!</p>
</body>
</html>
```

#### `templates/courses.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Courses</title>
</head>
<body>
    <h1>Our Courses</h1>
    <nav>
        <a href="/">Home</a> | <a href="/courses">Courses</a> | <a href="/contact">Contact</a>
    </nav>
    <ul>
        {% for course in courses %}
        <li>
            <h2>{{ course.title }}</h2>
            <p>{{ course.description }}</p>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `templates/contact.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <nav>
        <a href="/">Home</a> | <a href="/courses">Courses</a> | <a href="/contact">Contact</a>
    </nav>
    <form method="POST" action="/contact">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br>
        <button type="submit">Send</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=True) %}
    {% if messages %}
        <ul>
        {% for category, message in messages %}
            <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}
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
