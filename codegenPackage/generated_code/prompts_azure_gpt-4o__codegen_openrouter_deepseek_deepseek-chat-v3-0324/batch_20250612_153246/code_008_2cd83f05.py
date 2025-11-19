"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: Write JavaScript code to implement a search functionality for the "duct-split.com" website, allowing users to filter Gree air conditioners by cooling capacity, inverter type, and price range.
Generated: DETERMINISTIC_2cd83f058d359002
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Search functionality for Gree air conditioners on duct-split.com
 * Filters products by cooling capacity, inverter type, and price range
 */

class GreeACSearch {
  constructor(products) {
    this.products = products || [];
    this.filters = {
      coolingCapacity: null,
      inverterType: null,
      priceRange: { min: null, max: null }
    };
  }

  /**
   * Apply all active filters to products
   * @returns {Array} Filtered products
   */
  applyFilters() {
    return this.products.filter(product => {
      return (
        this._matchesCoolingCapacity(product) &&
        this._matchesInverterType(product) &&
        this._matchesPriceRange(product)
      );
    });
  }

  /**
   * Set cooling capacity filter
   * @param {string} capacity - Cooling capacity value (e.g., '1.5HP')
   */
  setCoolingCapacity(capacity) {
    this.filters.coolingCapacity = capacity || null;
  }

  /**
   * Set inverter type filter
   * @param {string} type - Inverter type ('Inverter' or 'Non-Inverter')
   */
  setInverterType(type) {
    this.filters.inverterType = type || null;
  }

  /**
   * Set price range filter
   * @param {number} min - Minimum price
   * @param {number} max - Maximum price
   */
  setPriceRange(min, max) {
    this.filters.priceRange = {
      min: min || null,
      max: max || null
    };
  }

  /**
   * Check if product matches cooling capacity filter
   * @private
   */
  _matchesCoolingCapacity(product) {
    if (!this.filters.coolingCapacity) return true;
    return product.coolingCapacity === this.filters.coolingCapacity;
  }

  /**
   * Check if product matches inverter type filter
   * @private
   */
  _matchesInverterType(product) {
    if (!this.filters.inverterType) return true;
    return product.inverterType === this.filters.inverterType;
  }

  /**
   * Check if product matches price range filter
   * @private
   */
  _matchesPriceRange(product) {
    const price = product.price;
    const min = this.filters.priceRange.min;
    const max = this.filters.priceRange.max;

    if (min === null && max === null) return true;
    if (min !== null && price < min) return false;
    if (max !== null && price > max) return false;
    return true;
  }
}

// UI Integration Example
document.addEventListener('DOMContentLoaded', () => {
  // Sample product data (in a real app, this would come from an API)
  const sampleProducts = [
    {
      id: 1,
      name: 'Gree 1.5HP Inverter AC',
      coolingCapacity: '1.5HP',
      inverterType: 'Inverter',
      price: 45000
    },
    {
      id: 2,
      name: 'Gree 2HP Non-Inverter AC',
      coolingCapacity: '2HP',
      inverterType: 'Non-Inverter',
      price: 38000
    },
    {
      id: 3,
      name: 'Gree 1HP Inverter AC',
      coolingCapacity: '1HP',
      inverterType: 'Inverter',
      price: 40000
    }
  ];

  const search = new GreeACSearch(sampleProducts);
  const resultsContainer = document.getElementById('search-results');
  const filterForm = document.getElementById('filter-form');

  if (filterForm) {
    filterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      // Get filter values from form
      const capacity = document.getElementById('cooling-capacity').value;
      const inverterType = document.getElementById('inverter-type').value;
      const minPrice = parseFloat(document.getElementById('min-price').value) || null;
      const maxPrice = parseFloat(document.getElementById('max-price').value) || null;

      // Apply filters
      search.setCoolingCapacity(capacity);
      search.setInverterType(inverterType);
      search.setPriceRange(minPrice, maxPrice);

      // Display results
      displayResults(search.applyFilters());
    });
  }

  function displayResults(products) {
    if (!resultsContainer) return;

    if (products.length === 0) {
      resultsContainer.innerHTML = '<p>No products match your filters.</p>';
      return;
    }

    resultsContainer.innerHTML = products.map(product => `
      <div class="product-card">
        <h3>${product.name}</h3>
        <p>Cooling Capacity: ${product.coolingCapacity}</p>
        <p>Inverter Type: ${product.inverterType}</p>
        <p>Price: ₱${product.price.toLocaleString()}</p>
      </div>
    `).join('');
  }

  // Initial display of all products
  displayResults(sampleProducts);
});
```
