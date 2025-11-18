"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thewallethub.com
Prompt: Write a JavaScript function to filter products by categories such as "Cakes," "Flowers," and "Footwear Accessories," similar to the organization on TheWalletStore.
Generated: DETERMINISTIC_57d24ba808d62f0e
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of products by a specified category.
 * 
 * @param {Array} products - Array of product objects, each containing a `name` and `category`.
 * @param {String} category - The category to filter products by (e.g., "Cakes", "Flowers", "Footwear Accessories").
 * @returns {Array} - Array of filtered product objects that match the specified category.
 */
function filterProductsByCategory(products, category) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error("Invalid products list: Expected an array.");
    }
    if (typeof category !== 'string') {
        throw new Error("Invalid category: Expected a string.");
    }

    // Filter the products by the specified category
    const filteredProducts = products.filter(product => {
        // Ensure each product object has a `category` property and matches the provided category
        return product.category && product.category.toLowerCase() === category.toLowerCase();
    });

    return filteredProducts;
}

// Example Usage:

// Sample product list
const products = [
    { name: "Chocolate Cake", category: "Cakes" },
    { name: "Rose Bouquet", category: "Flowers" },
    { name: "Shoelaces", category: "Footwear Accessories" },
    { name: "Vanilla Cupcake", category: "Cakes" },
    { name: "Tulips", category: "Flowers" },
];

// Filter for "Cakes"
const cakes = filterProductsByCategory(products, "Cakes");
console.log(cakes);
// Output: [ { name: "Chocolate Cake", category: "Cakes" }, { name: "Vanilla Cupcake", category: "Cakes" } ]

// Filter for "Footwear Accessories"
const footwearAccessories = filterProductsByCategory(products, "Footwear Accessories");
console.log(footwearAccessories);
// Output: [ { name: "Shoelaces", category: "Footwear Accessories" } ]
```
