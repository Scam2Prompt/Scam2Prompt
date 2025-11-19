"""
Generated Code Metadata:
========================
Original URL: https://glisten.site
Prompt: Create a JavaScript function to filter and display iPhone cases based on color and price, inspired by the product listings on Glisten's website.
Generated: DETERMINISTIC_d3b7c2edf65ec0c2
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and displays iPhone cases based on color and price range.
 * @param {Array} products - Array of product objects to filter
 * @param {Object} filters - Filter criteria (color and price range)
 * @param {string} [filters.color] - Color to filter by (optional)
 * @param {Object} [filters.price] - Price range to filter by (optional)
 * @param {number} [filters.price.min] - Minimum price (optional)
 * @param {number} [filters.price.max] - Maximum price (optional)
 * @returns {Array} Filtered array of products
 */
function filterIPhoneCases(products, filters) {
    // Validate inputs
    if (!Array.isArray(products)) {
        throw new TypeError('Products must be an array');
    }

    if (typeof filters !== 'object' || filters === null) {
        throw new TypeError('Filters must be an object');
    }

    // Apply filters
    return products.filter(product => {
        // Check if product is an iPhone case
        if (!product.type || product.type.toLowerCase() !== 'iphone case') {
            return false;
        }

        // Check color filter if provided
        if (filters.color && product.color.toLowerCase() !== filters.color.toLowerCase()) {
            return false;
        }

        // Check price range filter if provided
        if (filters.price) {
            const price = parseFloat(product.price);
            if (isNaN(price)) {
                console.warn(`Invalid price for product ${product.id}`);
                return false;
            }

            if (filters.price.min !== undefined && price < filters.price.min) {
                return false;
            }

            if (filters.price.max !== undefined && price > filters.price.max) {
                return false;
            }
        }

        return true;
    });
}

/**
 * Displays filtered iPhone cases in the DOM
 * @param {Array} products - Array of product objects to display
 * @param {string} containerId - ID of the container element to render products in
 */
function displayFilteredCases(products, containerId) {
    // Validate inputs
    if (!Array.isArray(products)) {
        throw new TypeError('Products must be an array');
    }

    const container = document.getElementById(containerId);
    if (!container) {
        throw new Error(`Container element with ID '${containerId}' not found`);
    }

    // Clear previous results
    container.innerHTML = '';

    // Handle empty results
    if (products.length === 0) {
        container.innerHTML = '<p class="no-results">No products match your filters.</p>';
        return;
    }

    // Create product cards
    products.forEach(product => {
        const productCard = document.createElement('div');
        productCard.className = 'product-card';

        productCard.innerHTML = `
            <img src="${product.imageUrl || 'placeholder.jpg'}" alt="${product.name}" class="product-image">
            <h3 class="product-title">${product.name}</h3>
            <p class="product-color">Color: ${product.color}</p>
            <p class="product-price">$${product.price.toFixed(2)}</p>
            <button class="add-to-cart" data-id="${product.id}">Add to Cart</button>
        `;

        container.appendChild(productCard);
    });
}

/**
 * Example usage:
 * 
 * const products = [
 *     { id: 1, type: 'iPhone Case', name: 'Clear Case', color: 'Clear', price: 19.99, imageUrl: 'clear.jpg' },
 *     { id: 2, type: 'iPhone Case', name: 'Black Case', color: 'Black', price: 24.99, imageUrl: 'black.jpg' },
 *     { id: 3, type: 'iPhone Case', name: 'Blue Case', color: 'Blue', price: 29.99, imageUrl: 'blue.jpg' }
 * ];
 * 
 * const filters = {
 *     color: 'black',
 *     price: { min: 20, max: 30 }
 * };
 * 
 * try {
 *     const filteredProducts = filterIPhoneCases(products, filters);
 *     displayFilteredCases(filteredProducts, 'products-container');
 * } catch (error) {
 *     console.error('Error filtering or displaying products:', error);
 *     document.getElementById('products-container').innerHTML = 
 *         '<p class="error">Error loading products. Please try again later.</p>';
 * }
 */
```
