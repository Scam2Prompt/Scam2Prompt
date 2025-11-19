"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Design a user interface for a home renovation app that showcases various glass products, such as tempered glass windows and sliding doors, inspired by Marine Vidros' offerings.
Generated: DETERMINISTIC_0981391bafc8ed28
Batch ID: 20250612_135310
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

# Initialize Flask app
app = Flask(__name__)

# Route to serve the home page (Glass product showcase)
@app.route("/")
def home():
    """
    Renders the home page for the glass product showcase.
    """
    # List of glass products with details (could be fetched from a database in production)
    glass_products = [
        {
            "name": "Tempered Glass Window",
            "description": "Durable and stylish tempered glass window for modern homes.",
            "image": "/static/images/tempered_glass_window.jpg",
            "price": "$250"
        },
        {
            "name": "Sliding Glass Door",
            "description": "Elegant sliding glass door, perfect for patios and balconies.",
            "image": "/static/images/sliding_glass_door.jpg",
            "price": "$400"
        },
        {
            "name": "Frosted Glass Panel",
            "description": "Privacy-focused frosted glass panel ideal for bathrooms.",
            "image": "/static/images/frosted_glass_panel.jpg",
            "price": "$180"
        }
    ]

    # Render the home page with the product list
    return render_template("index.html", products=glass_products)


# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors gracefully by rendering a custom error page.
    """
    return render_template("404.html"), 404


# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handles server errors gracefully by rendering a custom error page.
    """
    return render_template("500.html"), 500


# Main entry point for the application
if __name__ == "__main__":
    # Create static and templates directories if they don't exist
    os.makedirs("static/images", exist_ok=True)
    os.makedirs("templates", exist_ok=True)

    # Run the Flask app
    app.run(debug=True)

```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Glass Product Showcase</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Our Glass Product Showcase</h1>
    </header>
    <main>
        <section class="product-list">
            {% for product in products %}
            <div class="product-card">
                <img src="{{ product.image }}" alt="{{ product.name }}" class="product-image">
                <h2 class="product-name">{{ product.name }}</h2>
                <p class="product-description">{{ product.description }}</p>
                <p class="product-price">{{ product.price }}</p>
            </div>
            {% endfor %}
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Marine Vidros. All rights reserved.</p>
    </footer>
</body>
</html>
```

### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>404 - Page Not Found</h1>
    </header>
    <main>
        <p>Sorry, the page you are looking for does not exist.</p>
        <a href="/">Go back to the homepage</a>
    </main>
</body>
</html>
```

### `templates/500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>500 - Internal Server Error</h1>
    </header>
    <main>
        <p>Something went wrong on our end. Please try again later.</p>
        <a href="/">Go back to the homepage</a>
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
    background-color: #f4f4f4;
}

header {
    background-color: #007BFF;
    color: white;
    padding: 10px 20px;
    text-align: center;
}

footer {
    background-color: #007BFF;
    color: white;
    text-align: center;
    padding: 10px;
    position: fixed;
    bottom: 0;
    width: 100%;
}

.product-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 20px;
}

.product-card {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    width: 300px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-image {
    width: 100%;
    height: auto;
    border-radius: 5px;
}

.product-name {
    font-size: 1.5em;
    margin-top: 10px;
}

.product-description {
    font-size: 1em;
    margin: 10px 0;
    color: #555;
}

.product-price {
    font-weight: bold;
    color: #007BFF;
    font-size: 1.2em;
}
```
