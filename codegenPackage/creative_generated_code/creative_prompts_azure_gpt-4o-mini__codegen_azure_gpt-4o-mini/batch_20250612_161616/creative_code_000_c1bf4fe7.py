"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kamboz.com
Prompt: Generate a code snippet for an e-commerce website that displays a collection of superhero jackets, similar to the KAMBOZ online store.
Generated: DETERMINISTIC_c1bf4fe7665bc78c
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify
import os

# Initialize the Flask application
app = Flask(__name__)

# Sample data for superhero jackets (this would typically come from a database)
jackets = [
    {
        "id": 1,
        "name": "Batman Jacket",
        "price": 149.99,
        "image": "static/images/batman_jacket.jpg",
        "description": "A stylish jacket for the Dark Knight fan."
    },
    {
        "id": 2,
        "name": "Superman Jacket",
        "price": 129.99,
        "image": "static/images/superman_jacket.jpg",
        "description": "Fly high with this Superman-inspired jacket."
    },
    {
        "id": 3,
        "name": "Spider-Man Jacket",
        "price": 139.99,
        "image": "static/images/spiderman_jacket.jpg",
        "description": "Swing into action with this Spider-Man jacket."
    }
]

@app.route('/')
def home():
    """
    Render the home page displaying superhero jackets.
    """
    return render_template('index.html', jackets=jackets)

@app.route('/api/jackets', methods=['GET'])
def get_jackets():
    """
    API endpoint to retrieve jacket data.
    Returns a JSON response with the jackets data.
    """
    try:
        return jsonify(jackets), 200
    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(f"Error retrieving jackets: {str(e)}")
        return jsonify({"error": "Unable to fetch jackets"}), 500

if __name__ == '__main__':
    # Ensure the application runs in debug mode for development, disable for production
    app.run(debug=os.environ.get('FLASK_DEBUG', default=False))
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Superhero Jackets</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <header>
        <h1>Superhero Jackets Collection</h1>
    </header>
    <main>
        <div class="jacket-collection">
            {% for jacket in jackets %}
                <div class="jacket-item">
                    <img src="{{ jacket.image }}" alt="{{ jacket.name }}">
                    <h2>{{ jacket.name }}</h2>
                    <p>{{ jacket.description }}</p>
                    <p>Price: ${{ jacket.price }}</p>
                </div>
            {% endfor %}
        </div>
    </main>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

header {
    text-align: center;
    margin-bottom: 20px;
}

.jacket-collection {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}

.jacket-item {
    background: white;
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 10px;
    margin: 10px;
    width: 200px;
    text-align: center;
}

.jacket-item img {
    max-width: 100%;
    border-radius: 8px;
}
```
