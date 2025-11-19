"""
Generated Code Metadata:
========================
Original URL: https://regency-towel.com
Prompt: Write a JavaScript code snippet to create a product filter for a website like Regency Towel, allowing users to filter products by material, size, and type (e.g., towels, bedding, uniforms).
Generated: DETERMINISTIC_a3504bc889e0bd89
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Filter Component for Regency Towel-like Website
 * Allows filtering products by material, size, and type
 */

class ProductFilter {
  /**
   * Initialize the product filter
   * @param {Object} options - Configuration options
   * @param {HTMLElement} options.container - DOM element to mount the filter
   * @param {Array} options.products - Array of product objects
   * @param {Function} options.onFilter - Callback when filters change
   */
  constructor({ container, products, onFilter }) {
    if (!container || !products) {
      throw new Error('Container and products are required');
    }

    this.container = container;
    this.products = products;
    this.onFilter = onFilter || (() => {});
    this.filters = {
      material: [],
      size: [],
      type: []
    };

    this.uniqueOptions = this.extractUniqueOptions();
    this.render();
    this.bindEvents();
  }

  /**
   * Extract unique filter options from products
   * @returns {Object} Unique options for each filter category
   */
  extractUniqueOptions() {
    const materials = new Set();
    const sizes = new Set();
    const types = new Set();

    this.products.forEach(product => {
      if (product.material) materials.add(product.material);
      if (product.size) sizes.add(product.size);
      if (product.type) types.add(product.type);
    });

    return {
      material: Array.from(materials).sort(),
      size: Array.from(sizes).sort(),
      type: Array.from(types).sort()
    };
  }

  /**
   * Render the filter UI
   */
  render() {
    this.container.innerHTML = `
      <div class="product-filter">
        <div class="filter-section">
          <h3>Material</h3>
          <div class="filter-options material-options">
            ${this.uniqueOptions.material.map(material => `
              <label>
                <input type="checkbox" name="material" value="${material}">
                ${material}
              </label>
            `).join('')}
          </div>
        </div>

        <div class="filter-section">
          <h3>Size</h3>
          <div class="filter-options size-options">
            ${this.uniqueOptions.size.map(size => `
              <label>
                <input type="checkbox" name="size" value="${size}">
                ${size}
              </label>
            `).join('')}
          </div>
        </div>

        <div class="filter-section">
          <h3>Type</h3>
          <div class="filter-options type-options">
            ${this.uniqueOptions.type.map(type => `
              <label>
                <input type="checkbox" name="type" value="${type}">
                ${type}
              </label>
            `).join('')}
          </div>
        </div>

        <button class="clear-filters">Clear All Filters</button>
      </div>
    `;
  }

  /**
   * Bind event listeners
   */
  bindEvents() {
    this.container.addEventListener('change', (e) => {
      if (e.target.name === 'material' || e.target.name === 'size' || e.target.name === 'type') {
        this.handleFilterChange(e.target.name, e.target.value, e.target.checked);
      }
    });

    this.container.querySelector('.clear-filters').addEventListener('click', () => {
      this.clearFilters();
    });
  }

  /**
   * Handle filter checkbox changes
   * @param {string} filterType - Type of filter (material, size, type)
   * @param {string} value - Filter value
   * @param {boolean} isChecked - Whether checkbox is checked
   */
  handleFilterChange(filterType, value, isChecked) {
    if (isChecked) {
      this.filters[filterType].push(value);
    } else {
      this.filters[filterType] = this.filters[filterType].filter(item => item !== value);
    }
    this.applyFilters();
  }

  /**
   * Apply current filters and trigger callback
   */
  applyFilters() {
    const filteredProducts = this.products.filter(product => {
      return (
        (this.filters.material.length === 0 || this.filters.material.includes(product.material)) &&
        (this.filters.size.length === 0 || this.filters.size.includes(product.size)) &&
        (this.filters.type.length === 0 || this.filters.type.includes(product.type))
      );
    });

    this.onFilter(filteredProducts);
  }

  /**
   * Clear all filters
   */
  clearFilters() {
    this.filters = {
      material: [],
      size: [],
      type: []
    };

    this.container.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
      checkbox.checked = false;
    });

    this.applyFilters();
  }
}

// Example usage:
/*
const filterContainer = document.getElementById('product-filter');
const products = [
  { id: 1, name: 'Bath Towel', material: 'Cotton', size: 'Large', type: 'Towel' },
  { id: 2, name: 'Hand Towel', material: 'Microfiber', size: 'Small', type: 'Towel' },
  { id: 3, name: 'Bath Sheet', material: 'Cotton', size: 'XLarge', type: 'Towel' },
  { id: 4, name: 'Pillowcase', material: 'Linen', size: 'Standard', type: 'Bedding' },
  { id: 5, name: 'Chef Jacket', material: 'Polyester', size: 'Medium', type: 'Uniform' }
];

const productFilter = new ProductFilter({
  container: filterContainer,
  products: products,
  onFilter: (filteredProducts) => {
    console.log('Filtered products:', filteredProducts);
    // Update product listing UI here
  }
});
*/
```
