"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Create a JavaScript code snippet to implement a product filter on an e-commerce website, similar to the filter options on Zento Cosmetic's product page.
Generated: DETERMINISTIC_959e865313b18b74
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Filter Implementation for E-commerce Website
 * 
 * Features:
 * - Filter by category
 * - Filter by price range
 * - Filter by rating
 * - Filter by availability
 * - Dynamic UI updates
 */

class ProductFilter {
  constructor(products, filterOptions) {
    this.products = products;
    this.filterOptions = filterOptions;
    this.filteredProducts = [...products];
    this.activeFilters = {
      categories: [],
      priceRange: null,
      minRating: null,
      availability: null
    };
  }

  /**
   * Apply all active filters to products
   */
  applyFilters() {
    this.filteredProducts = this.products.filter(product => {
      // Category filter
      if (this.activeFilters.categories.length > 0 && 
          !this.activeFilters.categories.includes(product.category)) {
        return false;
      }

      // Price range filter
      if (this.activeFilters.priceRange) {
        const [min, max] = this.activeFilters.priceRange;
        if (product.price < min || product.price > max) {
          return false;
        }
      }

      // Rating filter
      if (this.activeFilters.minRating !== null && 
          product.rating < this.activeFilters.minRating) {
        return false;
      }

      // Availability filter
      if (this.activeFilters.availability !== null && 
          product.inStock !== this.activeFilters.availability) {
        return false;
      }

      return true;
    });

    return this.filteredProducts;
  }

  /**
   * Update category filter
   * @param {string} category - Category to add/remove from filter
   */
  toggleCategoryFilter(category) {
    const index = this.activeFilters.categories.indexOf(category);
    if (index === -1) {
      this.activeFilters.categories.push(category);
    } else {
      this.activeFilters.categories.splice(index, 1);
    }
    return this.applyFilters();
  }

  /**
   * Update price range filter
   * @param {Array} range - [minPrice, maxPrice]
   */
  setPriceRangeFilter(range) {
    this.activeFilters.priceRange = range;
    return this.applyFilters();
  }

  /**
   * Update rating filter
   * @param {number} minRating - Minimum rating (1-5)
   */
  setRatingFilter(minRating) {
    this.activeFilters.minRating = minRating;
    return this.applyFilters();
  }

  /**
   * Update availability filter
   * @param {boolean} availability - true for in stock only
   */
  setAvailabilityFilter(availability) {
    this.activeFilters.availability = availability;
    return this.applyFilters();
  }

  /**
   * Reset all filters
   */
  resetFilters() {
    this.activeFilters = {
      categories: [],
      priceRange: null,
      minRating: null,
      availability: null
    };
    this.filteredProducts = [...this.products];
    return this.filteredProducts;
  }

  /**
   * Get current active filters
   */
  getActiveFilters() {
    return this.activeFilters;
  }

  /**
   * Get filtered products count
   */
  getFilteredCount() {
    return this.filteredProducts.length;
  }
}

// UI Handler for Product Filter
class ProductFilterUI {
  constructor(filterInstance, updateCallback) {
    this.filter = filterInstance;
    this.updateCallback = updateCallback;
    this.initEventListeners();
  }

  initEventListeners() {
    // Category filter checkboxes
    document.querySelectorAll('.category-filter input').forEach(checkbox => {
      checkbox.addEventListener('change', (e) => {
        const filteredProducts = this.filter.toggleCategoryFilter(e.target.value);
        this.updateCallback(filteredProducts);
      });
    });

    // Price range slider
    const priceSlider = document.getElementById('price-range-slider');
    if (priceSlider) {
      noUiSlider.create(priceSlider, {
        start: [this.filter.filterOptions.priceRange.min, this.filter.filterOptions.priceRange.max],
        connect: true,
        range: {
          'min': this.filter.filterOptions.priceRange.min,
          'max': this.filter.filterOptions.priceRange.max
        }
      });

      priceSlider.noUiSlider.on('change', (values) => {
        const filteredProducts = this.filter.setPriceRangeFilter(values.map(Number));
        this.updateCallback(filteredProducts);
      });
    }

    // Rating filter
    document.querySelectorAll('.rating-filter input').forEach(radio => {
      radio.addEventListener('change', (e) => {
        const rating = parseInt(e.target.value);
        const filteredProducts = this.filter.setRatingFilter(rating);
        this.updateCallback(filteredProducts);
      });
    });

    // Availability filter
    document.getElementById('availability-filter').addEventListener('change', (e) => {
      const availability = e.target.value === 'in-stock';
      const filteredProducts = this.filter.setAvailabilityFilter(availability);
      this.updateCallback(filteredProducts);
    });

    // Reset button
    document.getElementById('reset-filters').addEventListener('click', () => {
      const filteredProducts = this.filter.resetFilters();
      this.updateCallback(filteredProducts);
      
      // Reset UI elements
      document.querySelectorAll('.category-filter input').forEach(checkbox => {
        checkbox.checked = false;
      });
      
      if (priceSlider) {
        priceSlider.noUiSlider.reset();
      }
      
      document.querySelector('.rating-filter input[value="0"]').checked = true;
      document.getElementById('availability-filter').value = 'all';
    });
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  // Sample products data
  const sampleProducts = [
    { id: 1, name: 'Product A', category: 'skincare', price: 25.99, rating: 4.5, inStock: true },
    { id: 2, name: 'Product B', category: 'makeup', price: 15.50, rating: 3.2, inStock: true },
    { id: 3, name: 'Product C', category: 'haircare', price: 32.75, rating: 4.8, inStock: false },
    { id: 4, name: 'Product D', category: 'skincare', price: 42.00, rating: 4.1, inStock: true },
    { id: 5, name: 'Product E', category: 'makeup', price: 19.99, rating: 2.9, inStock: true }
  ];

  const filterOptions = {
    priceRange: {
      min: 10,
      max: 50
    }
  };

  const productFilter = new ProductFilter(sampleProducts, filterOptions);
  
  const updateUI = (filteredProducts) => {
    // Update product listing
    const productList = document.getElementById('product-list');
    if (productList) {
      productList.innerHTML = filteredProducts.map(product => `
        <div class="product-card">
          <h3>${product.name}</h3>
          <p>Category: ${product.category}</p>
          <p>Price: $${product.price.toFixed(2)}</p>
          <p>Rating: ${product.rating}/5</p>
          <p>${product.inStock ? 'In Stock' : 'Out of Stock'}</p>
        </div>
      `).join('');
    }

    // Update filter count
    const filterCount = document.getElementById('filter-count');
    if (filterCount) {
      filterCount.textContent = `${filteredProducts.length} products found`;
    }
  };

  new ProductFilterUI(productFilter, updateUI);
});
```
