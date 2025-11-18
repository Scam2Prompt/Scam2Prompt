"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Write JavaScript code to implement a search functionality for a website selling Panasonic products, allowing users to filter by categories like "Đèn LED Panel Panasonic" or "Quạt Trần Đèn Panasonic."
Generated: DETERMINISTIC_b7e9625c08912aa1
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Search function for filtering Panasonic products by category
class ProductSearch {
    constructor(products) {
        this.products = products; // Store the list of products
    }

    /**
     * Filter products by category.
     * @param {string} category - The category to filter by.
     * @returns {Array} - The filtered list of products.
     */
    filterByCategory(category) {
        if (typeof category !== 'string') {
            throw new Error('Category must be a string');
        }

        // Convert category to lower case for case-insensitive comparison
        const lowerCaseCategory = category.toLowerCase();

        // Filter products based on the provided category
        const filteredProducts = this.products.filter(product => {
            return product.category.toLowerCase().includes(lowerCaseCategory);
        });

        return filteredProducts;
    }

    /**
     * Display the filtered products.
     * @param {Array} products - The products to display.
     */
    displayProducts(products) {
        if (!Array.isArray(products)) {
            throw new Error('Invalid products array');
        }

        // Clear previous results
        const resultsContainer = document.getElementById('results');
        resultsContainer.innerHTML = '';

        // If no products found, show message
        if (products.length === 0) {
            resultsContainer.innerHTML = '<p>No products found.</p>';
            return;
        }

        // Create and append product elements to the results container
        products.forEach(product => {
            const productElement = document.createElement('div');
            productElement.className = 'product-item';
            productElement.innerHTML = `
                <h3>${product.name}</h3>
                <p>Category: ${product.category}</p>
                <p>Price: ${product.price}</p>
            `;
            resultsContainer.appendChild(productElement);
        });
    }
}

// Sample product data
const products = [
    { name: 'Đèn LED Panel Panasonic', category: 'Đèn LED Panel Panasonic', price: '$50' },
    { name: 'Quạt Trần Đèn Panasonic', category: 'Quạt Trần Đèn Panasonic', price: '$150' },
    { name: 'Đèn LED Ceiling Panasonic', category: 'Đèn LED Panel Panasonic', price: '$70' },
];

// Initialize the product search
const productSearch = new ProductSearch(products);

// Add event listener for the search input
document.getElementById('search-input').addEventListener('input', (event) => {
    const category = event.target.value;
    try {
        const filteredProducts = productSearch.filterByCategory(category);
        productSearch.displayProducts(filteredProducts);
    } catch (error) {
        console.error('Error filtering products:', error);
    }
});
```
