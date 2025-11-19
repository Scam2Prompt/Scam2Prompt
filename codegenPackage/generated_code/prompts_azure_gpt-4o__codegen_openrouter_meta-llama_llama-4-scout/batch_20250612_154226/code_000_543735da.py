"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: Write a Python script to create a portfolio webpage showcasing award-winning interior design projects, including sections for "Residential Design," "Commercial Spaces," and "Custom Furniture," as described by Meezan Interior Solutions.
Generated: DETERMINISTIC_543735da3cdca056
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# Create a Flask application instance
app = Flask(__name__)

# Define project data
projects = {
    "Residential Design": [
        {"name": "Modern Home", "image": "modern_home.jpg", "description": "A modern home design with sleek furniture and minimalist decor"},
        {"name": "Cozy Living Room", "image": "cozy_living_room.jpg", "description": "A cozy living room with warm lighting and comfortable seating"}
    ],
    "Commercial Spaces": [
        {"name": "Office Space", "image": "office_space.jpg", "description": "A modern office space with open layout and collaborative workstations"},
        {"name": "Restaurant Design", "image": "restaurant_design.jpg", "description": "A restaurant design with unique lighting fixtures and stylish decor"}
    ],
    "Custom Furniture": [
        {"name": "Handcrafted Chair", "image": "handcrafted_chair.jpg", "description": "A handcrafted chair with intricate details and comfortable seating"},
        {"name": "Customized Table", "image": "customized_table.jpg", "description": "A customized table with unique design and sturdy construction"}
    ]
}

# Define allowed file extensions for image uploads
ALLOWED_EXTENSIONS = set(["jpg", "jpeg", "png", "gif"])

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the homepage
@app.route("/")
def index():
    return render_template("index.html", projects=projects)

# Route for handling image uploads
@app.route("/upload", methods=["POST"])
def upload_image():
    if request.method == "POST":
        # Check if the post request has the file part
        if "file" not in request.files:
            return "No file part", 400
        file = request.files["file"]
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            return "No selected file", 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join("static", filename))
            return "File uploaded successfully", 200
        else:
            return "Invalid file type", 400

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

# Run the application if this script is executed
if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meezan Interior Solutions</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Meezan Interior Solutions</h1>
        <nav>
            <ul>
                <li><a href="#residential-design">Residential Design</a></li>
                <li><a href="#commercial-spaces">Commercial Spaces</a></li>
                <li><a href="#custom-furniture">Custom Furniture</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% for category, project_list in projects.items() %}
        <section id="{{ category.lower().replace(' ', '-') }}">
            <h2>{{ category }}</h2>
            <div class="project-grid">
                {% for project in project_list %}
                <div class="project">
                    <img src="{{ url_for('static', filename=project.image) }}" alt="{{ project.name }}">
                    <h3>{{ project.name }}</h3>
                    <p>{{ project.description }}</p>
                </div>
                {% endfor %}
            </div>
        </section>
        {% endfor %}
    </main>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload Image">
    </form>
</body>
</html>
```

**templates/404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

**templates/500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>Internal Server Error</h1>
    <p>An error occurred on the server.</p>
</body>
</html>
```

**static/style.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.project {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
}

.project img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

.project h3 {
    margin-top: 10px;
}

.project p {
    margin-bottom: 20px;
}
```
