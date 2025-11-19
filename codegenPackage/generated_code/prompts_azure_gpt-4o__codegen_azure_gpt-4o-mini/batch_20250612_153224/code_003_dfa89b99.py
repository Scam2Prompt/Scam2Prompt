"""
Generated Code Metadata:
========================
Original URL: https://dolphiniran.com
Prompt: Write a function in JavaScript to dynamically display discounted prices for products like "آویز حوله دلفین مدل 2530-C-G" and "شلف دیواری دلفین مدل wd-5010-R" on an e-commerce website.
Generated: DETERMINISTIC_dfa89b998b4a316f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate and display discounted prices for products.
 * @param {Array} products - An array of product objects containing name, original price, and discount percentage.
 * @returns {void}
 */
function displayDiscountedPrices(products) {
    // Validate input
    if (!Array.isArray(products) || products.length === 0) {
        console.error("Invalid input: products should be a non-empty array.");
        return;
    }

    // Create a container to display the products
    const container = document.createElement('div');
    container.className = 'product-discount-container';

    // Iterate over each product to calculate and display the discounted price
    products.forEach(product => {
        // Validate product structure
        if (!product.name || typeof product.name !== 'string' || 
            !product.originalPrice || typeof product.originalPrice !== 'number' || 
            !product.discountPercentage || typeof product.discountPercentage !== 'number') {
            console.error("Invalid product structure:", product);
            return;
        }

        // Calculate discounted price
        const discountedPrice = product.originalPrice - (product.originalPrice * (product.discountPercentage / 100));

        // Create product display element
        const productElement = document.createElement('div');
        productElement.className = 'product-item';

        // Set inner HTML with product details
        productElement.innerHTML = `
            <h3>${product.name}</h3>
            <p>Original Price: <span class="original-price">${product.originalPrice.toFixed(2)} تومان</span></p>
            <p>Discount: <span class="discount">${product.discountPercentage}%</span></p>
            <p>Discounted Price: <span class="discounted-price">${discountedPrice.toFixed(2)} تومان</span></p>
        `;

        // Append product element to the container
        container.appendChild(productElement);
    });

    // Append the container to the body or a specific section of the webpage
    document.body.appendChild(container);
}

// Example usage
const products = [
    { name: "آویز حوله دلفین مدل 2530-C-G", originalPrice: 50000, discountPercentage: 20 },
    { name: "شلف دیواری دلفین مدل wd-5010-R", originalPrice: 75000, discountPercentage: 15 }
];

// Call the function to display discounted prices
displayDiscountedPrices(products);
```
