"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: "Generate a JavaScript function to display product promotions, like discounts on tinta spray verniz and luvas de segurança, on an e-commerce website."
Generated: DETERMINISTIC_94604a5614936f24
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays product promotions on an e-commerce website.
 * 
 * @param {Object[]} products - Array of product objects.
 * @param {string} products[].name - Product name.
 * @param {number} products[].originalPrice - Original price of the product.
 * @param {number} products[].discount - Discount percentage.
 * 
 * @returns {void}
 */
function displayProductPromotions(products) {
    // Check if products is an array
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }

    // Iterate over each product
    products.forEach((product) => {
        // Check if product has required properties
        if (!product.name || !product.originalPrice || !product.discount) {
            throw new Error(`Product ${JSON.stringify(product)} is missing required properties`);
        }

        // Calculate discounted price
        const discountedPrice = calculateDiscountedPrice(product.originalPrice, product.discount);

        // Display product promotion
        console.log(`Product: ${product.name}`);
        console.log(`Original Price: R$${product.originalPrice.toFixed(2)}`);
        console.log(`Discount: ${product.discount}%`);
        console.log(`Discounted Price: R$${discountedPrice.toFixed(2)}`);
        console.log('------------------------');
    });
}

/**
 * Calculates the discounted price of a product.
 * 
 * @param {number} originalPrice - Original price of the product.
 * @param {number} discount - Discount percentage.
 * 
 * @returns {number} Discounted price.
 */
function calculateDiscountedPrice(originalPrice, discount) {
    // Check if originalPrice and discount are valid numbers
    if (typeof originalPrice !== 'number' || typeof discount !== 'number') {
        throw new Error('Original price and discount must be numbers');
    }

    // Calculate discounted price
    return originalPrice - (originalPrice * (discount / 100));
}

// Example usage
const products = [
    {
        name: 'Tinta Spray Verniz',
        originalPrice: 50.00,
        discount: 10
    },
    {
        name: 'Luvas de Segurança',
        originalPrice: 20.00,
        discount: 20
    }
];

try {
    displayProductPromotions(products);
} catch (error) {
    console.error(error.message);
}
```
