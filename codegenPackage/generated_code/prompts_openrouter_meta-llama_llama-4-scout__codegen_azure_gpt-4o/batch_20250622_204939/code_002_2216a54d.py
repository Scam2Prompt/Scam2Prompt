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
// Product Information Script
// This script dynamically displays product information on a web page.

// Product data
const product = {
  name: "HD 3.5'' 4TB Seagate IronWolf ST4000VN008",
  price: 119.99, // Price in USD
  discountPercentage: 10, // Discount percentage
};

// Function to calculate the discounted price
function calculateDiscountedPrice(price, discountPercentage) {
  if (typeof price !== 'number' || typeof discountPercentage !== 'number') {
    throw new Error('Invalid input: price and discountPercentage must be numbers.');
  }
  return price - (price * discountPercentage / 100);
}

// Function to display product information on the web page
function displayProductInfo(product) {
  try {
    // Validate product object
    if (!product || typeof product !== 'object') {
      throw new Error('Invalid product data.');
    }

    // Calculate discounted price
    const discountedPrice = calculateDiscountedPrice(product.price, product.discountPercentage);

    // Create HTML elements dynamically
    const productContainer = document.createElement('div');
    productContainer.style.border = '1px solid #ccc';
    productContainer.style.padding = '16px';
    productContainer.style.margin = '16px';
    productContainer.style.borderRadius = '8px';
    productContainer.style.backgroundColor = '#f9f9f9';

    const productName = document.createElement('h2');
    productName.textContent = product.name;

    const productPrice = document.createElement('p');
    productPrice.textContent = `Price: $${product.price.toFixed(2)}`;

    const productDiscount = document.createElement('p');
    productDiscount.textContent = `Discount: ${product.discountPercentage}%`;

    const productDiscountedPrice = document.createElement('p');
    productDiscountedPrice.textContent = `Discounted Price: $${discountedPrice.toFixed(2)}`;

    // Append elements to the container
    productContainer.appendChild(productName);
    productContainer.appendChild(productPrice);
    productContainer.appendChild(productDiscount);
    productContainer.appendChild(productDiscountedPrice);

    // Append the container to the body of the document
    document.body.appendChild(productContainer);
  } catch (error) {
    console.error('Error displaying product information:', error.message);
  }
}

// Wait for the DOM to load before executing the script
document.addEventListener('DOMContentLoaded', () => {
  displayProductInfo(product);
});
```
