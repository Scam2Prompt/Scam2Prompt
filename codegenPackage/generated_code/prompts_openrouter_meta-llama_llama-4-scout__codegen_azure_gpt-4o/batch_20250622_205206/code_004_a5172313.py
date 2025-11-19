"""
Generated Code Metadata:
========================
Original URL: https://sayacosmetics.com
Prompt: "Create a simple HTML/CSS template for a cosmetics product page, similar to what might be found on sayacosmetics.com, using WordPress's block editor."
Generated: DETERMINISTIC_a5172313670c1fd7
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- HTML Template for Cosmetics Product Page -->
<!-- This template is designed to be used with WordPress's block editor -->

<!-- Main Container -->
<div class="product-page-container">
  <!-- Product Image Section -->
  <div class="product-image">
    <img src="path-to-product-image.jpg" alt="Product Name" />
  </div>

  <!-- Product Details Section -->
  <div class="product-details">
    <h1 class="product-title">Product Name</h1>
    <p class="product-description">
      A brief description of the product goes here. Highlight key features and benefits.
    </p>
    <p class="product-price">$29.99</p>

    <!-- Add to Cart Button -->
    <button class="add-to-cart-button">Add to Cart</button>
  </div>
</div>

<!-- CSS Styles -->
<style>
  /* General Styles */
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;
  }

  /* Main Container */
  .product-page-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
    background-color: #fff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
  }

  /* Product Image Section */
  .product-image img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
  }

  /* Product Details Section */
  .product-details {
    margin-left: 20px;
    max-width: 600px;
  }

  .product-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .product-description {
    font-size: 16px;
    color: #555;
    margin-bottom: 20px;
  }

  .product-price {
    font-size: 20px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
  }

  .add-to-cart-button {
    background-color: #ff6f61;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .add-to-cart-button:hover {
    background-color: #e65b50;
  }
</style>
```

This code can be pasted into the WordPress block editor using the "Custom HTML" block. Adjust the `path-to-product-image.jpg` to the actual image URL and customize the text content as needed.
