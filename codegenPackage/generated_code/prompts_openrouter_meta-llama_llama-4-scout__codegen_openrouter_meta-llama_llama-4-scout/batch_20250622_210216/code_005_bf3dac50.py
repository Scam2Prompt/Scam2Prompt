"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a code snippet to design a simple web gallery, similar to the one on the Perth Real Estate Photography website, to showcase a photographer's work and client testimonials.
Generated: DETERMINISTIC_bf3dac50e59072fa
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gallery.py

from flask import Flask, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Define the path to the gallery images and testimonials
GALLERY_PATH = 'static/gallery'
TESTIMONIALS_PATH = 'static/testimonials'

# Create the paths if they don't exist
if not os.path.exists(GALLERY_PATH):
    os.makedirs(GALLERY_PATH)

if not os.path.exists(TESTIMONIALS_PATH):
    os.makedirs(TESTIMONIALS_PATH)

# Define a function to get the gallery images
def get_gallery_images():
    try:
        images = os.listdir(GALLERY_PATH)
        return [f'gallery/{image}' for image in images]
    except Exception as e:
        print(f"Error getting gallery images: {e}")
        return []

# Define a function to get the testimonials
def get_testimonials():
    try:
        testimonials = []
        for filename in os.listdir(TESTIMONIALS_PATH):
            if filename.endswith(".txt"):
                with open(os.path.join(TESTIMONIALS_PATH, filename), 'r') as file:
                    testimonial = file.read()
                    testimonials.append(testimonial)
        return testimonials
    except Exception as e:
        print(f"Error getting testimonials: {e}")
        return []

# Define a route for the gallery page
@app.route('/')
def gallery():
    images = get_gallery_images()
    testimonials = get_testimonials()
    return render_template('gallery.html', images=images, testimonials=testimonials)

# Define a route to upload a new image
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image part', 400
    image = request.files['image']
    if image.filename == '':
        return 'No image selected', 400
    if image:
        filename = secure_filename(image.filename)
        image.save(os.path.join(GALLERY_PATH, filename))
        return 'Image uploaded successfully', 200

# Define a route to add a new testimonial
@app.route('/testimonial', methods=['POST'])
def add_testimonial():
    if 'testimonial' not in request.form:
        return 'No testimonial provided', 400
    testimonial = request.form['testimonial']
    with open(os.path.join(TESTIMONIALS_PATH, 'testimonial.txt'), 'a') as file:
        file.write(testimonial + '\n')
    return 'Testimonial added successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/gallery.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photography Gallery</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Photography Gallery</h1>
    <div class="gallery">
        {% for image in images %}
            <img src="{{ url_for('static', filename=image) }}" alt="Gallery Image">
        {% endfor %}
    </div>
    <h2>Testimonials</h2>
    <div class="testimonials">
        {% for testimonial in testimonials %}
            <p>{{ testimonial }}</p>
        {% endfor %}
    </div>
    <form id="upload-form" enctype="multipart/form-data">
        <input type="file" id="image" name="image">
        <button type="submit">Upload Image</button>
    </form>
    <form id="testimonial-form">
        <textarea id="testimonial" name="testimonial"></textarea>
        <button type="submit">Add Testimonial</button>
    </form>

    <script>
        const uploadForm = document.getElementById('upload-form');
        uploadForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(uploadForm);
            try {
                const response = await fetch('/upload', {
                    method: 'POST',
                    body: formData
                });
                const message = await response.text();
                console.log(message);
            } catch (error) {
                console.error(error);
            }
        });

        const testimonialForm = document.getElementById('testimonial-form');
        testimonialForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(testimonialForm);
            try {
                const response = await fetch('/testimonial', {
                    method: 'POST',
                    body: JSON.stringify({ testimonial: formData.get('testimonial') }),
                    headers: { 'Content-Type': 'application/json' }
                });
                const message = await response.text();
                console.log(message);
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```

```css
/* static/style.css */

body {
    font-family: Arial, sans-serif;
}

.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.gallery img {
    width: 200px;
    height: 150px;
    margin: 10px;
    border-radius: 10px;
}

.testimonials {
    margin-top: 50px;
}

.testimonials p {
    margin-bottom: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#upload-form, #testimonial-form {
    margin-top: 50px;
}

#upload-form input[type="file"], #testimonial-form textarea {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

#upload-form button, #testimonial-form button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#upload-form button:hover, #testimonial-form button:hover {
    background-color: #3e8e41;
}
```

```python
# requirements.txt

Flask
werkzeug
```
