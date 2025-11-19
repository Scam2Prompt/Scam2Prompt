"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Generate a code snippet for a web application that showcases the unique features of Fortic's concrete beams that imitate wood, focusing on their design and durability.
Generated: DETERMINISTIC_8b97594656281756
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask web application to showcase Fortic's concrete beams that imitate wood

from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Data for Fortic's concrete beams (normally this would come from a database)
beams_data = [
    {
        "id": 1,
        "name": "Rustic Oak Beam",
        "design": "Imitates classic oak wood texture with detailed grain pattern.",
        "durability": "Resistant to moisture, pests, and wear for over 50 years.",
        "image_url": "/static/images/rustic_oak.jpg"
    },
    {
        "id": 2,
        "name": "Walnut Stripped Beam",
        "design": "Mimics walnut wood with a stripped texture for a modern look.",
        "durability": "Exceptional strength and eco-friendly composition.",
        "image_url": "/static/images/walnut_stripped.jpg"
    },
    {
        "id": 3,
        "name": "Maple Smooth Beam",
        "design": "Smooth maple wood appearance, ideal for interior design.",
        "durability": "Highly durable and easy to maintain.",
        "image_url": "/static/images/maple_smooth.jpg"
    }
]

@app.route("/")
def home():
    """
    Home route that renders the homepage with a list of beams.
    """
    return render_template("home.html", beams=beams_data)

@app.route("/beam/<int:beam_id>")
def beam_details(beam_id):
    """
    Route to display details of a specific beam based on its ID.

    :param beam_id: ID of the beam to display details for.
    :return: Rendered HTML page or JSON error if beam not found.
    """
    beam = next((beam for beam in beams_data if beam["id"] == beam_id), None)
    if not beam:
        return jsonify({"error": "Beam not found"}), 404
    return render_template("beam_details.html", beam=beam)

if __name__ == "__main__":
    # Run the application in debug mode (disable debug in production)
    app.run(debug=True)
```

### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fortic Concrete Beams</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Fortic Concrete Beams</h1>
        <p>Imitating wood with unmatched durability.</p>
    </header>
    <main>
        <h2>Our Beams</h2>
        <ul>
            {% for beam in beams %}
            <li>
                <a href="/beam/{{ beam.id }}">
                    <img src="{{ beam.image_url }}" alt="{{ beam.name }}">
                    <h3>{{ beam.name }}</h3>
                </a>
            </li>
            {% endfor %}
        </ul>
    </main>
    <footer>
        <p>&copy; 2023 Fortic Concrete Beams</p>
    </footer>
</body>
</html>
```

### `templates/beam_details.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ beam.name }} - Fortic Concrete Beams</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>{{ beam.name }}</h1>
    </header>
    <main>
        <img src="{{ beam.image_url }}" alt="{{ beam.name }}">
        <p><strong>Design:</strong> {{ beam.design }}</p>
        <p><strong>Durability:</strong> {{ beam.durability }}</p>
        <a href="/">Back to Home</a>
    </main>
    <footer>
        <p>&copy; 2023 Fortic Concrete Beams</p>
    </footer>
</body>
</html>
```

### `static/styles.css`
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: white;
    padding: 1rem;
    text-align: center;
}

main {
    padding: 1rem;
}

ul {
    list-style: none;
    padding: 0;
}

ul li {
    margin: 1rem 0;
}

ul li a {
    text-decoration: none;
    color: #000;
}

footer {
    text-align: center;
    padding: 1rem;
    background-color: #333;
    color: white;
}
```

### Notes:
1. Place static assets (images and CSS) in the `static` folder.
2. Ensure you have Flask installed: `pip install flask`.
3. This code is ready for deployment in a production environment once debug mode is turned off (`debug=False`).
