"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oromaticas.com
Prompt: Create a JavaScript function to filter and display products based on their categories, such as "Aromáticas" and "Hortalizas," as seen on the Oromáticas website.
Generated: DETERMINISTIC_e827fe646622cc26
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays products based on selected categories.
 * 
 * This function takes an array of products and a category string as input,
 * filters the products that belong to the specified category, and displays
 * them in the console. If no products are found, it alerts the user.
 * 
 * @param {Array} products - An array of product objects, each containing a name and a category.
 * @param {string} selectedCategory - The category to filter products by.
 */
function filterAndDisplayProducts(products, selectedCategory) {
    // Validate inputs
    if (!Array.isArray(products)) {
        throw new TypeError('The first argument must be an array of products.');
    }
    if (typeof selectedCategory !== 'string') {
        throw new TypeError('The second argument must be a string representing the category.');
    }

    // Filter products based on the selected category
    const filteredProducts = products.filter(product => product.category === selectedCategory);

    // Check if there are any products in the filtered list
    if (filteredProducts.length === 0) {
        alert(`No products found in the category: ${selectedCategory}`);
        return;
    }

    // Display the filtered products
    console.log(`Products in the category: ${selectedCategory}`);
    filteredProducts.forEach(product => {
        console.log(`- ${product.name}`);
    });
}

// Example usage
const products = [
    { name: 'Rosemary', category: 'Aromáticas' },
    { name: 'Thyme', category: 'Aromáticas' },
    { name: 'Carrot', category: 'Hortalizas' },
    { name: 'Lettuce', category: 'Hortalizas' },
];

try {
    filterAndDisplayProducts(products, 'Aromáticas');
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
