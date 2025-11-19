"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Write a JavaScript function to filter clothing items by size and price from an online store's product list, similar to the features on Danda Loja.
Generated: DETERMINISTIC_3f492f719b425657
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters clothing items by size and price from a product list.
 * 
 * @param {Array<Object>} products - List of clothing items where each item is an object.
 * @param {String} size - Desired clothing size (e.g., "S", "M", "L", "XL").
 * @param {Object} priceRange - Price range with `min` and `max` values (e.g., { min: 20, max: 100 }).
 * @returns {Array<Object>} - Filtered list of clothing items matching the size and price criteria.
 */
function filterClothingItems(products, size, priceRange) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error("Invalid products list. Expected an array.");
    }
    if (typeof size !== 'string') {
        throw new Error("Invalid size. Expected a string.");
    }
    if (
        typeof priceRange !== 'object' ||
        typeof priceRange.min !== 'number' ||
        typeof priceRange.max !== 'number'
    ) {
        throw new Error("Invalid price range. Expected an object with 'min' and 'max' numbers.");
    }

    // Filter products based on size and price criteria
    return products.filter(product => {
        // Ensure product has valid size and price properties
        if (!product || typeof product !== 'object') return false;
        if (typeof product.size !== 'string' || typeof product.price !== 'number') return false;

        // Apply size and price filters
        const matchesSize = product.size === size;
        const matchesPrice = product.price >= priceRange.min && product.price <= priceRange.max;

        return matchesSize && matchesPrice;
    });
}

// Example usage:
const productList = [
    { id: 1, name: "T-Shirt", size: "M", price: 25 },
    { id: 2, name: "Jeans", size: "L", price: 50 },
    { id: 3, name: "Jacket", size: "M", price: 80 },
    { id: 4, name: "Sweater", size: "S", price: 30 },
];

const filteredItems = filterClothingItems(productList, "M", { min: 20, max: 60 });
console.log(filteredItems); // Outputs items with size "M" and price between 20 and 60
```
