"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trykart.in
Prompt: Generate HTML and CSS code to design a product listing page with sections like "Fresh Fruits & Vegetables," "Edible Oils," and "Biscuits & Cookies," inspired by the Trykart website layout.
Generated: DETERMINISTIC_c841cff17077016a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Listing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Product Listing</h1>
        <nav>
            <ul>
                <li><a href="#fruits-vegetables">Fresh Fruits & Vegetables</a></li>
                <li><a href="#edible-oils">Edible Oils</a></li>
                <li><a href="#biscuits-cookies">Biscuits & Cookies</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="fruits-vegetables">
            <h2>Fresh Fruits & Vegetables</h2>
            <div class="product-list">
                <div class="product-card">
                    <img src="apple.jpg" alt="Apple">
                    <h3>Apple</h3>
                    <p>$1.00 each</p>
                    <button>Add to Cart</button>
                </div>
                <div class="product-card">
                    <img src="banana.jpg" alt="Banana">
                    <h3>Banana</h3>
                    <p>$0.50 each</p>
                    <button>Add to Cart</button>
                </div>
                <!-- More products can be added here -->
            </div>
        </section>

        <section id="edible-oils">
            <h2>Edible Oils</h2>
            <div class="product-list">
                <div class="product-card">
                    <img src="olive-oil.jpg" alt="Olive Oil">
                    <h3>Olive Oil</h3>
                    <p>$10.00 per liter</p>
                    <button>Add to Cart</button>
                </div>
                <div class="product-card">
                    <img src="sunflower-oil.jpg" alt="Sunflower Oil">
                    <h3>Sunflower Oil</h3>
                    <p>$8.00 per liter</p>
                    <button>Add to Cart</button>
                </div>
                <!-- More products can be added here -->
            </div>
        </section>

        <section id="biscuits-cookies">
            <h2>Biscuits & Cookies</h2>
            <div class="product-list">
                <div class="product-card">
                    <img src="chocolate-cookie.jpg" alt="Chocolate Cookie">
                    <h3>Chocolate Cookie</h3>
                    <p>$2.50 per pack</p>
                    <button>Add to Cart</button>
                </div>
                <div class="product-card">
                    <img src="oatmeal-cookie.jpg" alt="Oatmeal Cookie">
                    <h3>Oatmeal Cookie</h3>
                    <p>$2.00 per pack</p>
                    <button>Add to Cart</button>
                </div>
                <!-- More products can be added here -->
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Product Listing. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Resetting some default styles */
body, h1, h2, h3, p {
    margin: 0;
    padding: 0;
}

/* Styling the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f8f8f8;
}

/* Header styles */
header {
    background-color: #4CAF50;
    color: white;
    padding: 10px 0;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style-type: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 30px;
    background-color: #fff;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Product list styles */
.product-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

/* Product card styles */
.product-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    width: calc(33% - 10px);
    margin-bottom: 15px;
    padding: 10px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.product-card img {
    max-width: 100%;
    height: auto;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background-color: #4CAF50;
    color: white;
}
```
