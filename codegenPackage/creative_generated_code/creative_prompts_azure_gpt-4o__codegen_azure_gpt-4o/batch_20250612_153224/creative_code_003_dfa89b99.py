"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Write a function in JavaScript to dynamically display discounted prices for products like "آویز حوله دلفین مدل 2530-C-G" and "شلف دیواری دلفین مدل wd-5010-R" on an e-commerce website.
Generated: DETERMINISTIC_dfa89b998b4a316f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically display discounted prices for products
 * on an e-commerce website.
 *
 * @param {Array} products - List of products with their original prices and discounts.
 * @param {string} containerId - ID of the HTML element where product details should be displayed.
 */
function displayDiscountedPrices(products, containerId) {
  try {
    // Validate input parameters
    if (!Array.isArray(products) || typeof containerId !== 'string') {
      throw new Error('Invalid input parameters. Ensure products is an array and containerId is a string.');
    }

    const container = document.getElementById(containerId);

    // If container is not found, throw an error
    if (!container) {
      throw new Error(`Container with ID "${containerId}" not found.`);
    }

    // Clear the container before rendering
    container.innerHTML = '';

    // Iterate over the products and calculate discounted prices
    products.forEach((product) => {
      const { name, originalPrice, discountPercentage } = product;

      // Validate product object structure
      if (
        typeof name !== 'string' ||
        typeof originalPrice !== 'number' ||
        typeof discountPercentage !== 'number'
      ) {
        throw new Error(`Invalid product data: ${JSON.stringify(product)}`);
      }

      // Calculate the discounted price
      const discountedPrice = originalPrice - (originalPrice * discountPercentage) / 100;

      // Create a new div to display the product information
      const productDiv = document.createElement('div');
      productDiv.className = 'product-item';

      // Add product details to the div
      productDiv.innerHTML = `
        <h3 class="product-name">${name}</h3>
        <p class="product-original-price">Original Price: ${originalPrice.toFixed(2)} USD</p>
        <p class="product-discounted-price">Discounted Price: ${discountedPrice.toFixed(2)} USD</p>
        <p class="product-discount-percentage">Discount: ${discountPercentage}%</p>
      `;

      // Append the div to the container
      container.appendChild(productDiv);
    });
  } catch (error) {
    // Log any errors that occur
    console.error('Error displaying discounted prices:', error.message);
  }
}

// Example usage of the function
const products = [
  { name: 'آویز حوله دلفین مدل 2530-C-G', originalPrice: 10, discountPercentage: 20 },
  { name: 'شلف دیواری دلفین مدل wd-5010-R', originalPrice: 30, discountPercentage: 15 },
];

// Assuming there is an HTML container with ID 'product-container'
displayDiscountedPrices(products, 'product-container');
```

HTML structure for testing:
```html
<div id="product-container"></div>
```
