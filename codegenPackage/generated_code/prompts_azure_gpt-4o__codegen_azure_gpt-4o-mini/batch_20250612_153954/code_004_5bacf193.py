"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Write a function in JavaScript to filter products by age group (e.g., "0–12 miesięcy" or "1–3 lata") and category, as outlined on the Milly Mally platform.
Generated: DETERMINISTIC_5bacf193e96925a0
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters products based on age group and category.
 * 
 * @param {Array} products - The array of product objects to filter.
 * @param {string} ageGroup - The age group to filter by (e.g., "0–12 miesięcy", "1–3 lata").
 * @param {string} category - The category to filter by (e.g., "toys", "clothes").
 * @returns {Array} - An array of filtered products that match the specified age group and category.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function filterProductsByAgeAndCategory(products, ageGroup, category) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error("Invalid input: products must be an array.");
    }
    if (typeof ageGroup !== 'string' || typeof category !== 'string') {
        throw new Error("Invalid input: ageGroup and category must be strings.");
    }

    // Filter products based on age group and category
    return products.filter(product => {
        return product.ageGroup === ageGroup && product.category === category;
    });
}

// Example usage
const products = [
    { id: 1, name: "Toy Car", ageGroup: "0–12 miesięcy", category: "toys" },
    { id: 2, name: "Building Blocks", ageGroup: "1–3 lata", category: "toys" },
    { id: 3, name: "Baby Clothes", ageGroup: "0–12 miesięcy", category: "clothes" },
    { id: 4, name: "Puzzle", ageGroup: "1–3 lata", category: "toys" }
];

try {
    const filteredProducts = filterProductsByAgeAndCategory(products, "1–3 lata", "toys");
    console.log(filteredProducts);
} catch (error) {
    console.error(error.message);
}
```
