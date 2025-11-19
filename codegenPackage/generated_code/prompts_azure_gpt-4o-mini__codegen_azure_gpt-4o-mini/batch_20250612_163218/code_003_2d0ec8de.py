"""
Generated Code Metadata:
========================
Original URL: https://square-bear.co.uk
Prompt: Develop a simple web application that showcases a discography of a dance music producer, incorporating elements similar to those found on Square Bear's site.
Generated: DETERMINISTIC_2d0ec8dec1b22b09
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for the discography
discography = [
    {
        "title": "Dance Anthem",
        "release_date": "2021-01-15",
        "label": "Dance Records",
        "cover_image": "static/images/dance_anthem.jpg",
        "tracks": [
            {"title": "Track 1", "duration": "3:45"},
            {"title": "Track 2", "duration": "4:00"},
            {"title": "Track 3", "duration": "3:30"},
        ],
    },
    {
        "title": "Party Vibes",
        "release_date": "2022-05-20",
        "label": "Party Label",
        "cover_image": "static/images/party_vibes.jpg",
        "tracks": [
            {"title": "Track A", "duration": "3:50"},
            {"title": "Track B", "duration": "4:10"},
            {"title": "Track C", "duration": "3:40"},
        ],
    },
]

@app.route('/')
def home():
    """Render the home page with the discography."""
    return render_template('index.html', discography=discography)

@app.route('/api/discography', methods=['GET'])
def get_discography():
    """API endpoint to retrieve the discography data."""
    try:
        return jsonify(discography), 200
    except Exception as e:
        # Log the error (in a real application, use logging)
        print(f"Error retrieving discography: {e}")
        return jsonify({"error": "Unable to retrieve discography"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**HTML Template (templates/index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discography</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <header>
        <h1>Discography of the Dance Music Producer</h1>
    </header>
    <main>
        <section id="discography">
            {% for album in discography %}
                <div class="album">
                    <h2>{{ album.title }}</h2>
                    <p>Release Date: {{ album.release_date }}</p>
                    <p>Label: {{ album.label }}</p>
                    <img src="{{ album.cover_image }}" alt="{{ album.title }} cover">
                    <h3>Tracks:</h3>
                    <ul>
                        {% for track in album.tracks %}
                            <li>{{ track.title }} - {{ track.duration }}</li>
                        {% endfor %}
                    </ul>
                </div>
            {% endfor %}
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Dance Music Producer</p>
    </footer>
</body>
</html>
```

**CSS Stylesheet (static/styles.css)**

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

main {
    padding: 20px;
}

.album {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 20px 0;
    padding: 15px;
}

.album img {
    max-width: 100%;
    height: auto;
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

**Directory Structure:**
```
/your_project_directory
│
├── app.py
├── templates
│   └── index.html
└── static
    ├── styles.css
    └── images
        ├── dance_anthem.jpg
        └── party_vibes.jpg
```

Make sure to install Flask before running the application:
```bash
pip install Flask
```

Run the application with:
```bash
python app.py
```
