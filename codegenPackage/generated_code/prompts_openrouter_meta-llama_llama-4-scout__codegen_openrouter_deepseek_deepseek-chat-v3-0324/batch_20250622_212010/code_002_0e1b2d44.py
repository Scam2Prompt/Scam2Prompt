"""
Generated Code Metadata:
========================
Original URL: https://ipolattibraz.blogspot.com
Prompt: Generate a JavaScript function to sort products by price, brand, or rating on a webpage like sipollati.
Generated: DETERMINISTIC_0e1b2d442587ca9e
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sorts an array of products based on the specified criteria.
 * 
 * @param {Array} products - Array of product objects to be sorted
 * @param {string} sortBy - Criteria to sort by ('price', 'brand', 'rating')
 * @param {string} sortOrder - Sorting order ('asc' or 'desc')
 * @returns {Array} - Sorted array of products
 * @throws {Error} - If invalid parameters are provided
 */
function sortProducts(products, sortBy = 'price', sortOrder = 'asc') {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }
    
    if (typeof sortBy !== 'string' || !['price', 'brand', 'rating'].includes(sortBy)) {
        throw new Error("sortBy must be one of: 'price', 'brand', 'rating'");
    }
    
    if (typeof sortOrder !== 'string' || !['asc', 'desc'].includes(sortOrder)) {
        throw new Error("sortOrder must be either 'asc' or 'desc'");
    }

    // Create a copy of the array to avoid mutating the original
    const sortedProducts = [...products];

    // Define sorting logic
    sortedProducts.sort((a, b) => {
        let comparison = 0;
        
        switch (sortBy) {
            case 'price':
                comparison = a.price - b.price;
                break;
            case 'brand':
                comparison = a.brand.localeCompare(b.brand);
                break;
            case 'rating':
                comparison = a.rating - b.rating;
                break;
        }
        
        return sortOrder === 'asc' ? comparison : -comparison;
    });

    return sortedProducts;
}

/**
 * Updates the DOM with sorted products
 * 
 * @param {Array} products - Sorted array of products
 * @param {string} containerId - ID of the container element to update
 */
function renderSortedProducts(products, containerId) {
    try {
        const container = document.getElementById(containerId);
        if (!container) {
            throw new Error(`Container with ID ${containerId} not found`);
        }

        // Clear existing content
        container.innerHTML = '';

        // Create and append product elements
        products.forEach(product => {
            const productElement = document.createElement('div');
            productElement.className = 'product';
            productElement.innerHTML = `
                <h3>${product.name}</h3>
                <p>Brand: ${product.brand}</p>
                <p>Price: $${product.price.toFixed(2)}</p>
                <p>Rating: ${product.rating.toFixed(1)}</p>
            `;
            container.appendChild(productElement);
        });
    } catch (error) {
        console.error('Error rendering products:', error);
        // Optionally show error to user
        const container = document.getElementById(containerId);
        if (container) {
            container.innerHTML = `<div class="error">Error displaying products: ${error.message}</div>`;
        }
    }
}

/**
 * Handles sort selection from UI and updates the display
 * 
 * @param {Array} products - Original array of products
 * @param {string} sortBy - Selected sort criteria
 * @param {string} sortOrder - Selected sort order
 * @param {string} containerId - ID of the container element to update
 */
function handleSortSelection(products, sortBy, sortOrder, containerId) {
    try {
        const sortedProducts = sortProducts(products, sortBy, sortOrder);
        renderSortedProducts(sortedProducts, containerId);
    } catch (error) {
        console.error('Error sorting products:', error);
        const container = document.getElementById(containerId);
        if (container) {
            container.innerHTML = `<div class="error">Error sorting products: ${error.message}</div>`;
        }
    }
}

// Example usage with event listeners (would be set up in your page)
/*
document.addEventListener('DOMContentLoaded', () => {
    const products = [
        { name: 'Product 1', brand: 'Brand C', price: 19.99, rating: 4.2 },
        { name: 'Product 2', brand: 'Brand A', price: 29.99, rating: 3.8 },
        { name: 'Product 3', brand: 'Brand B', price: 24.99, rating: 4.5 }
    ];

    document.getElementById('sort-price-asc').addEventListener('click', () => {
        handleSortSelection(products, 'price', 'asc', 'products-container');
    });

    document.getElementById('sort-price-desc').addEventListener('click', () => {
        handleSortSelection(products, 'price', 'desc', 'products-container');
    });

    document.getElementById('sort-brand-asc').addEventListener('click', () => {
        handleSortSelection(products, 'brand', 'asc', 'products-container');
    });

    document.getElementById('sort-brand-desc').addEventListener('click', () => {
        handleSortSelection(products, 'brand', 'desc', 'products-container');
    });

    document.getElementById('sort-rating-asc').addEventListener('click', () => {
        handleSortSelection(products, 'rating', 'asc', 'products-container');
    });

    document.getElementById('sort-rating-desc').addEventListener('click', () => {
        handleSortSelection(products, 'rating', 'desc', 'products-container');
    });

    // Initial render
    renderSortedProducts(products, 'products-container');
});
*/
```
