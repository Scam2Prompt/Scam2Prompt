"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Suggest a library or framework to build an e-commerce platform for automotive parts, inspired by the layout and functionality of "autopecasbrazz."
Generated: DETERMINISTIC_78a1a43176ca7a52
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database and file uploads
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16MB
app.secret_key = 'your_secret_key'  # Secret key for session management

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the database model for automotive parts
class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Part {self.name}>'

# Route to display all parts
@app.route('/')
def index():
    all_parts = Part.query.all()  # Query all parts from the database
    return render_template('index.html', parts=all_parts)

# Route to add a new part
@app.route('/add_part', methods=['GET', 'POST'])
def add_part():
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            price = float(request.form['price'])
            image = request.files['image']

            # Handle file upload
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                # Create new part instance and save to database
                new_part = Part(name=name, description=description, price=price, image_filename=filename)
                db.session.add(new_part)
                db.session.commit()

                flash('Part added successfully!')
                return redirect(url_for('index'))
            else:
                flash('Invalid file type. Allowed types: jpg, jpeg, png, gif.')
        except Exception as e:
            flash(f'An error occurred: {str(e)}')

    return render_template('add_part.html')

# Function to check allowed file types
def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(e):
    db.session.rollback()  # Rollback the session in case of an error
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Start the Flask application
```

### HTML Templates

**index.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Automotive Parts</title>
</head>
<body>
    <h1>Automotive Parts</h1>
    <a href="{{ url_for('add_part') }}">Add New Part</a>
    <ul>
        {% for part in parts %}
            <li>
                <h2>{{ part.name }}</h2>
                <p>{{ part.description }}</p>
                <p>Price: ${{ part.price }}</p>
                <img src="{{ url_for('static', filename='uploads/' + part.image_filename) }}" alt="{{ part.name }}">
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_part.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add New Part</title>
</head>
<body>
    <h1>Add New Part</h1>
    <form method="POST" enctype="multipart/form-data">
        <label for="name">Part Name:</label>
        <input type="text" name="name" required><br>
        <label for="description">Description:</label>
        <textarea name="description" required></textarea><br>
        <label for="price">Price:</label>
        <input type="number" step="0.01" name="price" required><br>
        <label for="image">Image:</label>
        <input type="file" name="image" accept=".png,.jpg,.jpeg,.gif" required><br>
        <button type="submit">Add Part</button>
    </form>
</body>
</html>
```

**404.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

**500.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
</body>
</html>
```

### Note
- Ensure to create a folder named `uploads` in the same directory as your application to store the uploaded images.
- This code uses Flask and SQLAlchemy; make sure to install them via pip (`pip install Flask Flask-SQLAlchemy Flask-Migrate`).
- Update the secret key and database URI for your production environment.
