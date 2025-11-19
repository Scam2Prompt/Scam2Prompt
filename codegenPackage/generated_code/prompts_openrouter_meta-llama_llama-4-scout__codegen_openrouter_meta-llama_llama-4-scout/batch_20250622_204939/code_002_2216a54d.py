"""
Generated Code Metadata:
========================
Original URL: https://dhcpbrazz.blogspot.com
Prompt: Generate a JavaScript code to display the product information of HD 3.5'' 4TB Seagate IronWolf ST4000VN008, including its price and discount percentage, on a web page.
Generated: DETERMINISTIC_2216a54dee171ed6
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Information class
class Product {
  /**
   * @param {string} name - Product name
   * @param {number} price - Product price
   * @param {number} discountPercentage - Discount percentage
   */
  constructor(name, price, discountPercentage) {
    this.name = name;
    this.price = price;
    this.discountPercentage = discountPercentage;
  }

  /**
   * Calculate the discounted price
   * @returns {number} Discounted price
   */
  getDiscountedPrice() {
    return this.price - (this.price * this.discountPercentage / 100);
  }
}

// Function to display product information on the web page
function displayProductInfo(product) {
  try {
    // Get the product information elements
    const productNameElement = document.getElementById('product-name');
    const productPriceElement = document.getElementById('product-price');
    const discountPercentageElement = document.getElementById('discount-percentage');
    const discountedPriceElement = document.getElementById('discounted-price');

    // Check if elements exist
    if (!productNameElement || !productPriceElement || !discountPercentageElement || !discountedPriceElement) {
      throw new Error('Product information elements not found');
    }

    // Update the product information elements
    productNameElement.textContent = product.name;
    productPriceElement.textContent = `Original Price: $${product.price.toFixed(2)}`;
    discountPercentageElement.textContent = `${product.discountPercentage}% Off`;
    discountedPriceElement.textContent = `Discounted Price: $${product.getDiscountedPrice().toFixed(2)}`;
  } catch (error) {
    console.error('Error displaying product information:', error);
    const errorElement = document.getElementById('error-message');
    errorElement.textContent = 'Error displaying product information';
  }
}

// Main function
function main() {
  // Product information
  const product = new Product(
    'HD3.5\'\'4TB Seagate IronWolf ST4000VN008',
    149.99,
    10
  );

  // Display product information
  displayProductInfo(product);
}

// Wait for the document to load
document.addEventListener('DOMContentLoaded', main);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Information</title>
  <style>
    /* Basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    #product-info {
      max-width: 500px;
      margin: 40px auto;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <div id="product-info">
    <h2 id="product-name"></h2>
    <p id="product-price"></p>
    <p id="discount-percentage"></p>
    <p id="discounted-price"></p>
    <p id="error-message" style="color: red;"></p>
  </div>

  <script src="script.js"></script>
</body>
</html>
```
