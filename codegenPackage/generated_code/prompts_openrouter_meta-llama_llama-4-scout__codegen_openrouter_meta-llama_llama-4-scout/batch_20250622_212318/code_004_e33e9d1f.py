"""
Generated Code Metadata:
========================
Original URL: https://cafelc.com
Prompt: Develop a simple HTML and CSS template for a product page on an e-commerce website, inspired by the design of cafelc.com.
Generated: DETERMINISTIC_e33e9d1fef91aebf
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="product-hero">
            <img src="product-image.jpg" alt="Product Image">
        </section>
        <section class="product-info">
            <h1>Product Title</h1>
            <p class="product-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            <div class="product-price">
                <span>$19.99</span>
            </div>
            <button class="add-to-cart">Add to Cart</button>
            <div class="product-specifications">
                <h2>Specifications</h2>
                <ul>
                    <li><strong>Material:</strong> Stainless Steel</li>
                    <li><strong>Size:</strong> 10 oz</li>
                    <li><strong>Color:</strong> Black</li>
                </ul>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 E-commerce Website</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.product-hero {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

.product-hero img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.product-info {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product-description {
    margin-bottom: 20px;
}

.product-price {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}

.add-to-cart {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
}

.add-to-cart:hover {
    background-color: #444;
}

.product-specifications {
    margin-top: 20px;
}

.product-specifications ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.product-specifications li {
    margin-bottom: 10px;
}

.product-specifications strong {
    font-weight: bold;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
