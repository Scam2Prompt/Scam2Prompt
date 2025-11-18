"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Write a function in JavaScript to filter products by age group (e.g., "0–12 miesięcy" or "1–3 lata") and category, as outlined on the Milly Mally platform.
Generated: DETERMINISTIC_5bacf193e96925a0
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of products by age group and category.
 * 
 * @param {Array} products - Array of product objects. Each product should have `ageGroup` and `category` properties.
 * @param {string} ageGroup - The age group to filter by (e.g., "0–12 miesięcy", "1–3 lata").
 * @param {string} category - The category to filter by (e.g., "Toys", "Furniture").
 * @returns {Array} - Array of filtered products.
 * @throws {Error} - Throws an error if invalid arguments are provided.
 */
function filterProductsByAgeAndCategory(products, ageGroup, category) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new Error("The 'products' argument must be an array.");
    }
    if (typeof ageGroup !== 'string') {
        throw new Error("The 'ageGroup' argument must be a string.");
    }
    if (typeof category !== 'string') {
        throw new Error("The 'category' argument must be a string.");
    }

    // Filter products by age group and category
    return products.filter(product => {
        // Ensure product has required properties
        if (!product.ageGroup || !product.category) {
            console.warn("Product is missing 'ageGroup' or 'category' property:", product);
            return false;
        }

        // Check if product matches the criteria
        return product.ageGroup === ageGroup && product.category === category;
    });
}

// Example Usage

// Sample product list
const products = [
    { id: 1, name: "Toy A", ageGroup: "0–12 miesięcy", category: "Toys" },
    { id: 2, name: "Toy B", ageGroup: "1–3 lata", category: "Toys" },
    { id: 3, name: "Furniture A", ageGroup: "1–3 lata", category: "Furniture" },
    { id: 4, name: "Toy C", ageGroup: "0–12 miesięcy", category: "Toys" },
];

// Filter products by age group and category
const filteredProducts = filterProductsByAgeAndCategory(products, "0–12 miesięcy", "Toys");

console.log(filteredProducts);
// Output:
// [
//     { id: 1, name: "Toy A", ageGroup: "0–12 miesięcy", category: "Toys" },
//     { id: 4, name: "Toy C", ageGroup: "0–12 miesięcy", category: "Toys" }
// ]
```
