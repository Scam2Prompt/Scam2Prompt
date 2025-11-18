"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alshehhi.net
Prompt: Create a web application template for showcasing completed projects, similar to the "اعمالنا" (Our Work) section on Alshehhi.Net.
Generated: DETERMINISTIC_208c12b3aef7c545
Batch ID: 20250612_151553
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/blogging": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/ecommerce": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/portfolio": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample project data to mimic database entries
projects = [
    {
        "id": 1,
        "title": "E-Commerce Platform",
        "description": "A fully functional e-commerce platform with secure payment integration.",
        "image_url": "/static/images/e_commerce.png",
        "url": "https://example.com/ecommerce"
    },
    {
        "id": 2,
        "title": "Portfolio Website",
        "description": "A sleek and modern portfolio website showcasing personal work.",
        "image_url": "/static/images/portfolio.png",
        "url": "https://example.com/portfolio"
    },
    {
        "id": 3,
        "title": "Blogging Platform",
        "description": "A dynamic content management system for blogging.",
        "image_url": "/static/images/blogging.png",
        "url": "https://example.com/blogging"
    }
]

@app.route('/')
def home():
    """
    Render the home page template with project data.
    """
    return render_template('home.html', projects=projects)

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    API endpoint to fetch project data in JSON format.
    """
    return jsonify(projects)

if __name__ == '__main__':
    # Run the development server
    app.run(debug=True)
```

### Directory Structure
```
project-showcase/
│
├── app.py                     # Main application code
│
├── templates/                 # HTML templates directory
│   └── home.html              # Template for the home page
│
├── static/                    # Static files directory
│   └── images/                # Images for project showcase
│       ├── e_commerce.png
│       ├── portfolio.png
│       └── blogging.png
│
└── requirements.txt           # Python dependencies file
```

### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Work</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Our Work</h1>
    </header>
    <main>
        <section class="projects">
            {% for project in projects %}
                <div class="project-card">
                    <img src="{{ project.image_url }}" alt="{{ project.title }}">
                    <h2>{{ project.title }}</h2>
                    <p>{{ project.description }}</p>
                    <a href="{{ project.url }}" target="_blank">View Project</a>
                </div>
            {% endfor %}
        </section>
    </main>
</body>
</html>
```

### `static/styles.css`
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f7f7f7;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
}

.projects {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    padding: 2rem;
    justify-content: center;
}

.project-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    width: 300px;
}

.project-card img {
    width: 100%;
    height: auto;
}

.project-card h2 {
    font-size: 1.5rem;
    margin: 1rem 0 0.5rem;
    padding: 0 1rem;
}

.project-card p {
    padding: 0 1rem;
    margin: 0 0 1rem;
}

.project-card a {
    display: block;
    text-align: center;
    background-color: #007bff;
    color: #fff;
    padding: 0.5rem;
    text-decoration: none;
    border-radius: 4px;
    margin: 1rem;
}

.project-card a:hover {
    background-color: #0056b3;
}
```

### `requirements.txt`
```
Flask==2.3.2
```
