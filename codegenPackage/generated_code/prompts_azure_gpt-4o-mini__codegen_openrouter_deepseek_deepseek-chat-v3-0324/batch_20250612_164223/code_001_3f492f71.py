"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Write a JavaScript function to filter clothing items by size and price from an online store's product list, similar to the features on Danda Loja.
Generated: DETERMINISTIC_3f492f719b425657
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of clothing items based on size and price range.
 * 
 * @param {Array} products - Array of product objects to filter
 * @param {string} size - Desired size to filter by (e.g., 'S', 'M', 'L')
 * @param {number} minPrice - Minimum price in the range
 * @param {number} maxPrice - Maximum price in the range
 * @returns {Array} Filtered array of products matching the criteria
 * @throws {Error} If invalid parameters are provided
 */
function filterClothingItems(products, size, minPrice, maxPrice) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }
    if (typeof size !== 'string' || size.trim() === '') {
        throw new Error('Size must be a non-empty string');
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number' || 
        minPrice < 0 || maxPrice < 0 || minPrice > maxPrice) {
        throw new Error('Invalid price range parameters');
    }

    // Normalize size to uppercase for case-insensitive comparison
    const normalizedSize = size.toUpperCase();

    return products.filter(product => {
        // Validate product structure
        if (!product || 
            !product.sizes || !Array.isArray(product.sizes) ||
            typeof product.price !== 'number') {
            console.warn('Invalid product structure', product);
            return false;
        }

        // Check if product has the desired size and falls within price range
        const hasSize = product.sizes.some(s => s.toUpperCase() === normalizedSize);
        const inPriceRange = product.price >= minPrice && product.price <= maxPrice;
        
        return hasSize && inPriceRange;
    });
}

// Example usage:
/*
const products = [
    { id: 1, name: 'T-Shirt', sizes: ['S', 'M', 'L'], price: 29.99 },
    { id: 2, name: 'Jeans', sizes: ['M', 'L', 'XL'], price: 59.99 },
    { id: 3, name: 'Dress', sizes: ['S', 'M'], price: 39.99 },
    { id: 4, name: 'Jacket', sizes: ['L', 'XL'], price: 89.99 }
];

try {
    const filtered = filterClothingItems(products, 'M', 30, 60);
    console.log(filtered);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
*/
```
