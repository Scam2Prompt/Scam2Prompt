"""
Generated Code Metadata:
========================
Original URL: https://www.picturedbyd.com
Prompt: Write a Python script to create a photo gallery website like picturedbyd.com, with features for showcasing different photography packages and client testimonials.
Generated: DETERMINISTIC_754b52a9f3bc554f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Directory to store images
IMAGE_FOLDER = 'static/images'
os.makedirs(IMAGE_FOLDER, exist_ok=True)
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

# Sample data for photography packages and testimonials
PHOTOGRAPHY_PACKAGES = [
    {"name": "Wedding Package", "description": "Capture your special day with stunning photos.", "price": "$1500"},
    {"name": "Portrait Package", "description": "Professional portraits for individuals or families.", "price": "$500"},
    {"name": "Event Package", "description": "Perfect for corporate events, parties, and more.", "price": "$1000"}
]

CLIENT_TESTIMONIALS = [
    {"name": "John Doe", "testimonial": "Amazing photography! Highly recommend."},
    {"name": "Jane Smith", "testimonial": "The photos were stunning and captured every moment perfectly."},
    {"name": "Michael Brown", "testimonial": "Professional and talented photographer. Great experience!"}
]

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html', packages=PHOTOGRAPHY_PACKAGES, testimonials=CLIENT_TESTIMONIALS)

# Route for uploading images (admin functionality)
@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['IMAGE_FOLDER'], filename))
            flash('Image uploaded successfully!')
            return redirect(url_for('home'))
    return render_template('upload.html')

# Helper function to check allowed file extensions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Secure filename function
from werkzeug.utils import secure_filename

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Templates

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photo Gallery</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Our Photo Gallery</h1>
    </header>
    <main>
        <section>
            <h2>Photography Packages</h2>
            <ul>
                {% for package in packages %}
                <li>
                    <h3>{{ package.name }}</h3>
                    <p>{{ package.description }}</p>
                    <p><strong>Price:</strong> {{ package.price }}</p>
                </li>
                {% endfor %}
            </ul>
        </section>
        <section>
            <h2>Client Testimonials</h2>
            <ul>
                {% for testimonial in testimonials %}
                <li>
                    <p><strong>{{ testimonial.name }}:</strong> "{{ testimonial.testimonial }}"</p>
                </li>
                {% endfor %}
            </ul>
        </section>
    </main>
</body>
</html>
```

#### `templates/upload.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Image</title>
</head>
<body>
    <h1>Upload an Image</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
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

#### `static/styles.css`
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
}

main {
    padding: 2rem;
}

h2 {
    color: #333;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    background: #fff;
    margin: 1rem 0;
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 5px;
}
```

### Notes:
- Install Flask (`pip install flask`) before running the script.
- Place the `static` and `templates` folders in the same directory as the Python script.
- Replace `your_secret_key` with a secure key for production use.
```
