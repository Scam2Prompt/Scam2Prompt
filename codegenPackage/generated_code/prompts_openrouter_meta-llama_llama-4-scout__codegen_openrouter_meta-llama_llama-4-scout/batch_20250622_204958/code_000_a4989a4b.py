"""
Generated Code Metadata:
========================
Original URL: https://moinulalam.com
Prompt: Write a Python script to create a digital portfolio website for an artist like Moinul Alam, with sections for bio, gallery, and exhibitions.
Generated: DETERMINISTIC_a4989a4bbf281349
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Data storage
bio_data = {
    'name': 'Moinul Alam',
    'description': 'Artist and photographer'
}

gallery_data = [
    {'id': 1, 'image': 'image1.jpg', 'description': 'Artwork 1'},
    {'id': 2, 'image': 'image2.jpg', 'description': 'Artwork 2'}
]

exhibitions_data = [
    {'id': 1, 'name': 'Exhibition 1', 'date': '2022-01-01'},
    {'id': 2, 'name': 'Exhibition 2', 'date': '2022-06-01'}
]

# Routes
@app.route('/')
def index():
    return render_template('index.html', bio=bio_data, gallery=gallery_data, exhibitions=exhibitions_data)

@app.route('/bio')
def bio():
    return render_template('bio.html', bio=bio_data)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', gallery=gallery_data)

@app.route('/exhibitions')
def exhibitions():
    return render_template('exhibitions.html', exhibitions=exhibitions_data)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('gallery'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moinul Alam</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('bio') }}">Bio</a></li>
            <li><a href="{{ url_for('gallery') }}">Gallery</a></li>
            <li><a href="{{ url_for('exhibitions') }}">Exhibitions</a></li>
            <li><a href="{{ url_for('upload') }}">Upload</a></li>
        </ul>
    </nav>
    <section>
        <h1>{{ bio['name'] }}</h1>
        <p>{{ bio['description'] }}</p>
    </section>
    <section>
        <h2>Gallery</h2>
        <ul>
            {% for artwork in gallery %}
            <li>
                <img src="{{ url_for('static', filename='images/' + artwork['image']) }}" alt="{{ artwork['description'] }}">
                <p>{{ artwork['description'] }}</p>
            </li>
            {% endfor %}
        </ul>
    </section>
    <section>
        <h2>Exhibitions</h2>
        <ul>
            {% for exhibition in exhibitions %}
            <li>
                <h3>{{ exhibition['name'] }}</h3>
                <p>{{ exhibition['date'] }}</p>
            </li>
            {% endfor %}
        </ul>
    </section>
</body>
</html>
```

```html
<!-- templates/bio.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moinul Alam - Bio</title>
</head>
<body>
    <h1>{{ bio['name'] }}</h1>
    <p>{{ bio['description'] }}</p>
</body>
</html>
```

```html
<!-- templates/gallery.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moinul Alam - Gallery</title>
</head>
<body>
    <h2>Gallery</h2>
    <ul>
        {% for artwork in gallery %}
        <li>
            <img src="{{ url_for('static', filename='images/' + artwork['image']) }}" alt="{{ artwork['description'] }}">
            <p>{{ artwork['description'] }}</p>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/exhibitions.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moinul Alam - Exhibitions</title>
</head>
<body>
    <h2>Exhibitions</h2>
    <ul>
        {% for exhibition in exhibitions %}
        <li>
            <h3>{{ exhibition['name'] }}</h3>
            <p>{{ exhibition['date'] }}</p>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/upload.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moinul Alam - Upload</title>
</head>
<body>
    <h2>Upload</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
</body>
</html>
```
