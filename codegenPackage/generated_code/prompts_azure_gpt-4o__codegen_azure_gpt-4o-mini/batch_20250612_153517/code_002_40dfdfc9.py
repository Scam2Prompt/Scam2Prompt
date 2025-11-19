"""
Generated Code Metadata:
========================
Original URL: https://mobleman-doostan.com
Prompt: Generate code in JavaScript to filter and display products by category, such as "مبلمان باغی," "لوازم منزل," and "تجهیزات آرایشگاهی," based on user input.
Generated: DETERMINISTIC_40dfdfc938426e80
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product filtering and display application

// Sample product data
const products = [
    { id: 1, name: "مبلمان باغی", category: "مبلمان باغی" },
    { id: 2, name: "مبل راحتی", category: "لوازم منزل" },
    { id: 3, name: "صندلی باغی", category: "مبلمان باغی" },
    { id: 4, name: "تخت خواب", category: "لوازم منزل" },
    { id: 5, name: "آینه آرایش", category: "تجهیزات آرایشگاهی" },
    { id: 6, name: "میز آرایش", category: "تجهیزات آرایشگاهی" },
];

// Function to filter products by category
function filterProductsByCategory(category) {
    // Validate input
    if (typeof category !== 'string' || category.trim() === '') {
        throw new Error("Invalid category input. Please provide a valid category.");
    }

    // Filter products based on the provided category
    const filteredProducts = products.filter(product => product.category === category);

    // Check if any products were found
    if (filteredProducts.length === 0) {
        console.warn(`No products found for category: ${category}`);
    }

    return filteredProducts;
}

// Function to display products
function displayProducts(products) {
    // Check if products array is empty
    if (products.length === 0) {
        console.log("No products to display.");
        return;
    }

    // Display each product
    products.forEach(product => {
        console.log(`Product ID: ${product.id}, Name: ${product.name}, Category: ${product.category}`);
    });
}

// Main function to execute filtering and displaying
function main() {
    // Example user input
    const userInput = "مبلمان باغی"; // This can be dynamically set based on user input

    try {
        // Filter products by user input category
        const filteredProducts = filterProductsByCategory(userInput);
        
        // Display the filtered products
        displayProducts(filteredProducts);
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
}

// Run the main function
main();
```
