"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate a JavaScript code to create a simple product filter for a sports equipment website, allowing users to filter by sport (e.g., beach volleyball, handball, etc.) and product type (e.g., balls, shoes, etc.).
Generated: DETERMINISTIC_4fc72dbbefdbfdda
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Filter for Sports Equipment Website
 * Allows filtering by sport and product type
 */

// Product data
const products = [
    { id: 1, name: 'Beach Volleyball', sport: 'beach-volleyball', type: 'balls', price: 29.99 },
    { id: 2, name: 'Handball Shoes', sport: 'handball', type: 'shoes', price: 89.99 },
    { id: 3, name: 'Handball Ball', sport: 'handball', type: 'balls', price: 24.99 },
    { id: 4, name: 'Volleyball Knee Pads', sport: 'volleyball', type: 'accessories', price: 19.99 },
    { id: 5, name: 'Beach Volleyball Net', sport: 'beach-volleyball', type: 'nets', price: 59.99 },
    { id: 6, name: 'Running Shoes', sport: 'running', type: 'shoes', price: 79.99 },
];

// DOM elements
const sportFilter = document.getElementById('sport-filter');
const typeFilter = document.getElementById('type-filter');
const productContainer = document.getElementById('product-container');
const resetButton = document.getElementById('reset-filters');

// Initialize the filter
document.addEventListener('DOMContentLoaded', () => {
    initializeFilters();
    renderProducts(products);
    setupEventListeners();
});

/**
 * Initialize filter dropdowns with available options
 */
function initializeFilters() {
    try {
        // Get unique sports
        const sports = [...new Set(products.map(product => product.sport))];
        sports.forEach(sport => {
            const option = document.createElement('option');
            option.value = sport;
            option.textContent = sport.split('-').map(word => 
                word.charAt(0).toUpperCase() + word.slice(1)
            ).join(' ');
            sportFilter.appendChild(option);
        });

        // Get unique types
        const types = [...new Set(products.map(product => product.type))];
        types.forEach(type => {
            const option = document.createElement('option');
            option.value = type;
            option.textContent = type.charAt(0).toUpperCase() + type.slice(1);
            typeFilter.appendChild(option);
        });
    } catch (error) {
        console.error('Error initializing filters:', error);
    }
}

/**
 * Set up event listeners for filters and reset button
 */
function setupEventListeners() {
    sportFilter.addEventListener('change', applyFilters);
    typeFilter.addEventListener('change', applyFilters);
    resetButton.addEventListener('click', resetFilters);
}

/**
 * Apply filters based on user selection
 */
function applyFilters() {
    try {
        const selectedSport = sportFilter.value;
        const selectedType = typeFilter.value;

        const filteredProducts = products.filter(product => {
            const sportMatch = selectedSport === 'all' || product.sport === selectedSport;
            const typeMatch = selectedType === 'all' || product.type === selectedType;
            return sportMatch && typeMatch;
        });

        renderProducts(filteredProducts);
    } catch (error) {
        console.error('Error applying filters:', error);
    }
}

/**
 * Reset all filters to default state
 */
function resetFilters() {
    try {
        sportFilter.value = 'all';
        typeFilter.value = 'all';
        renderProducts(products);
    } catch (error) {
        console.error('Error resetting filters:', error);
    }
}

/**
 * Render products to the DOM
 * @param {Array} productsToRender - Array of product objects to display
 */
function renderProducts(productsToRender) {
    try {
        productContainer.innerHTML = '';

        if (productsToRender.length === 0) {
            productContainer.innerHTML = '<p class="no-results">No products match your filters.</p>';
            return;
        }

        productsToRender.forEach(product => {
            const productElement = document.createElement('div');
            productElement.className = 'product-card';
            productElement.innerHTML = `
                <h3>${product.name}</h3>
                <p><strong>Sport:</strong> ${product.sport.split('-').map(word => 
                    word.charAt(0).toUpperCase() + word.slice(1)
                ).join(' ')}</p>
                <p><strong>Type:</strong> ${product.type.charAt(0).toUpperCase() + product.type.slice(1)}</p>
                <p><strong>Price:</strong> $${product.price.toFixed(2)}</p>
            `;
            productContainer.appendChild(productElement);
        });
    } catch (error) {
        console.error('Error rendering products:', error);
    }
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sports Equipment Filter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .filters {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }
        select {
            padding: 8px;
            font-size: 16px;
        }
        button {
            padding: 8px 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .product-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }
        .product-card {
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 5px;
        }
        .no-results {
            grid-column: 1 / -1;
            text-align: center;
            font-size: 18px;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Sports Equipment</h1>
    
    <div class="filters">
        <select id="sport-filter">
            <option value="all">All Sports</option>
        </select>
        
        <select id="type-filter">
            <option value="all">All Types</option>
        </select>
        
        <button id="reset-filters">Reset Filters</button>
    </div>
    
    <div id="product-container"></div>

    <script src="product-filter.js"></script>
</body>
</html>
```
