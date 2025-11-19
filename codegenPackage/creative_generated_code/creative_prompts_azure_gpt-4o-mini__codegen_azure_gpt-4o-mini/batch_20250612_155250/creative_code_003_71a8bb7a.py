"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Develop a function in JavaScript that filters and displays best-selling products from the Brands Outlet based on user-selected categories like men, women, and kids.
Generated: DETERMINISTIC_71a8bb7a84485450
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays best-selling products from the Brands Outlet 
 * based on user-selected categories: men, women, and kids.
 * 
 * @param {Array} products - The array of products to filter.
 * @param {string} category - The selected category to filter products by.
 * @returns {Array} - An array of filtered best-selling products.
 * 
 * @throws {Error} - Throws an error if the category is invalid or products are not provided.
 */
function filterBestSellingProducts(products, category) {
    // Define valid categories
    const validCategories = ['men', 'women', 'kids'];

    // Validate input
    if (!Array.isArray(products)) {
        throw new Error('The products parameter must be an array.');
    }
    if (!validCategories.includes(category)) {
        throw new Error('Invalid category selected. Please choose from: men, women, or kids.');
    }

    // Filter products based on category and best-selling status
    const filteredProducts = products.filter(product => 
        product.category === category && product.isBestSeller
    );

    return filteredProducts;
}

/**
 * Displays the filtered products on the webpage.
 * 
 * @param {Array} products - The array of products to display.
 */
function displayProducts(products) {
    const productContainer = document.getElementById('product-container');
    productContainer.innerHTML = ''; // Clear existing products

    if (products.length === 0) {
        productContainer.innerHTML = '<p>No best-selling products found.</p>';
        return;
    }

    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.className = 'product-item';
        productElement.innerHTML = `
            <h3>${product.name}</h3>
            <p>Price: ${product.price}</p>
            <p>Category: ${product.category}</p>
        `;
        productContainer.appendChild(productElement);
    });
}

/**
 * Main function to handle the filtering and displaying of products 
 * based on user selection.
 * 
 * @param {Array} products - The initial array of products.
 */
function handleProductFiltering(products) {
    const categorySelect = document.getElementById('category-select');

    categorySelect.addEventListener('change', () => {
        const selectedCategory = categorySelect.value;

        try {
            const bestSellingProducts = filterBestSellingProducts(products, selectedCategory);
            displayProducts(bestSellingProducts);
        } catch (error) {
            console.error(error.message);
            alert(error.message); // Notify user of the error
        }
    });
}

// Example usage
const products = [
    { name: 'Men\'s Jacket', price: 79.99, category: 'men', isBestSeller: true },
    { name: 'Women\'s Dress', price: 49.99, category: 'women', isBestSeller: false },
    { name: 'Kids\' Shoes', price: 29.99, category: 'kids', isBestSeller: true },
    { name: 'Women\'s Sneakers', price: 89.99, category: 'women', isBestSeller: true },
];

// Initialize the product filtering functionality
handleProductFiltering(products);
```
