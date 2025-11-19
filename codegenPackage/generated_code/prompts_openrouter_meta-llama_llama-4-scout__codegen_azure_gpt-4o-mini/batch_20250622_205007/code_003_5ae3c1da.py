"""
Generated Code Metadata:
========================
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Write a JavaScript code to implement a product filtering system, similar to the one used on the webpage, to filter shoes by brand (e.g., Nike, Mizuno, Puma) and price range.
Generated: DETERMINISTIC_5ae3c1da72e3ff70
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product filtering system for shoes by brand and price range

// Sample data representing a collection of shoe products
const products = [
    { id: 1, brand: 'Nike', price: 120 },
    { id: 2, brand: 'Mizuno', price: 90 },
    { id: 3, brand: 'Puma', price: 75 },
    { id: 4, brand: 'Nike', price: 150 },
    { id: 5, brand: 'Mizuno', price: 110 },
    { id: 6, brand: 'Puma', price: 60 },
];

// Function to filter products based on brand and price range
/**
 * Filters the products array based on the specified brand and price range.
 * @param {Array} products - The array of product objects to filter.
 * @param {string} brand - The brand to filter by (e.g., 'Nike').
 * @param {number} minPrice - The minimum price for the filter.
 * @param {number} maxPrice - The maximum price for the filter.
 * @returns {Array} - An array of filtered product objects.
 */
function filterProducts(products, brand, minPrice, maxPrice) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error('Invalid products array');
    }
    if (typeof brand !== 'string' || typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Invalid input types');
    }
    if (minPrice < 0 || maxPrice < 0 || minPrice > maxPrice) {
        throw new Error('Invalid price range');
    }

    // Filter products based on brand and price range
    return products.filter(product => 
        product.brand === brand && 
        product.price >= minPrice && 
        product.price <= maxPrice
    );
}

// Example usage of the filterProducts function
try {
    const filteredProducts = filterProducts(products, 'Nike', 100, 150);
    console.log('Filtered Products:', filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
