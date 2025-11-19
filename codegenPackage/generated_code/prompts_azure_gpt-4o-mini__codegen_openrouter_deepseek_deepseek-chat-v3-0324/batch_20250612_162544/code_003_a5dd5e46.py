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
 * Displays product availability and sorting options for an online home goods store.
 * @param {Array} products - Array of product objects
 * @param {Object} options - Configuration options
 * @param {boolean} options.showAvailability - Whether to display availability status
 * @param {Array} options.sortOptions - Available sorting options
 * @returns {Object} - Object containing filtered products and UI elements
 */
function displayProductCatalog(products, options = {}) {
    // Default options
    const defaultOptions = {
        showAvailability: true,
        sortOptions: [
            { value: 'price-asc', label: 'Price: Low to High' },
            { value: 'price-desc', label: 'Price: High to Low' },
            { value: 'name-asc', label: 'Name: A to Z' },
            { value: 'name-desc', label: 'Name: Z to A' }
        ]
    };

    // Merge provided options with defaults
    const config = { ...defaultOptions, ...options };

    // Validate products array
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }

    // Create UI elements
    const uiElements = {
        sortDropdown: createSortDropdown(config.sortOptions),
        availabilityFilter: config.showAvailability ? createAvailabilityFilter() : null,
        productContainer: document.createElement('div')
    };

    // Initialize with default sorting
    let sortedProducts = [...products];
    sortProducts(sortedProducts, 'price-asc');

    // Return public API
    return {
        products: sortedProducts,
        uiElements,
        /**
         * Sort products by given criteria
         * @param {string} sortBy - Sorting criteria
         */
        sortBy: (sortBy) => {
            sortProducts(sortedProducts, sortBy);
        },
        /**
         * Filter products by availability
         * @param {boolean} inStockOnly - Whether to show only in-stock items
         */
        filterByAvailability: (inStockOnly) => {
            return inStockOnly 
                ? sortedProducts.filter(product => product.inStock) 
                : [...sortedProducts];
        }
    };

    // Helper functions
    function createSortDropdown(sortOptions) {
        const dropdown = document.createElement('select');
        dropdown.className = 'product-sort-dropdown';
        
        sortOptions.forEach(option => {
            const optElement = document.createElement('option');
            optElement.value = option.value;
            optElement.textContent = option.label;
            dropdown.appendChild(optElement);
        });

        dropdown.addEventListener('change', (e) => {
            sortProducts(sortedProducts, e.target.value);
        });

        return dropdown;
    }

    function createAvailabilityFilter() {
        const container = document.createElement('div');
        container.className = 'availability-filter';
        
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = 'in-stock-only';
        
        const label = document.createElement('label');
        label.htmlFor = 'in-stock-only';
        label.textContent = 'Show only in-stock items';
        
        container.appendChild(checkbox);
        container.appendChild(label);
        
        return container;
    }

    function sortProducts(products, sortBy) {
        switch (sortBy) {
            case 'price-asc':
                products.sort((a, b) => a.price - b.price);
                break;
            case 'price-desc':
                products.sort((a, b) => b.price - a.price);
                break;
            case 'name-asc':
                products.sort((a, b) => a.name.localeCompare(b.name));
                break;
            case 'name-desc':
                products.sort((a, b) => b.name.localeCompare(a.name));
                break;
            default:
                console.warn(`Unknown sort option: ${sortBy}`);
        }
    }
}

// Example usage:
/*
const products = [
    { id: 1, name: 'Throw Pillow', price: 24.99, inStock: true },
    { id: 2, name: 'Ceramic Vase', price: 45.50, inStock: false },
    { id: 3, name: 'Wooden Coffee Table', price: 199.99, inStock: true }
];

const catalog = displayProductCatalog(products, {
    showAvailability: true,
    sortOptions: [
        { value: 'price-asc', label: 'Price: Low to High' },
        { value: 'name-asc', label: 'Name: A to Z' }
    ]
});

document.body.appendChild(catalog.uiElements.sortDropdown);
document.body.appendChild(catalog.uiElements.availabilityFilter);
*/
```
