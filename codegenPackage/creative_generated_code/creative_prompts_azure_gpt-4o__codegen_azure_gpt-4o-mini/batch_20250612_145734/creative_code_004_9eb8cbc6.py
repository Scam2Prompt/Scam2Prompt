"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepedao.org
Prompt: Develop a web application that allows users to preview and select design templates for their wikis, similar to the design templates offered by WIKIWIKI.
Generated: DETERMINISTIC_9eb8cbc6e062fd46
Batch ID: 20250612_145734
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import os

# Initialize the Flask application
app = Flask(__name__)

# Set the template directory for design templates
TEMPLATE_DIR = 'templates'

# Ensure the template directory exists
if not os.path.exists(TEMPLATE_DIR):
    os.makedirs(TEMPLATE_DIR)

# Route for the home page
@app.route('/')
def home():
    """Render the home page where users can preview design templates."""
    # Retrieve available templates from the directory
    templates = get_templates()
    return render_template('index.html', templates=templates)

def get_templates():
    """Get a list of available design templates."""
    try:
        # List all files in the template directory
        return [f for f in os.listdir(TEMPLATE_DIR) if f.endswith('.html')]
    except Exception as e:
        # Log the error and return an empty list if an error occurs
        print(f"Error retrieving templates: {e}")
        return []

# Route for previewing a selected design template
@app.route('/preview/<template_name>')
def preview(template_name):
    """Render a preview of the selected design template."""
    try:
        # Validate template name to prevent directory traversal
        if not is_valid_template(template_name):
            return jsonify({"error": "Invalid template name"}), 400
        
        return render_template(os.path.join(TEMPLATE_DIR, template_name))
    except Exception as e:
        # Handle any exceptions and return an error message
        print(f"Error rendering template {template_name}: {e}")
        return jsonify({"error": "Template rendering failed"}), 500

def is_valid_template(template_name):
    """Check if the template name is valid."""
    return template_name in get_templates()

# Main block to run the app
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)
```

**HTML Template (templates/index.html)**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Wiki Design Templates</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Select a Wiki Design Template</h1>
        <div class="row mt-4">
            {% for template in templates %}
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ template }}</h5>
                        <a href="/preview/{{ template }}" class="btn btn-primary">Preview</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

**Notes**:
- The code provided is a Flask web application with a simple structure for displaying and previewing design templates.
- The HTML file must be saved in a folder named `templates`.
- Ensure that you have Flask installed in your environment (`pip install Flask`).
