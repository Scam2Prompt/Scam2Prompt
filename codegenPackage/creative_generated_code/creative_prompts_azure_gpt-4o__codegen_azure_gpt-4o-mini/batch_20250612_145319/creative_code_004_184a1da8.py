"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zirciulit.com
Prompt: Suggest tools or libraries for creating a portfolio website showcasing residential, commercial, and aviation interior design projects, similar to Zirciulit Design Firm's portfolio.
Generated: DETERMINISTIC_184a1da8d4e11970
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web framework and rendering
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing interior design projects
projects = {
    "residential": [
        {"title": "Modern Apartment", "description": "A sleek and modern apartment design.", "image": "residential_apartment.jpg"},
        {"title": "Cozy Cottage", "description": "A warm and inviting cottage design.", "image": "residential_cottage.jpg"}
    ],
    "commercial": [
        {"title": "Office Space", "description": "A professional and efficient office design.", "image": "commercial_office.jpg"},
        {"title": "Retail Store", "description": "An attractive and functional retail design.", "image": "commercial_store.jpg"}
    ],
    "aviation": [
        {"title": "Private Jet Interior", "description": "Luxurious design for private jet interiors.", "image": "aviation_private_jet.jpg"},
        {"title": "Airport Lounge", "description": "A comfortable and elegant airport lounge design.", "image": "aviation_lounge.jpg"}
    ]
}

@app.route('/')
def home():
    """Render the home page with project categories."""
    return render_template('home.html')

@app.route('/projects/<category>')
def projects_by_category(category):
    """Render the projects based on the selected category."""
    # Validate category input
    if category not in projects:
        return render_template('404.html'), 404  # Return a 404 page if category not found
    
    project_list = projects[category]
    return render_template('projects.html', projects=project_list, category=category)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors and render a custom error page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(debug=True)
    except Exception as e:
        # Log the error and exit gracefully
        print(f"Error starting the application: {e}")
```

### Directory Structure
```
/portfolio_website
    ├── app.py                  # Main Flask application file
    ├── templates               # HTML templates
    │   ├── home.html          # Home page template
    │   ├── projects.html       # Projects category template
    │   └── 404.html            # Custom 404 error page
    └── static                  # Static files (e.g., images, CSS, JS)
        ├── css
        ├── images
        └── js
```

### Notes:
- Create `templates/home.html`, `templates/projects.html`, and `templates/404.html` to render the respective pages.
- Place project images inside `static/images`.
- Modify `app.run(debug=True)` to `app.run()` in production.
