"""
Generated Code Metadata:
========================
Original URL: https://ktfmultan.com
Prompt: Create a JavaScript function to implement a filtering system for an e-commerce website, allowing customers to filter products by categories like "Winters", "Summers", "Bridal", and "Print Khes".
Generated: DETERMINISTIC_fd5849603269a69f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of products based on the selected category.
 * 
 * @param {Array} products - The array of product objects to filter.
 * @param {string} category - The category to filter products by.
 * @returns {Array} - An array of products that belong to the specified category.
 * @throws {Error} - Throws an error if the products array is not an array or if the category is not a string.
 */
function filterProductsByCategory(products, category) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new Error("The 'products' parameter must be an array.");
    }
    if (typeof category !== 'string') {
        throw new Error("The 'category' parameter must be a string.");
    }

    // Define valid categories
    const validCategories = ["Winters", "Summers", "Bridal", "Print Khes"];

    // Check if the provided category is valid
    if (!validCategories.includes(category)) {
        throw new Error(`Invalid category. Valid categories are: ${validCategories.join(", ")}`);
    }

    // Filter products based on the selected category
    return products.filter(product => product.category === category);
}

// Example usage
const products = [
    { id: 1, name: "Winter Jacket", category: "Winters" },
    { id: 2, name: "Summer Dress", category: "Summers" },
    { id: 3, name: "Bridal Gown", category: "Bridal" },
    { id: 4, name: "Print Khes Scarf", category: "Print Khes" },
    { id: 5, name: "Winter Boots", category: "Winters" }
];

try {
    const filteredProducts = filterProductsByCategory(products, "Winters");
    console.log(filteredProducts);
} catch (error) {
    console.error(error.message);
}
```
