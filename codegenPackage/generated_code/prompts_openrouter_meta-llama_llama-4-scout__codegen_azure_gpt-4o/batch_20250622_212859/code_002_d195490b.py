"""
Generated Code Metadata:
========================
Original URL: https://womensecretoutlet.shop
Prompt: Generate HTML/CSS code for a simple women's clothing product page layout inspired by womensecretoutlet.shop.
Generated: DETERMINISTIC_d195490b3902c1b5
Batch ID: 20250622_212859
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
  <meta name="description" content="Women's Clothing Product Page">
  <title>Women's Clothing Product Page</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">Women's Secret Outlet</h1>
      <nav class="nav">
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">Shop</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Main Content Section -->
  <main class="main-content">
    <div class="container">
      <h2 class="section-title">Featured Products</h2>
      <div class="product-grid">
        <!-- Product Card -->
        <div class="product-card">
          <img src="product1.jpg" alt="Product 1" class="product-image">
          <h3 class="product-title">Floral Dress</h3>
          <p class="product-price">$49.99</p>
          <button class="btn">Add to Cart</button>
        </div>
        <!-- Product Card -->
        <div class="product-card">
          <img src="product2.jpg" alt="Product 2" class="product-image">
          <h3 class="product-title">Casual Top</h3>
          <p class="product-price">$29.99</p>
          <button class="btn">Add to Cart</button>
        </div>
        <!-- Product Card -->
        <div class="product-card">
          <img src="product3.jpg" alt="Product 3" class="product-image">
          <h3 class="product-title">Summer Skirt</h3>
          <p class="product-price">$39.99</p>
          <button class="btn">Add to Cart</button>
        </div>
      </div>
    </div>
  </main>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 Women's Secret Outlet. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
* {
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

.header .logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.header .nav ul {
  list-style: none;
  display: flex;
  justify-content: flex-end;
}

.header .nav ul li {
  margin-left: 1rem;
}

.header .nav ul li a {
  color: #fff;
  text-decoration: none;
  font-size: 1rem;
}

.header .nav ul li a:hover {
  text-decoration: underline;
}

/* Main Content */
.main-content {
  padding: 2rem 0;
}

.section-title {
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2rem;
  color: #333;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.product-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 1rem;
  text-align: center;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-image {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
}

.product-title {
  font-size: 1.2rem;
  margin: 1rem 0 0.5rem;
}

.product-price {
  font-size: 1rem;
  color: #555;
  margin-bottom: 1rem;
}

.btn {
  display: inline-block;
  background-color: #333;
  color: #fff;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-transform: uppercase;
  font-size: 0.9rem;
}

.btn:hover {
  background-color: #555;
}

/* Footer */
.footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
  margin-top: 2rem;
}

.footer p {
  font-size: 0.9rem;
}
```
