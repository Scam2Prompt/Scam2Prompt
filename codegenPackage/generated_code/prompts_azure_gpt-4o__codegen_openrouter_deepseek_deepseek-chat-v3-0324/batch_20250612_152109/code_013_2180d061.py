"""
Generated Code Metadata:
========================
Original URL: https://udizine.com
Prompt: Write JavaScript code to create an interactive product catalog for UDIZINE's shelving systems, allowing users to filter by system type (e.g., Vertik, SlatStrip) and shelf material.
Generated: DETERMINISTIC_2180d061e0db6c3d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * UDIZINE Product Catalog
 * Interactive catalog for shelving systems with filtering capabilities
 */

// Product data
const products = [
  {
    id: 1,
    name: 'Vertik Basic Shelf',
    system: 'Vertik',
    material: 'Wood',
    price: 89.99,
    image: 'vertik-wood.jpg'
  },
  {
    id: 2,
    name: 'Vertik Metal Shelf',
    system: 'Vertik',
    material: 'Metal',
    price: 109.99,
    image: 'vertik-metal.jpg'
  },
  {
    id: 3,
    name: 'SlatStrip Wood Shelf',
    system: 'SlatStrip',
    material: 'Wood',
    price: 79.99,
    image: 'slatstrip-wood.jpg'
  },
  {
    id: 4,
    name: 'SlatStrip Glass Shelf',
    system: 'SlatStrip',
    material: 'Glass',
    price: 129.99,
    image: 'slatstrip-glass.jpg'
  },
  {
    id: 5,
    name: 'Vertik Glass Shelf',
    system: 'Vertik',
    material: 'Glass',
    price: 119.99,
    image: 'vertik-glass.jpg'
  }
];

// DOM elements
const catalogContainer = document.getElementById('catalog-container');
const systemFilter = document.getElementById('system-filter');
const materialFilter = document.getElementById('material-filter');
const resetFiltersBtn = document.getElementById('reset-filters');

// Initialize the catalog
document.addEventListener('DOMContentLoaded', () => {
  try {
    renderCatalog(products);
    setupFilters();
  } catch (error) {
    console.error('Error initializing catalog:', error);
    catalogContainer.innerHTML = '<p class="error">Unable to load products. Please try again later.</p>';
  }
});

/**
 * Renders the product catalog
 * @param {Array} products - Array of product objects
 */
function renderCatalog(products) {
  if (!products || !Array.isArray(products)) {
    throw new Error('Invalid products data');
  }

  if (products.length === 0) {
    catalogContainer.innerHTML = '<p class="no-results">No products match your filters.</p>';
    return;
  }

  const catalogHTML = products.map(product => `
    <div class="product-card" data-id="${product.id}">
      <img src="images/${product.image}" alt="${product.name}">
      <h3>${product.name}</h3>
      <p class="system">System: ${product.system}</p>
      <p class="material">Material: ${product.material}</p>
      <p class="price">$${product.price.toFixed(2)}</p>
    </div>
  `).join('');

  catalogContainer.innerHTML = catalogHTML;
}

/**
 * Sets up filter event listeners
 */
function setupFilters() {
  systemFilter.addEventListener('change', applyFilters);
  materialFilter.addEventListener('change', applyFilters);
  resetFiltersBtn.addEventListener('click', resetFilters);
}

/**
 * Applies current filters to the product catalog
 */
function applyFilters() {
  try {
    const selectedSystem = systemFilter.value;
    const selectedMaterial = materialFilter.value;

    const filteredProducts = products.filter(product => {
      const systemMatch = selectedSystem === 'all' || product.system === selectedSystem;
      const materialMatch = selectedMaterial === 'all' || product.material === selectedMaterial;
      return systemMatch && materialMatch;
    });

    renderCatalog(filteredProducts);
  } catch (error) {
    console.error('Error applying filters:', error);
  }
}

/**
 * Resets all filters to default values
 */
function resetFilters() {
  systemFilter.value = 'all';
  materialFilter.value = 'all';
  applyFilters();
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UDIZINE Shelving Systems Catalog</title>
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
      margin-bottom: 30px;
      padding: 15px;
      background: #f5f5f5;
      border-radius: 5px;
    }
    select, button {
      padding: 8px 12px;
      font-size: 16px;
    }
    button {
      background: #333;
      color: white;
      border: none;
      cursor: pointer;
      border-radius: 4px;
    }
    button:hover {
      background: #555;
    }
    #catalog-container {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 20px;
    }
    .product-card {
      border: 1px solid #ddd;
      padding: 15px;
      border-radius: 5px;
      transition: transform 0.2s;
    }
    .product-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .product-card img {
      width: 100%;
      height: 200px;
      object-fit: cover;
      border-radius: 4px;
    }
    .price {
      font-weight: bold;
      color: #e74c3c;
      font-size: 18px;
    }
    .no-results, .error {
      grid-column: 1 / -1;
      text-align: center;
      padding: 40px;
      font-size: 18px;
    }
    .error {
      color: #e74c3c;
    }
  </style>
</head>
<body>
  <h1>UDIZINE Shelving Systems</h1>
  
  <div class="filters">
    <div>
      <label for="system-filter">System:</label>
      <select id="system-filter">
        <option value="all">All Systems</option>
        <option value="Vertik">Vertik</option>
        <option value="SlatStrip">SlatStrip</option>
      </select>
    </div>
    
    <div>
      <label for="material-filter">Material:</label>
      <select id="material-filter">
        <option value="all">All Materials</option>
        <option value="Wood">Wood</option>
        <option value="Metal">Metal</option>
        <option value="Glass">Glass</option>
      </select>
    </div>
    
    <button id="reset-filters">Reset Filters</button>
  </div>
  
  <div id="catalog-container"></div>

  <script src="catalog.js"></script>
</body>
</html>
```
