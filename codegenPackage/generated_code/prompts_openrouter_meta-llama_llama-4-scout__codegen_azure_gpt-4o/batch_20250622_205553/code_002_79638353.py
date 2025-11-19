"""
Generated Code Metadata:
========================
Original URL: https://eveandevan.com
Prompt: Generate HTML and CSS code for a simple webpage showcasing men's clothing products, including shirts, pants, and jackets, with a similar layout to Evan Mens.
Generated: DETERMINISTIC_796383537adafb0b
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Men's clothing products including shirts, pants, and jackets.">
    <title>Men's Clothing Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1>Men's Clothing Showcase</h1>
            <nav class="nav">
                <ul>
                    <li><a href="#shirts">Shirts</a></li>
                    <li><a href="#pants">Pants</a></li>
                    <li><a href="#jackets">Jackets</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content Section -->
    <main class="main-content">
        <!-- Shirts Section -->
        <section id="shirts" class="product-section">
            <h2>Shirts</h2>
            <div class="product-grid">
                <div class="product-card">
                    <img src="shirt1.jpg" alt="Classic White Shirt">
                    <h3>Classic White Shirt</h3>
                    <p>$25.00</p>
                </div>
                <div class="product-card">
                    <img src="shirt2.jpg" alt="Blue Denim Shirt">
                    <h3>Blue Denim Shirt</h3>
                    <p>$30.00</p>
                </div>
            </div>
        </section>

        <!-- Pants Section -->
        <section id="pants" class="product-section">
            <h2>Pants</h2>
            <div class="product-grid">
                <div class="product-card">
                    <img src="pants1.jpg" alt="Black Formal Pants">
                    <h3>Black Formal Pants</h3>
                    <p>$40.00</p>
                </div>
                <div class="product-card">
                    <img src="pants2.jpg" alt="Casual Khaki Pants">
                    <h3>Casual Khaki Pants</h3>
                    <p>$35.00</p>
                </div>
            </div>
        </section>

        <!-- Jackets Section -->
        <section id="jackets" class="product-section">
            <h2>Jackets</h2>
            <div class="product-grid">
                <div class="product-card">
                    <img src="jacket1.jpg" alt="Leather Jacket">
                    <h3>Leather Jacket</h3>
                    <p>$75.00</p>
                </div>
                <div class="product-card">
                    <img src="jacket2.jpg" alt="Winter Coat">
                    <h3>Winter Coat</h3>
                    <p>$90.00</p>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 Men's Clothing Showcase. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
.header {
    background-color: #333;
    color: #fff;
    padding: 1rem 0;
}

.header h1 {
    text-align: center;
    margin-bottom: 0.5rem;
}

.nav ul {
    display: flex;
    justify-content: center;
    list-style: none;
}

.nav ul li {
    margin: 0 1rem;
}

.nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

.nav ul li a:hover {
    text-decoration: underline;
}

/* Main Content */
.main-content {
    padding: 2rem 0;
}

.product-section {
    margin-bottom: 2rem;
}

.product-section h2 {
    text-align: center;
    margin-bottom: 1rem;
    color: #333;
}

.product-grid {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.product-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    width: 300px;
    text-align: center;
    padding: 1rem;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-card img {
    max-width: 100%;
    border-radius: 5px;
}

.product-card h3 {
    margin: 0.5rem 0;
    color: #333;
}

.product-card p {
    color: #666;
    font-weight: bold;
}

/* Footer */
.footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}

.footer p {
    margin: 0;
}
```
