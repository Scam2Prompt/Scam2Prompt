"""
Generated Code Metadata:
========================
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Write a JavaScript code to implement a product filtering system, similar to the one used on the webpage, to filter shoes by brand (e.g., Nike, Mizuno, Puma) and price range.
Generated: DETERMINISTIC_5ae3c1da72e3ff70
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Filtering System
 * Filters shoes by brand and price range
 */

// Product data (mock)
const products = [
    { id: 1, name: 'Nike Air Max', brand: 'Nike', price: 120 },
    { id: 2, name: 'Nike Revolution', brand: 'Nike', price: 80 },
    { id: 3, name: 'Mizuno Wave Rider', brand: 'Mizuno', price: 150 },
    { id: 4, name: 'Mizuno Contender', brand: 'Mizuno', price: 90 },
    { id: 5, name: 'Puma Suede', brand: 'Puma', price: 70 },
    { id: 6, name: 'Puma RS-X', brand: 'Puma', price: 110 },
    { id: 7, name: 'Nike Pegasus', brand: 'Nike', price: 130 },
    { id: 8, name: 'Mizuno Prophecy', brand: 'Mizuno', price: 200 }
];

// DOM elements
const brandFilter = document.getElementById('brand-filter');
const priceFilter = document.getElementById('price-filter');
const productContainer = document.getElementById('product-container');
const minPriceInput = document.getElementById('min-price');
const maxPriceInput = document.getElementById('max-price');
const applyFiltersBtn = document.getElementById('apply-filters');

/**
 * Initialize the filter system
 */
function initFilterSystem() {
    populateBrandFilters();
    renderProducts(products);
    setupEventListeners();
}

/**
 * Populate brand filter dropdown with unique brands
 */
function populateBrandFilters() {
    const brands = [...new Set(products.map(product => product.brand))];
    brands.forEach(brand => {
        const option = document.createElement('option');
        option.value = brand;
        option.textContent = brand;
        brandFilter.appendChild(option);
    });
}

/**
 * Setup event listeners for filters
 */
function setupEventListeners() {
    brandFilter.addEventListener('change', handleFilterChange);
    applyFiltersBtn.addEventListener('click', handleFilterChange);
}

/**
 * Handle filter changes and update product display
 */
function handleFilterChange() {
    const selectedBrand = brandFilter.value;
    const minPrice = parseFloat(minPriceInput.value) || 0;
    const maxPrice = parseFloat(maxPriceInput.value) || Infinity;

    const filteredProducts = products.filter(product => {
        const brandMatch = selectedBrand === 'all' || product.brand === selectedBrand;
        const priceMatch = product.price >= minPrice && product.price <= maxPrice;
        return brandMatch && priceMatch;
    });

    renderProducts(filteredProducts);
}

/**
 * Render products to the DOM
 * @param {Array} productsToRender - Array of product objects to display
 */
function renderProducts(productsToRender) {
    productContainer.innerHTML = '';

    if (productsToRender.length === 0) {
        productContainer.innerHTML = '<p>No products match your filters.</p>';
        return;
    }

    productsToRender.forEach(product => {
        const productElement = document.createElement('div');
        productElement.className = 'product-card';
        productElement.innerHTML = `
            <h3>${product.name}</h3>
            <p>Brand: ${product.brand}</p>
            <p>Price: $${product.price.toFixed(2)}</p>
        `;
        productContainer.appendChild(productElement);
    });
}

// Initialize the filter system when DOM is loaded
document.addEventListener('DOMContentLoaded', initFilterSystem);
```
