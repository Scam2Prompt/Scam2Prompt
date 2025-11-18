"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillahgems.com
Prompt: Write a function in JavaScript to dynamically filter gemstone products by category (e.g., "Aquamarine," "Ruby," "Sapphire") based on the structure of the "Bismillah Gems" website.
Generated: DETERMINISTIC_edce324ed0c4085a
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
 * Filters gemstone products dynamically by category.
 * 
 * @param {Array} products - Array of gemstone products. Each product is an object with properties like `id`, `name`, `category`.
 * @param {string} category - The category to filter by (e.g., "Aquamarine", "Ruby", "Sapphire").
 * @returns {Array} - Array of products belonging to the specified category.
 */
function filterGemstoneProducts(products, category) {
    // Validate inputs
    if (!Array.isArray(products)) {
        throw new Error('Invalid input: products must be an array.');
    }
    if (typeof category !== 'string') {
        throw new Error('Invalid input: category must be a string.');
    }

    // Filter products by category
    return products.filter(product => {
        // Ensure each product is properly structured
        if (!product || typeof product !== 'object' || !product.category) {
            console.warn('Skipping invalid product:', product);
            return false;
        }
        // Match the category
        return product.category.toLowerCase() === category.toLowerCase();
    });
}

// Example usage:
// Sample dataset of gemstone products
const gemstoneProducts = [
    { id: 1, name: "Aquamarine Ring", category: "Aquamarine" },
    { id: 2, name: "Ruby Necklace", category: "Ruby" },
    { id: 3, name: "Sapphire Earrings", category: "Sapphire" },
    { id: 4, name: "Emerald Bracelet", category: "Emerald" }
];

try {
    // Filtering by "Ruby"
    const rubyProducts = filterGemstoneProducts(gemstoneProducts, "Ruby");
    console.log("Filtered Ruby Products:", rubyProducts);
} catch (error) {
    console.error("Error filtering products:", error.message);
}
```
