"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonswallet.top
Prompt: Create a JavaScript function that filters track cycling products by category, such as "Track Bikes" or "Track Helmets," as seen on the Velodrome Shop website.
Generated: DETERMINISTIC_c2feabe90882acaf
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters an array of track cycling products by category.
 * @param {Array<Object>} products - The array of products to filter.
 * @param {string} category - The category to filter by (e.g., "Track Bikes", "Track Helmets").
 * @returns {Array<Object>} - An array of products that belong to the specified category.
 * @throws {Error} - Throws an error if the input products is not an array or if category is not a string.
 */
function filterProductsByCategory(products, category) {
    // Input validation
    if (!Array.isArray(products)) {
        throw new Error('Invalid input: products must be an array.');
    }
    if (typeof category !== 'string') {
        throw new Error('Invalid input: category must be a string.');
    }

    // Use Array.prototype.filter to return products that match the specified category
    return products.filter(product => {
        // Ensure product has a category property and compare it to the provided category
        return product.category && product.category.toLowerCase() === category.toLowerCase();
    });
}

// Example usage
const products = [
    { id: 1, name: 'Speedster Track Bike', category: 'Track Bikes' },
    { id: 2, name: 'Pro Track Helmet', category: 'Track Helmets' },
    { id: 3, name: 'Urban Track Bike', category: 'Track Bikes' },
    { id: 4, name: 'Safety Track Helmet', category: 'Track Helmets' }
];

try {
    const filteredBikes = filterProductsByCategory(products, 'Track Bikes');
    console.log('Filtered Track Bikes:', filteredBikes);
    
    const filteredHelmets = filterProductsByCategory(products, 'Track Helmets');
    console.log('Filtered Track Helmets:', filteredHelmets);
} catch (error) {
    console.error(error.message);
}
```
