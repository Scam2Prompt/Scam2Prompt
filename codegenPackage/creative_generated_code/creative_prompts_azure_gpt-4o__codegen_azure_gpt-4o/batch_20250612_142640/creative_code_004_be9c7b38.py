"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looks-rare.com
Prompt: Create a web application that allows artists to submit their portfolios for review, modeled after the application process described on the Looks Rare site.
Generated: DETERMINISTIC_be9c7b38a24156c7
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a simple web application that allows artists to submit their portfolios for review. The application is built using Python with the Flask framework and includes MongoDB as a database for storing portfolio submissions.

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import pymongo
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration
app.secret_key = 'your_secret_key_here'  # Replace with your own secret key
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017"
client = pymongo.MongoClient(MONGO_URI)
db = client['artist_portfolios']
collection = db['submissions']

# Ensure uploads directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/')
def index():
    """
    Render the home page with the submission form.
    """
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_portfolio():
    """
    Handle portfolio submission.
    """
    try:
        name = request.form['name']
        email = request.form['email']
        description = request.form['description']
        file = request.files['portfolio']

        # Validate inputs
        if not name or not email or not description or not file:
            flash('All fields are required.', 'error')
            return redirect(url_for('index'))

        if not allowed_file(file.filename):
            flash('Invalid file type. Allowed types: png, jpg, jpeg, pdf.', 'error')
            return redirect(url_for('index'))

        # Save the file securely
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Store submission in the database
        submission = {
            'name': name,
            'email': email,
            'description': description,
            'file_path': file_path,
            'submitted_at': datetime.now()
        }
        collection.insert_one(submission)

        flash('Portfolio submitted successfully!', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/submissions')
def view_submissions():
    """
    Render a page to view all portfolio submissions.
    """
    submissions = collection.find()
    return render_template('submissions.html', submissions=submissions)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Template: `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio Submission</title>
</head>
<body>
    <h1>Submit Your Portfolio</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        <ul>
        {% for category, message in messages %}
            <li style="color: {{ 'red' if category == 'error' else 'green' }}">{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}
    <form action="/submit" method="post" enctype="multipart/form-data">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <label for="description">Portfolio Description:</label><br>
        <textarea id="description" name="description" rows="5" required></textarea><br><br>
        <label for="portfolio">Upload Portfolio File:</label>
        <input type="file" id="portfolio" name="portfolio" required><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### Template: `templates/submissions.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio Submissions</title>
</head>
<body>
    <h1>Portfolio Submissions</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Description</th>
                <th>File Path</th>
                <th>Submission Date</th>
            </tr>
        </thead>
        <tbody>
            {% for submission in submissions %}
            <tr>
                <td>{{ submission.name }}</td>
                <td>{{ submission.email }}</td>
                <td>{{ submission.description }}</td>
                <td><a href="{{ submission.file_path }}">View File</a></td>
                <td>{{ submission.submitted_at }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

### Notes:
1. Install dependencies: `Flask`, `pymongo`, and any others as required (`pip install flask pymongo`).
2. Start MongoDB before running the app.
3. Set appropriate permissions for the `uploads` directory.
