"""
Generated Code Metadata:
========================
Original URL: https://games-home-plays-galla.weebly.com
Prompt: Write a JavaScript code snippet to implement a product filtering system on an e-commerce website like Baby Calçados, allowing customers to filter products by category, brand, and price.
Generated: DETERMINISTIC_a1e7f4b42e0a37f7
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Filtering System for E-commerce
 * Filters products by category, brand, and price range
 */

class ProductFilter {
  constructor(products) {
    this.products = products || [];
    this.filters = {
      category: null,
      brand: null,
      minPrice: null,
      maxPrice: null
    };
  }

  /**
   * Apply all active filters to products
   * @returns {Array} Filtered products
   */
  applyFilters() {
    return this.products.filter(product => {
      const matchesCategory = !this.filters.category || 
                             product.category === this.filters.category;
      const matchesBrand = !this.filters.brand || 
                          product.brand === this.filters.brand;
      const matchesMinPrice = !this.filters.minPrice || 
                             product.price >= this.filters.minPrice;
      const matchesMaxPrice = !this.filters.maxPrice || 
                             product.price <= this.filters.maxPrice;

      return matchesCategory && matchesBrand && matchesMinPrice && matchesMaxPrice;
    });
  }

  /**
   * Set category filter
   * @param {string} category - Category to filter by
   */
  setCategoryFilter(category) {
    this.filters.category = category || null;
  }

  /**
   * Set brand filter
   * @param {string} brand - Brand to filter by
   */
  setBrandFilter(brand) {
    this.filters.brand = brand || null;
  }

  /**
   * Set price range filter
   * @param {number} min - Minimum price
   * @param {number} max - Maximum price
   */
  setPriceFilter(min, max) {
    this.filters.minPrice = typeof min === 'number' ? min : null;
    this.filters.maxPrice = typeof max === 'number' ? max : null;
  }

  /**
   * Reset all filters to default values
   */
  resetFilters() {
    this.filters = {
      category: null,
      brand: null,
      minPrice: null,
      maxPrice: null
    };
  }
}

// Example usage with UI event handlers
document.addEventListener('DOMContentLoaded', () => {
  // Sample product data (in a real app, this would come from an API)
  const sampleProducts = [
    { id: 1, name: 'Product 1', category: 'shoes', brand: 'Nike', price: 59.99 },
    { id: 2, name: 'Product 2', category: 'sandals', brand: 'Adidas', price: 39.99 },
    { id: 3, name: 'Product 3', category: 'shoes', brand: 'Puma', price: 49.99 },
    { id: 4, name: 'Product 4', category: 'boots', brand: 'Nike', price: 79.99 }
  ];

  const filter = new ProductFilter(sampleProducts);
  const resultsContainer = document.getElementById('product-results');

  /**
   * Update and display filtered products
   */
  function updateResults() {
    const filteredProducts = filter.applyFilters();
    displayProducts(filteredProducts);
  }

  /**
   * Display products in the UI
   * @param {Array} products - Products to display
   */
  function displayProducts(products) {
    resultsContainer.innerHTML = '';
    
    if (products.length === 0) {
      resultsContainer.innerHTML = '<p>No products match your filters.</p>';
      return;
    }

    products.forEach(product => {
      const productElement = document.createElement('div');
      productElement.className = 'product-item';
      productElement.innerHTML = `
        <h3>${product.name}</h3>
        <p>Brand: ${product.brand}</p>
        <p>Category: ${product.category}</p>
        <p>Price: $${product.price.toFixed(2)}</p>
      `;
      resultsContainer.appendChild(productElement);
    });
  }

  // Event listeners for filter controls
  document.getElementById('category-filter').addEventListener('change', (e) => {
    filter.setCategoryFilter(e.target.value);
    updateResults();
  });

  document.getElementById('brand-filter').addEventListener('change', (e) => {
    filter.setBrandFilter(e.target.value);
    updateResults();
  });

  document.getElementById('price-filter-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const minPrice = parseFloat(document.getElementById('min-price').value);
    const maxPrice = parseFloat(document.getElementById('max-price').value);
    filter.setPriceFilter(minPrice, maxPrice);
    updateResults();
  });

  document.getElementById('reset-filters').addEventListener('click', () => {
    filter.resetFilters();
    document.getElementById('category-filter').value = '';
    document.getElementById('brand-filter').value = '';
    document.getElementById('min-price').value = '';
    document.getElementById('max-price').value = '';
    updateResults();
  });

  // Initial display
  updateResults();
});
```
