"""
Generated Code Metadata:
========================
Original URL: https://gcapmarkets.com
Prompt: Generate a code snippet for a basic financial advisory website that highlights the importance of ethics and professional quality in client interactions.
Generated: DETERMINISTIC_fddb5f6d95dca360
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with a secure secret key in production

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Render the home page with financial advisory information."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page highlighting ethics and professionalism."""
    return render_template('about.html', 
                          ethics_statement="We adhere to the highest ethical standards in all client interactions.",
                          quality_statement="Professional quality is at the core of our advisory services.")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle client contact form submissions."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic validation
        if not name or not email or not message:
            flash('Please fill out all fields.', 'error')
            return redirect(url_for('contact'))
        
        # Process the message (e.g., send email, save to database)
        flash('Thank you for your message. We will respond shortly.', 'success')
        return redirect(url_for('home'))
    
    return render_template('contact.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """Handle file uploads for document submissions."""
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected.', 'error')
            return redirect(url_for('upload_file'))
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected.', 'error')
            return redirect(url_for('upload_file'))
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid file type. Allowed types: pdf, txt, doc, docx.', 'error')
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

Here are the accompanying template files (place them in a `templates` folder):

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Advisory</title>
</head>
<body>
    <h1>Welcome to Our Financial Advisory Service</h1>
    <p>Providing ethical and professional financial guidance.</p>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About Us</a> |
        <a href="/contact">Contact</a> |
        <a href="/upload">Upload Documents</a>
    </nav>
    {% with messages = get_flashed_messages(with_categories=true) %}
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

**templates/about.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us</title>
</head>
<body>
    <h1>About Our Financial Advisory</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About Us</a> |
        <a href="/contact">Contact</a> |
        <a href="/upload">Upload Documents</a>
    </nav>
    <h2>Our Ethics</h2>
    <p>{{ ethics_statement }}</p>
    <h2>Our Professional Quality</h2>
    <p>{{ quality_statement }}</p>
</body>
</html>
```

**templates/contact.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Our Financial Advisors</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About Us</a> |
        <a href="/contact">Contact</a> |
        <a href="/upload">Upload Documents</a>
    </nav>
    <form method="POST" action="/contact">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

**templates/upload.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Upload</title>
</head>
<body>
    <h1>Upload Financial Documents</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About Us</a> |
        <a href="/contact">Contact</a> |
        <a href="/upload">Upload Documents</a>
    </nav>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
