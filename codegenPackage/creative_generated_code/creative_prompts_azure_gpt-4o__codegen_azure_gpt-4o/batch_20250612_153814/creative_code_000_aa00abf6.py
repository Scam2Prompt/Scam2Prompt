"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomdistro.com
Prompt: Write code to create a registration form that includes fields for DBA Name, Resale Certificate, State Tax ID, Federal EIN Document, Vape License Number, and Driving License, as described on PhantomDistro.com.
Generated: DETERMINISTIC_aa00abf6f5033300
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure secret key for session management (flash messages)
app.secret_key = 'your_secret_key'

# Configure upload folder and allowed file extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if a file extension is valid."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def register():
    """
    Handle the registration form. Displays the form on GET requests and processes
    submitted form data on POST requests.
    """
    if request.method == 'POST':
        # Fetch form data
        dba_name = request.form.get('dba_name')
        resale_certificate = request.files.get('resale_certificate')
        state_tax_id = request.form.get('state_tax_id')
        federal_ein_document = request.files.get('federal_ein_document')
        vape_license_number = request.form.get('vape_license_number')
        driving_license = request.files.get('driving_license')

        # Validate required fields
        if not dba_name or not state_tax_id or not vape_license_number:
            flash("DBA Name, State Tax ID, and Vape License Number are required fields.", 'error')
            return redirect(url_for('register'))

        # Validate and save uploaded files
        uploaded_files = {}
        for file_field, file_obj in {
            'resale_certificate': resale_certificate,
            'federal_ein_document': federal_ein_document,
            'driving_license': driving_license,
        }.items():
            if file_obj and allowed_file(file_obj.filename):
                filename = secure_filename(file_obj.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file_obj.save(file_path)
                uploaded_files[file_field] = file_path
            elif file_obj:
                flash(f"Invalid file type for {file_field}. Please upload PDF, JPG, JPEG, or PNG files.", 'error')
                return redirect(url_for('register'))

        # Success message for form submission
        flash("Registration form submitted successfully!", 'success')
        return redirect(url_for('register'))

    return render_template('register.html')

# HTML template for the registration form
@app.route('/register.html')
def register_html():
    """
    Serve the registration template.
    """
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Registration Form</title>
    </head>
    <body>
        <h1>Registration Form</h1>
        <form method="POST" enctype="multipart/form-data">
            <label for="dba_name">DBA Name:</label>
            <input type="text" id="dba_name" name="dba_name" required><br><br>
            
            <label for="resale_certificate">Resale Certificate:</label>
            <input type="file" id="resale_certificate" name="resale_certificate"><br><br>
            
            <label for="state_tax_id">State Tax ID:</label>
            <input type="text" id="state_tax_id" name="state_tax_id" required><br><br>
            
            <label for="federal_ein_document">Federal EIN Document:</label>
            <input type="file" id="federal_ein_document" name="federal_ein_document"><br><br>
            
            <label for="vape_license_number">Vape License Number:</label>
            <input type="text" id="vape_license_number" name="vape_license_number" required><br><br>
            
            <label for="driving_license">Driving License:</label>
            <input type="file" id="driving_license" name="driving_license"><br><br>
            
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
