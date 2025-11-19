"""
Generated Code Metadata:
========================
Original URL: https://wallmemes.com
Prompt: Design an e-commerce website homepage using HTML, CSS, and JavaScript that showcases various products with images, prices, and discounts, similar to wallmemes.com.
Generated: DETERMINISTIC_30b2d2b939bd5ac2
Batch ID: 20250622_211520
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
    <meta name="description" content="E-commerce homepage showcasing various products with images, prices, and discounts.">
    <title>E-Commerce Homepage</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1 class="logo">ShopEasy</h1>
            <nav class="nav">
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#products">Products</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Welcome to ShopEasy</h2>
            <p>Your one-stop shop for amazing deals and discounts!</p>
            <a href="#products" class="btn">Shop Now</a>
        </div>
    </section>

    <!-- Products Section -->
    <section id="products" class="products">
        <div class="container">
            <h2>Featured Products</h2>
            <div class="product-grid">
                <!-- Product Card -->
                <div class="product-card">
                    <img src="product1.jpg" alt="Product 1">
                    <h3>Product 1</h3>
                    <p class="price">$20 <span class="discount">$25</span></p>
                    <button class="btn add-to-cart">Add to Cart</button>
                </div>
                <!-- Product Card -->
                <div class="product-card">
                    <img src="product2.jpg" alt="Product 2">
                    <h3>Product 2</h3>
                    <p class="price">$15 <span class="discount">$18</span></p>
                    <button class="btn add-to-cart">Add to Cart</button>
                </div>
                <!-- Product Card -->
                <div class="product-card">
                    <img src="product3.jpg" alt="Product 3">
                    <h3>Product 3</h3>
                    <p class="price">$30 <span class="discount">$35</span></p>
                    <button class="btn add-to-cart">Add to Cart</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 ShopEasy. All rights reserved.</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a, img {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

/* Header Styling */
.header {
    background: #333;
    color: #fff;
    padding: 1rem 0;
}

.header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header .logo {
    font-size: 1.5rem;
    font-weight: bold;
}

.header .nav ul {
    list-style: none;
    display: flex;
    gap: 1rem;
}

.header .nav a {
    color: #fff;
    text-decoration: none;
}

/* Hero Section */
.hero {
    background: #f4f4f4;
    text-align: center;
    padding: 2rem 0;
}

.hero h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.hero .btn {
    background: #333;
    color: #fff;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 5px;
}

/* Products Section */
.products {
    padding: 2rem 0;
    background: #fff;
}

.products h2 {
    text-align: center;
    margin-bottom: 2rem;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}

.product-card {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 1rem;
    text-align: center;
    background: #f9f9f9;
}

.product-card img {
    max-width: 100%;
    height: auto;
    margin-bottom: 1rem;
}

.product-card .price {
    font-size: 1.2rem;
    color: #333;
}

.product-card .discount {
    text-decoration: line-through;
    color: #999;
    font-size: 0.9rem;
}

.product-card .btn {
    background: #333;
    color: #fff;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 5px;
    margin-top: 1rem;
}

/* Footer Section */
.footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}
```

```javascript
// script.js

// Add to Cart Button Event Listener
document.addEventListener('DOMContentLoaded', () => {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', () => {
            alert('Item added to cart!');
        });
    });
});
```
