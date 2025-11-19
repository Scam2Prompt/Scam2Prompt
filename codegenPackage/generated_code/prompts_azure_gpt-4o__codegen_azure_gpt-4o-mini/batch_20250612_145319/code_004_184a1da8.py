"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: Suggest tools or libraries for creating a portfolio website showcasing residential, commercial, and aviation interior design projects, similar to Zirciulit Design Firm's portfolio.
Generated: DETERMINISTIC_184a1da8d4e11970
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_website.py

from flask import Flask, render_template, request, redirect, url_for, flash
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for production

# Configuration for file uploads
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Home route to display the portfolio
@app.route('/')
def home():
    """Render the home page showcasing the portfolio."""
    return render_template('index.html')

# Route to handle project submissions
@app.route('/submit_project', methods=['POST'])
def submit_project():
    """Handle project submission from the user."""
    if 'project_file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['project_file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file:
        try:
            # Save the file to the upload folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            flash('Project submitted successfully!')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f'An error occurred while saving the file: {str(e)}')
            return redirect(request.url)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 error page."""
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    """Render a custom 500 error page."""
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <h1>Welcome to Our Interior Design Portfolio</h1>
    <form action="/submit_project" method="post" enctype="multipart/form-data">
        <label for="project_file">Upload your project file:</label>
        <input type="file" name="project_file" id="project_file" required>
        <button type="submit">Submit Project</button>
    </form>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
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
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
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
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Sorry, something went wrong on our end.</p>
</body>
</html>
```

```css
/* static/styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
}

h1 {
    color: #333;
}

form {
    margin-top: 20px;
}

input[type="file"] {
    margin-bottom: 10px;
}
```
