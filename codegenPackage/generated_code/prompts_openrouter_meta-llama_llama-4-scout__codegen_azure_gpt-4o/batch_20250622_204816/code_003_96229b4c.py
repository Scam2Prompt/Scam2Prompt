"""
Generated Code Metadata:
========================
Original URL: https://parsflooring.net
Prompt: Create a simple HTML and CSS template for a flooring website's product page, featuring product images, descriptions, and pricing information.
Generated: DETERMINISTIC_96229b4cd522891e
Batch ID: 20250622_204816
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
  <meta name="description" content="Flooring product page showcasing high-quality flooring options with images, descriptions, and pricing.">
  <title>Flooring Products</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1>Flooring Products</h1>
      <p>Explore our premium flooring options for your home or office.</p>
    </div>
  </header>

  <!-- Product Section -->
  <main class="product-section">
    <div class="container">
      <!-- Product 1 -->
      <div class="product-card">
        <img src="images/product1.jpg" alt="Hardwood Flooring" class="product-image">
        <h2 class="product-title">Hardwood Flooring</h2>
        <p class="product-description">Elegant and durable hardwood flooring to enhance your space.</p>
        <p class="product-price">$49.99 / sq ft</p>
      </div>

      <!-- Product 2 -->
      <div class="product-card">
        <img src="images/product2.jpg" alt="Laminate Flooring" class="product-image">
        <h2 class="product-title">Laminate Flooring</h2>
        <p class="product-description">Affordable and stylish laminate flooring for modern interiors.</p>
        <p class="product-price">$29.99 / sq ft</p>
      </div>

      <!-- Product 3 -->
      <div class="product-card">
        <img src="images/product3.jpg" alt="Vinyl Flooring" class="product-image">
        <h2 class="product-title">Vinyl Flooring</h2>
        <p class="product-description">Water-resistant vinyl flooring perfect for kitchens and bathrooms.</p>
        <p class="product-price">$19.99 / sq ft</p>
      </div>
    </div>
  </main>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 Flooring Co. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p {
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

/* Header Section */
.header {
  background-color: #4CAF50;
  color: #fff;
  padding: 20px 0;
  text-align: center;
}

.header h1 {
  font-size: 2.5rem;
}

.header p {
  font-size: 1.2rem;
}

/* Product Section */
.product-section {
  padding: 20px 0;
}

.product-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 5px;
  margin: 20px 0;
  padding: 15px;
  text-align: center;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-image {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
}

.product-title {
  font-size: 1.5rem;
  margin: 10px 0;
}

.product-description {
  font-size: 1rem;
  margin: 10px 0;
  color: #555;
}

.product-price {
  font-size: 1.2rem;
  font-weight: bold;
  color: #4CAF50;
}

/* Footer Section */
.footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 10px 0;
}

.footer p {
  font-size: 0.9rem;
}
```
