"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: Write a Python script to create a webpage showcasing the amenities of Dens Haven villas, including features like a swimming pool, clubhouse, landscaped garden, and CCTV monitoring system.
Generated: DETERMINISTIC_af39486e0fd1bb50
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template

app = Flask(__name__)

# Sample data for the amenities of Dens Haven villas
amenities = [
    {
        "name": "Swimming Pool",
        "description": "A large, beautifully designed swimming pool for relaxation and recreation.",
        "image": "static/images/swimming_pool.jpg"
    },
    {
        "name": "Clubhouse",
        "description": "A spacious clubhouse for gatherings, events, and community activities.",
        "image": "static/images/clubhouse.jpg"
    },
    {
        "name": "Landscaped Garden",
        "description": "A lush, landscaped garden providing a serene environment for residents.",
        "image": "static/images/garden.jpg"
    },
    {
        "name": "CCTV Monitoring System",
        "description": "24/7 CCTV surveillance ensuring the safety and security of all residents.",
        "image": "static/images/cctv.jpg"
    }
]

@app.route('/')
def home():
    """
    Render the homepage showcasing the amenities of Dens Haven villas.
    """
    return render_template('index.html', amenities=amenities)

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(debug=True)
    except Exception as e:
        # Log the error and exit gracefully
        print(f"An error occurred: {e}")
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dens Haven Villas Amenities</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Dens Haven Villas</h1>
        <h2>Our Amenities</h2>
    </header>
    <main>
        <section>
            {% for amenity in amenities %}
                <div class="amenity">
                    <h3>{{ amenity.name }}</h3>
                    <img src="{{ amenity.image }}" alt="{{ amenity.name }}">
                    <p>{{ amenity.description }}</p>
                </div>
            {% endfor %}
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Dens Haven Villas. All rights reserved.</p>
    </footer>
</body>
</html>
```

**CSS (static/styles.css)**

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

h1, h2 {
    margin: 0;
}

main {
    padding: 20px;
}

.amenity {
    background: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 5px;
    margin: 20px 0;
    padding: 15px;
    text-align: center;
}

.amenity img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

**Directory Structure:**
```
/project-directory
    /static
        /images
            swimming_pool.jpg
            clubhouse.jpg
            garden.jpg
            cctv.jpg
        styles.css
    app.py
    templates
        index.html
```

Make sure to install Flask using `pip install Flask` and place the images in the specified directory for the code to run correctly.
