"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzostudio.com
Prompt: Generate a code snippet for a web application that displays architectural projects similar to those featured on RENZO Studio de Arquitetura's website.
Generated: DETERMINISTIC_1eed0cecd92d68ea
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code snippet in Python using the Flask framework for the backend. It assumes you have basic knowledge of Flask and web development.

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data representing architectural projects
projects = [
    {
        "id": 1,
        "title": "Modern Villa",
        "image_url": "/static/images/modern_villa.jpg",
        "description": "A luxurious modern villa with sustainable design.",
        "location": "California, USA"
    },
    {
        "id": 2,
        "title": "Urban Office Space",
        "image_url": "/static/images/urban_office.jpg",
        "description": "A sleek office space located in the heart of the city.",
        "location": "New York, USA"
    },
    {
        "id": 3,
        "title": "Beachfront Residence",
        "image_url": "/static/images/beachfront_residence.jpg",
        "description": "A stunning beachfront property with panoramic views.",
        "location": "Miami, USA"
    }
]

@app.route('/')
def homepage():
    """
    Render the homepage that displays architectural projects.
    """
    return render_template("index.html", projects=projects)

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    API endpoint to fetch all projects in JSON format.
    """
    try:
        return jsonify(projects), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch projects", "message": str(e)}), 500

# Error handler for 404 page not found
@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors with a custom message.
    """
    return render_template("404.html"), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

```

### `index.html` (Frontend Template - Save in `templates/index.html`):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architectural Projects</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>Architectural Projects</h1>
    <div class="projects-container">
        {% for project in projects %}
        <div class="project-card">
            <img src="{{ project.image_url }}" alt="{{ project.title }}">
            <h2>{{ project.title }}</h2>
            <p>{{ project.description }}</p>
            <p><strong>Location:</strong> {{ project.location }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

### Example CSS (`styles.css` - Save in `static/styles.css`):
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

h1 {
    text-align: center;
    margin-top: 20px;
}

.projects-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    padding: 20px;
}

.project-card {
    background: white;
    width: 300px;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    text-align: center;
    padding: 15px;
}

.project-card img {
    width: 100%;
    height: auto;
    border-bottom: 1px solid #ddd;
}

.project-card h2 {
    margin: 10px 0;
    font-size: 1.5em;
}

.project-card p {
    margin: 5px 0;
    color: #333;
}
```

Ensure you have Flask installed (`pip install flask`) and the necessary static files (`images` and `styles.css`) properly set up in the designated directories (`static/` for assets, `templates/` for HTML).
