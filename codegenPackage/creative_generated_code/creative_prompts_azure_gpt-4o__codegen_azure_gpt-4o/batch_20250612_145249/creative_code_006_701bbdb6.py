"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Develop a web application to showcase a gallery of completed restoration projects, allowing users to filter by service type (e.g., tuckpointing, repointing, lintel replacement) as highlighted on Premier Pointing's website.
Generated: DETERMINISTIC_701bbdb61c4a20e2
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Necessary imports for a basic Flask web application
from flask import Flask, render_template, request, jsonify
import os

# Initialize Flask application
app = Flask(__name__)

# Dummy data representing completed restoration projects
# Each project has a name, description, image, and service type
projects = [
    {
        "id": 1,
        "name": "Historic Building Restoration",
        "description": "Restoration of a historic building's brickwork.",
        "image_url": "/static/images/project1.jpg",
        "service_type": "tuckpointing"
    },
    {
        "id": 2,
        "name": "Repointing Cottage Bricks",
        "description": "Repointing services for a countryside cottage.",
        "image_url": "/static/images/project2.jpg",
        "service_type": "repointing"
    },
    {
        "id": 3,
        "name": "Lintel Replacement for Commercial Property",
        "description": "Replaced lintels for a large commercial property.",
        "image_url": "/static/images/project3.jpg",
        "service_type": "lintel replacement"
    },
    {
        "id": 4,
        "name": "Residential Tuckpointing",
        "description": "Tuckpointing for a residential property.",
        "image_url": "/static/images/project4.jpg",
        "service_type": "tuckpointing"
    }
]

# Route for the home page
@app.route('/')
def home():
    """
    Home route to render the gallery page.
    """
    return render_template('index.html', projects=projects)

# API route to filter projects by service type
@app.route('/api/filter', methods=['GET'])
def filter_projects():
    """
    API endpoint to filter projects based on service type.
    Accepts 'service_type' as a query parameter.
    """
    service_type = request.args.get('service_type')
    
    if not service_type:
        # Handle case where no filter is applied; return all projects
        return jsonify(projects)
    
    try:
        # Filter the projects based on the requested service type
        filtered_projects = [project for project in projects if project['service_type'] == service_type]
        return jsonify(filtered_projects)
    except Exception as e:
        # Return error response if something goes wrong
        return jsonify({"error": "An error occurred while filtering projects.", "details": str(e)}), 500

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page.
    """
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom 500 error page.
    """
    return render_template('500.html'), 500

# Main entry point to run the application
if __name__ == '__main__':
    # Set debug to False for production environments
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restoration Projects Gallery</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Restoration Projects Gallery</h1>
    </header>
    <main>
        <section id="filters">
            <label for="service-type">Filter by Service Type:</label>
            <select id="service-type" onchange="filterGallery()">
                <option value="">All</option>
                <option value="tuckpointing">Tuckpointing</option>
                <option value="repointing">Repointing</option>
                <option value="lintel replacement">Lintel Replacement</option>
            </select>
        </section>

        <section id="gallery">
            <!-- Projects will be dynamically populated here -->
        </section>
    </main>
    <script>
        // JavaScript function to dynamically update the gallery based on selected filter
        async function filterGallery() {
            const serviceType = document.getElementById('service-type').value;
            const gallery = document.getElementById('gallery');
            gallery.innerHTML = 'Loading...'; // Show loading state

            try {
                // Make API call to fetch filtered projects
                const response = await fetch(`/api/filter?service_type=${serviceType}`);
                const projects = await response.json();

                // Populate gallery with filtered results
                gallery.innerHTML = '';
                projects.forEach(project => {
                    const projectCard = `
                        <div class="project-card">
                            <img src="${project.image_url}" alt="${project.name}">
                            <h3>${project.name}</h3>
                            <p>${project.description}</p>
                        </div>
                    `;
                    gallery.innerHTML += projectCard;
                });
            } catch (error) {
                gallery.innerHTML = 'An error occurred while loading projects.';
            }
        }

        // Initial load of all projects
        filterGallery();
    </script>
</body>
</html>
```

### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```

### `templates/500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Oops! Something went wrong on our end. Please try again later.</p>
</body>
</html>
```

### `static/styles.css`
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background-color: #007BFF;
    color: white;
    padding: 1rem 0;
    text-align: center;
}

#filters {
    text-align: center;
    margin: 1rem 0;
}

#gallery {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    padding: 1rem;
}

.project-card {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 1rem;
    width: calc(33% - 2rem);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.project-card img {
    max-width: 100%;
    border-radius: 5px;
}

.project-card h3 {
    margin: 0.5rem 0;
}
```
