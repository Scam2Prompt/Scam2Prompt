"""
Generated Code Metadata:
========================
Original URL: https://phantomslens.com
Prompt: Write a Python script to create a portfolio website for a freelance artist with sections for music and horror projects, inspired by PhantomsLens.
Generated: DETERMINISTIC_80c93ab8935095d4
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Portfolio Website for Freelance Artist with Music and Horror Projects Sections

This script creates a simple Flask-based portfolio website for a freelance artist,
inspired by PhantomsLens, with dedicated sections for music and horror projects.

Features:
- Home page with artist introduction
- Music projects section
- Horror projects section
- Responsive design
- Contact form functionality
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Sample project data (replace with actual projects)
music_projects = [
    {
        'title': 'Album: Midnight Echoes',
        'description': 'A haunting ambient album inspired by urban legends',
        'image': 'music1.jpg',
        'year': 2023
    },
    {
        'title': 'Soundtrack: The Forgotten',
        'description': 'Original score for indie horror short film',
        'image': 'music2.jpg',
        'year': 2022
    }
]

horror_projects = [
    {
        'title': 'Short Film: The Whispering',
        'description': 'Supernatural horror short about a cursed radio station',
        'image': 'horror1.jpg',
        'year': 2023
    },
    {
        'title': 'Photography: Urban Decay',
        'description': 'Series exploring abandoned locations and their stories',
        'image': 'horror2.jpg',
        'year': 2021
    }
]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Render the home page with artist introduction."""
    return render_template('index.html')

@app.route('/music')
def music():
    """Render the music projects page."""
    return render_template('music.html', projects=music_projects)

@app.route('/horror')
def horror():
    """Render the horror projects page."""
    return render_template('horror.html', projects=horror_projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle contact form submissions."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if not name or not email or not message:
            flash('Please fill all fields', 'error')
            return redirect(url_for('contact'))
        
        # Here you would typically send an email or save to database
        flash('Your message has been sent!', 'success')
        return redirect(url_for('home'))
    
    return render_template('contact.html')

@app.route('/admin/upload', methods=['GET', 'POST'])
def upload_file():
    """Admin route for uploading project images."""
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded', 'success')
            return redirect(url_for('home'))
    
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
```

Note: This is the main Flask application file. You'll need to create corresponding HTML templates in a `templates` folder (index.html, music.html, horror.html, contact.html) and a `static` folder for CSS, JavaScript, and images. The actual implementation would also require proper styling and possibly JavaScript for enhanced interactivity.
