"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://techcherio.com
Prompt: Create a sample HTML/CSS layout for an eCommerce website, inspired by the web design services provided by TechCherio.
Generated: DETERMINISTIC_075cc0948892fe50
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="TechCherio-inspired eCommerce layout">
  <title>eCommerce Website</title>
  <!-- Link to external CSS file -->
  <link rel="stylesheet" href="styles.css">
  <!-- Include Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <div class="logo">
        <a href="#">TechCherioShop</a>
      </div>
      <nav class="navigation">
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">Shop</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
      <div class="cart">
        <a href="#">Cart (0)</a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <h1>Welcome to TechCherioShop</h1>
      <p>Discover the latest tech gadgets and accessories.</p>
      <a href="#" class="btn">Shop Now</a>
    </div>
  </section>

  <!-- Product Section -->
  <section class="products">
    <div class="container">
      <h2>Featured Products</h2>
      <div class="product-grid">
        <div class="product-item">
          <img src="placeholder1.jpg" alt="Product 1">
          <h3>Product 1</h3>
          <p>$49.99</p>
          <a href="#" class="btn">Add to Cart</a>
        </div>
        <div class="product-item">
          <img src="placeholder2.jpg" alt="Product 2">
          <h3>Product 2</h3>
          <p>$79.99</p>
          <a href="#" class="btn">Add to Cart</a>
        </div>
        <div class="product-item">
          <img src="placeholder3.jpg" alt="Product 3">
          <h3>Product 3</h3>
          <p>$99.99</p>
          <a href="#" class="btn">Add to Cart</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer Section -->
  <footer>
    <div class="container">
      <div class="footer-info">
        <p>&copy; 2023 TechCherioShop. All rights reserved.</p>
      </div>
      <div class="social-links">
        <a href="#">Facebook</a>
        <a href="#">Twitter</a>
        <a href="#">Instagram</a>
      </div>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Font and colors */
body {
  font-family: 'Roboto', sans-serif;
  line-height: 1.6;
  color: #333;
}

/* Container */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

/* Header Section */
header {
  background: #222;
  color: #fff;
  padding: 10px 0;
}

header .logo a {
  color: #fff;
  text-decoration: none;
  font-size: 24px;
  font-weight: bold;
}

header .navigation ul {
  display: flex;
  list-style: none;
}

header .navigation ul li {
  margin: 0 10px;
}

header .navigation ul li a {
  color: #fff;
  text-decoration: none;
}

header .cart a {
  color: #fff;
  text-decoration: none;
}

/* Hero Section */
.hero {
  background: #f4f4f4;
  text-align: center;
  padding: 50px 20px;
}

.hero h1 {
  font-size: 36px;
}

.hero p {
  margin: 20px 0;
}

.hero .btn {
  background: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  text-decoration: none;
  font-size: 16px;
}

/* Product Section */
.products {
  padding: 50px 20px;
}

.products h2 {
  text-align: center;
  margin-bottom: 30px;
}

.product-grid {
  display: flex;
  gap: 20px;
  justify-content: space-around;
}

.product-item {
  background: #f9f9f9;
  padding: 15px;
  text-align: center;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.product-item h3 {
  margin: 10px 0;
}

.product-item .btn {
  background: #007bff;
  color: #fff;
  padding: 10px 15px;
  border: none;
  text-decoration: none;
  font-size: 14px;
}

/* Footer Section */
footer {
  background: #222;
  color: #fff;
  text-align: center;
  padding: 15px 0;
}

footer .social-links a {
  color: #fff;
  text-decoration: none;
  margin: 0 10px;
}
```
