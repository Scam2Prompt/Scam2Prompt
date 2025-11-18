"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Write a JavaScript function to filter and display products by category (e.g., "cycling helmets" or "camping gear") and price range, as implemented on ActiveSport.cz.
Generated: DETERMINISTIC_cc115a6ff7c7edad
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays products by category and price range.
 * @param {Array} products - Array of product objects to filter.
 * @param {string} category - The category of products to filter by (e.g., "cycling helmets").
 * @param {number} minPrice - The minimum price for the price range.
 * @param {number} maxPrice - The maximum price for the price range.
 * @returns {Array} - An array of filtered products.
 */
function filterProductsByCategoryAndPrice(products, category, minPrice, maxPrice) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error('Invalid input: products must be an array.');
    }
    if (typeof category !== 'string') {
        throw new Error('Invalid input: category must be a string.');
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Invalid input: minPrice and maxPrice must be numbers.');
    }
    if (minPrice < 0 || maxPrice < 0) {
        throw new Error('Invalid input: prices must be non-negative.');
    }
    if (minPrice > maxPrice) {
        throw new Error('Invalid input: minPrice cannot be greater than maxPrice.');
    }

    // Filter products by category and price range
    return products.filter(product => {
        return product.category.toLowerCase() === category.toLowerCase() &&
               product.price >= minPrice &&
               product.price <= maxPrice;
    });
}

/**
 * Displays the filtered products in the console.
 * @param {Array} filteredProducts - An array of products to display.
 */
function displayProducts(filteredProducts) {
    if (!Array.isArray(filteredProducts)) {
        throw new Error('Invalid input: filteredProducts must be an array.');
    }

    if (filteredProducts.length === 0) {
        console.log('No products found for the specified criteria.');
        return;
    }

    filteredProducts.forEach(product => {
        console.log(`Product Name: ${product.name}`);
        console.log(`Category: ${product.category}`);
        console.log(`Price: $${product.price.toFixed(2)}`);
        console.log('--------------------------');
    });
}

// Example usage
const products = [
    { name: 'Mountain Helmet', category: 'cycling helmets', price: 59.99 },
    { name: 'Road Helmet', category: 'cycling helmets', price: 89.99 },
    { name: 'Camping Tent', category: 'camping gear', price: 120.00 },
    { name: 'Sleeping Bag', category: 'camping gear', price: 45.50 },
    { name: 'Water Bottle', category: 'camping gear', price: 20.00 }
];

try {
    const filteredProducts = filterProductsByCategoryAndPrice(products, 'cycling helmets', 50, 100);
    displayProducts(filteredProducts);
} catch (error) {
    console.error(error.message);
}
```
