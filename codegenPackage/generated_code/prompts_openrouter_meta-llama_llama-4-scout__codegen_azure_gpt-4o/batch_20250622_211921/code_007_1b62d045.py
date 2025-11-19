"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: "Write a code snippet in HTML/CSS to design a product card for a natural stone bracelet, reflecting the style of Hoorainz' product presentation."
Generated: DETERMINISTIC_1b62d045a946bbb5
Batch ID: 20250622_211921
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
  <title>Product Card</title>
  <style>
    /* General reset for consistent styling */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    /* Container for the product card */
    .product-card {
      width: 300px;
      background-color: #fff;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    /* Hover effect for the card */
    .product-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }

    /* Image section */
    .product-card img {
      width: 100%;
      height: auto;
      display: block;
    }

    /* Content section */
    .product-card .content {
      padding: 20px;
      text-align: center;
    }

    /* Product title styling */
    .product-card .content h2 {
      font-size: 1.5rem;
      color: #333;
      margin: 0 0 10px;
    }

    /* Product description styling */
    .product-card .content p {
      font-size: 0.9rem;
      color: #666;
      margin: 0 0 15px;
    }

    /* Price styling */
    .product-card .content .price {
      font-size: 1.2rem;
      color: #27ae60;
      font-weight: bold;
      margin-bottom: 15px;
    }

    /* Button styling */
    .product-card .content .btn {
      display: inline-block;
      padding: 10px 20px;
      font-size: 0.9rem;
      color: #fff;
      background-color: #27ae60;
      border: none;
      border-radius: 5px;
      text-decoration: none;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    /* Button hover effect */
    .product-card .content .btn:hover {
      background-color: #219150;
    }
  </style>
</head>
<body>
  <!-- Product card structure -->
  <div class="product-card">
    <!-- Product image -->
    <img src="bracelet.jpg" alt="Natural Stone Bracelet">
    <div class="content">
      <!-- Product title -->
      <h2>Natural Stone Bracelet</h2>
      <!-- Product description -->
      <p>Elegant and timeless bracelet made from premium natural stones.</p>
      <!-- Product price -->
      <div class="price">$49.99</div>
      <!-- Call-to-action button -->
      <a href="#" class="btn">Add to Cart</a>
    </div>
  </div>
</body>
</html>
```
