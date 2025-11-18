"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-daomars-com.pages.dev
Prompt: Create a grant application submission form for the MarsDAO grant system, ensuring compatibility with the MarsDAO ecosystem.
Generated: DETERMINISTIC_2d22a7b818c40d83
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for web application development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application to use a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Set maximum file size to 16 MB
app.secret_key = 'your_secret_key_here'

# Initialize the database
db = SQLAlchemy(app)

# Define the GrantApplication model for the database
class GrantApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    project_title = db.Column(db.String(200), nullable=False)
    project_description = db.Column(db.Text, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    resume_file = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<GrantApplication {self.id} - {self.project_title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to display the grant application form
@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        try:
            # Collecting data from the form
            applicant_name = request.form['applicant_name']
            project_title = request.form['project_title']
            project_description = request.form['project_description']
            budget = float(request.form['budget'])

            # Handling file upload
            resume_file = request.files['resume_file']
            if resume_file and allowed_file(resume_file.filename):
                filename = secure_filename(resume_file.filename)
                resume_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                filename = None

            # Creating a new grant application entry
            new_application = GrantApplication(
                applicant_name=applicant_name,
                project_title=project_title,
                project_description=project_description,
                budget=budget,
                resume_file=filename
            )

            # Adding the entry to the database
            db.session.add(new_application)
            db.session.commit()

            flash('Application submitted successfully!', 'success')
            return redirect(url_for('apply'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')
            return redirect(url_for('apply'))

    return render_template('apply.html')

# Function to check allowed file extensions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
``` 

```html
<!-- apply.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grant Application Form</title>
</head>
<body>
    <h1>Grant Application Submission</h1>
    <form method="POST" enctype="multipart/form-data">
        <label for="applicant_name">Applicant Name:</label>
        <input type="text" id="applicant_name" name="applicant_name" required><br>

        <label for="project_title">Project Title:</label>
        <input type="text" id="project_title" name="project_title" required><br>

        <label for="project_description">Project Description:</label>
        <textarea id="project_description" name="project_description" required></textarea><br>

        <label for="budget">Budget ($):</label>
        <input type="number" id="budget" name="budget" step="0.01" required><br>

        <label for="resume_file">Resume (PDF/DOC/DOCX):</label>
        <input type="file" id="resume_file" name="resume_file"><br>

        <input type="submit" value="Submit Application">
    </form>

    <!-- Display flash messages here -->
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
