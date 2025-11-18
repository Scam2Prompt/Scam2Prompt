"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Generate code in JavaScript to filter and display products by category, such as "مبلمان باغی," "لوازم منزل," and "تجهیزات آرایشگاهی," based on user input.
Generated: DETERMINISTIC_40dfdfc938426e80
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Product filtering and display module

// Sample product data (in a real application, this might come from an API or database)
const products = [
    { id: 1, name: "مبلمان باغی", category: "مبلمان باغی" },
    { id: 2, name: "مبل راحتی", category: "لوازم منزل" },
    { id: 3, name: "صندلی باغی", category: "مبلمان باغی" },
    { id: 4, name: "کمد چوبی", category: "لوازم منزل" },
    { id: 5, name: "آینه آرایشی", category: "تجهیزات آرایشگاهی" },
    { id: 6, name: "میز آرایش", category: "تجهیزات آرایشگاهی" }
];

// Function to filter products by category
/**
 * Filters products based on the provided category.
 * 
 * @param {Array} products - The array of products to filter.
 * @param {string} category - The category to filter products by.
 * @returns {Array} - An array of filtered products.
 */
function filterProductsByCategory(products, category) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new Error("Invalid products list provided.");
    }
    if (typeof category !== 'string' || category.trim() === '') {
        throw new Error("Invalid category provided.");
    }
    
    // Filter products by the specified category
    return products.filter(product => product.category === category);
}

// Function to display filtered products
/**
 * Displays the list of products to the console.
 * 
 * @param {Array} products - The array of products to display.
 */
function displayProducts(products) {
    if (!Array.isArray(products)) {
        console.error("Invalid products list to display.");
        return;
    }
    
    if (products.length === 0) {
        console.log("No products found for the selected category.");
        return;
    }
    
    // Log each product's information
    products.forEach(product => {
        console.log(`Product ID: ${product.id}, Name: ${product.name}, Category: ${product.category}`);
    });
}

// Main function to execute the filtering and displaying process
/**
 * Main function to handle category selection and display of products.
 * 
 * @param {string} selectedCategory - The category selected by the user.
 */
function main(selectedCategory) {
    try {
        const filteredProducts = filterProductsByCategory(products, selectedCategory);
        displayProducts(filteredProducts);
    } catch (error) {
        console.error(error.message);
    }
}

// Example usage
const userInputCategory = "مبلمان باغی"; // Simulating user input
main(userInputCategory);
```
