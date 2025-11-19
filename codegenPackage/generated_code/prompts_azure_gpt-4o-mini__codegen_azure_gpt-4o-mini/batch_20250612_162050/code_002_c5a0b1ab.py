"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: Write a Python script that simulates an "Aula Invertida" learning environment, allowing students to access simplified educational materials online.
Generated: DETERMINISTIC_c5a0b1abfc54cf38
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aula_invertida.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Initialize the database
db = SQLAlchemy(app)

# Model for educational materials
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Material {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    materials = Material.query.all()
    return render_template('index.html', materials=materials)

# Route to upload new educational materials
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        file = request.files['file']

        # Validate file upload
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Create a new Material entry
            new_material = Material(title=title, description=description, file_path=file_path)
            db.session.add(new_material)
            db.session.commit()
            flash('Material uploaded successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid file type. Please upload a valid file.', 'danger')

    return render_template('upload.html')

# Function to check allowed file types
def allowed_file(filename):
    allowed_extensions = {'pdf', 'doc', 'docx', 'ppt', 'pptx', 'txt'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Route to view a specific educational material
@app.route('/material/<int:material_id>')
def material(material_id):
    material = Material.query.get_or_404(material_id)
    return render_template('material.html', material=material)

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    # Ensure the upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    app.run(debug=True)  # Set debug=False in production
```

### HTML Templates
You will need to create the following HTML templates in a `templates` directory:

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula Invertida</title>
</head>
<body>
    <h1>Educational Materials</h1>
    <a href="{{ url_for('upload') }}">Upload New Material</a>
    <ul>
        {% for material in materials %}
            <li>
                <a href="{{ url_for('material', material_id=material.id) }}">{{ material.title }}</a>
                - {{ material.description }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. **upload.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Material</title>
</head>
<body>
    <h1>Upload Educational Material</h1>
    <form method="POST" enctype="multipart/form-data">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <br>
        <label for="description">Description:</label>
        <input type="text" name="description" required>
        <br>
        <label for="file">File:</label>
        <input type="file" name="file" required>
        <br>
        <input type="submit" value="Upload">
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

3. **material.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ material.title }}</title>
</head>
<body>
    <h1>{{ material.title }}</h1>
    <p>{{ material.description }}</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
    <br>
    <a href="{{ url_for('static', filename=material.file_path) }}">Download Material</a>
</body>
</html>
```

4. **404.html**
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
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Note
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- Adjust the `UPLOAD_FOLDER` path and `secret_key` as needed for your production environment.
