"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Create a JavaScript function to display product availability and sorting options for an online store focused on home goods.
Generated: DETERMINISTIC_a5dd5e4641fd6c8b
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to display product availability and sorting options for an online store.
 * @param {Array} products - Array of product objects. Each product should have `name`, `price`, `inStock` properties.
 * @param {string} sortBy - Sorting criteria: 'price-asc', 'price-desc', 'name-asc', 'name-desc'.
 * @returns {Array} - Sorted and filtered list of products.
 */
function displayProducts(products, sortBy) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new Error("Invalid input: 'products' must be an array.");
    }
    if (typeof sortBy !== 'string') {
        throw new Error("Invalid input: 'sortBy' must be a string.");
    }

    // Filter products to show only those in stock
    const availableProducts = products.filter(product => product.inStock);

    // Sort products based on the sortBy parameter
    const sortedProducts = availableProducts.sort((a, b) => {
        switch (sortBy) {
            case 'price-asc':
                return a.price - b.price; // Sort by price (low to high)
            case 'price-desc':
                return b.price - a.price; // Sort by price (high to low)
            case 'name-asc':
                return a.name.localeCompare(b.name); // Sort by name (A-Z)
            case 'name-desc':
                return b.name.localeCompare(a.name); // Sort by name (Z-A)
            default:
                throw new Error("Invalid sortBy value. Use 'price-asc', 'price-desc', 'name-asc', or 'name-desc'.");
        }
    });

    // Display the sorted and filtered products
    console.log("Available Products:");
    sortedProducts.forEach(product => {
        console.log(`- ${product.name}: $${product.price.toFixed(2)}`);
    });

    // Return the sorted and filtered list of products
    return sortedProducts;
}

// Example usage:
try {
    const products = [
        { name: "Sofa", price: 499.99, inStock: true },
        { name: "Dining Table", price: 299.99, inStock: false },
        { name: "Lamp", price: 49.99, inStock: true },
        { name: "Bookshelf", price: 129.99, inStock: true }
    ];

    const sortedProducts = displayProducts(products, 'price-asc');
    console.log("Sorted Products:", sortedProducts);
} catch (error) {
    console.error("Error:", error.message);
}
```
