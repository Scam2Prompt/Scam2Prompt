"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Write code to create a searchable gallery feature for an educational institution's website, similar to the "Galería" section on the IEBCA website.
Generated: DETERMINISTIC_9b3253baebe7ee55
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, request, jsonify
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration for gallery assets
GALLERY_FOLDER = 'static/gallery'  # Folder containing gallery images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed image file extensions

# Helper function to check allowed file extensions
def allowed_file(filename):
    """Checks if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Helper function to load gallery items
def load_gallery_items():
    """
    Loads gallery items from the GALLERY_FOLDER.
    Each item has a filename and a name derived from the filename.
    """
    items = []
    for filename in os.listdir(GALLERY_FOLDER):
        if allowed_file(filename):
            items.append({
                'filename': filename,
                'name': os.path.splitext(filename)[0]  # Use filename without extension as the name
            })
    return items

# Route to render the gallery page
@app.route('/')
def gallery():
    """
    Renders the gallery page with all items loaded from the GALLERY_FOLDER.
    """
    gallery_items = load_gallery_items()
    return render_template('gallery.html', gallery_items=gallery_items)

# Route to handle gallery search functionality
@app.route('/search', methods=['GET'])
def search_gallery():
    """
    Handles searching the gallery items based on query parameter 'q'.
    Returns JSON response with matching items.
    """
    query = request.args.get('q', '').lower()  # Get the search query and convert to lowercase
    if not query:
        return jsonify({'error': 'Query parameter "q" is required.'}), 400

    # Filter items based on query
    gallery_items = load_gallery_items()
    matching_items = [
        item for item in gallery_items if query in item['name'].lower()
    ]

    return jsonify({'results': matching_items})

# Flask error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 page."""
    return render_template('404.html'), 404

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template: gallery.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gallery</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>Gallery</h1>
    <input type="text" id="search" placeholder="Search gallery..." oninput="searchGallery()">
    <div id="gallery">
        <!-- Render gallery items dynamically -->
        {% for item in gallery_items %}
        <div class="gallery-item">
            <img src="{{ url_for('static', filename='gallery/' + item.filename) }}" alt="{{ item.name }}">
            <p>{{ item.name }}</p>
        </div>
        {% endfor %}
    </div>
    <script>
        async function searchGallery() {
            const query = document.getElementById('search').value;
            const response = await fetch(`/search?q=${query}`);
            const data = await response.json();
            const gallery = document.getElementById('gallery');
            gallery.innerHTML = ''; // Clear current gallery items

            // Display matching results
            if (data.results) {
                data.results.forEach(item => {
                    const div = document.createElement('div');
                    div.className = 'gallery-item';
                    div.innerHTML = `
                        <img src="/static/gallery/${item.filename}" alt="${item.name}">
                        <p>${item.name}</p>
                    `;
                    gallery.appendChild(div);
                });
            }
        }
    </script>
</body>
</html>
```

**CSS Stylesheet: styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

h1 {
    text-align: center;
    margin-top: 20px;
}

#search {
    display: block;
    margin: 20px auto;
    width: 50%;
    padding: 10px;
    font-size: 16px;
}

#gallery {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin: 20px;
}

.gallery-item {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: center;
    width: 200px;
}

.gallery-item img {
    max-width: 100%;
    height: auto;
}
```

**Folder Structure:**
```
project/
│
├── static/
│   ├── gallery/
│   │   ├── image1.jpg
│   │   ├── image2.png
│   │   └── ...
│   └── styles.css
│
├── templates/
│   ├── gallery.html
│   └── 404.html
│
├── app.py
```
