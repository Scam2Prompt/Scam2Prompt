"""
Generated Code Metadata:
========================
Original URL: https://ranchioffline.com
Prompt: Write a code snippet in HTML/CSS to create a responsive and user-friendly interface for an e-commerce website like RanchiOffline.
Generated: DETERMINISTIC_59389a3208f55ace
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RanchiOffline</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#" class="logo">RanchiOffline</a></li>
                <li><a href="#">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to RanchiOffline</h1>
        <p>Your one-stop shop for all your needs</p>
        <button>Explore Now</button>
    </section>

    <!-- Products Section -->
    <section class="products">
        <h2>Our Products</h2>
        <div class="product-grid">
            <div class="product-card">
                <img src="product1.jpg" alt="Product 1">
                <h3>Product 1</h3>
                <p>$19.99</p>
            </div>
            <div class="product-card">
                <img src="product2.jpg" alt="Product 2">
                <h3>Product 2</h3>
                <p>$29.99</p>
            </div>
            <div class="product-card">
                <img src="product3.jpg" alt="Product 3">
                <h3>Product 3</h3>
                <p>$39.99</p>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 RanchiOffline. All rights reserved.</p>
    </footer>

    <!-- Mobile Navigation -->
    <div class="mobile-nav">
        <button class="mobile-nav-toggle">Menu</button>
        <ul class="mobile-nav-links">
            <li><a href="#">Home</a></li>
            <li><a href="#">Products</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </div>
</body>
</html>
```

```css
/* styles.css */

:root {
    --primary-color: #333;
    --secondary-color: #666;
    --background-color: #f9f9f9;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: var(--primary-color);
    background-color: var(--background-color);
}

header {
    background-color: var(--primary-color);
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

header nav a:hover {
    color: var(--secondary-color);
}

.logo {
    font-size: 24px;
    font-weight: bold;
}

.hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #ddd);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--primary-color);
}

.hero h1 {
    font-size: 48px;
}

.hero p {
    font-size: 18px;
    margin-bottom: 20px;
}

.hero button {
    background-color: var(--primary-color);
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

.hero button:hover {
    background-color: var(--secondary-color);
}

.products {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.product-card {
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 20px;
    text-align: center;
}

.product-card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

.product-card h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

footer {
    background-color: var(--primary-color);
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

.mobile-nav {
    display: none;
}

.mobile-nav-toggle {
    background-color: var(--primary-color);
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
    position: fixed;
    top: 10px;
    right: 10px;
}

.mobile-nav-links {
    list-style: none;
    margin: 0;
    padding: 0;
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: var(--primary-color);
    padding: 20px;
}

.mobile-nav-links li {
    margin-bottom: 10px;
}

.mobile-nav-links a {
    color: #fff;
    text-decoration: none;
}

@media (max-width: 768px) {
    .mobile-nav {
        display: block;
    }

    .mobile-nav-links {
        display: block;
    }

    .product-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 480px) {
    .hero h1 {
        font-size: 36px;
    }

    .product-grid {
        grid-template-columns: 1fr;
    }
}
```
