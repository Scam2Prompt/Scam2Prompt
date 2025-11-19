"""
Generated Code Metadata:
========================
Original URL: https://alsafwaq8.com
Prompt: "Write a code snippet for filtering and sorting products by size and price on an e-commerce website, similar to the layout and functionality seen on الصفوة للملابس الجاهزة for their men's winter dishdashas."
Generated: DETERMINISTIC_ff2ba3f22619dd97
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Filtering and Sorting Utility
 * 
 * This module provides functionality to filter and sort products
 * based on size and price criteria, similar to e-commerce sites.
 */

class ProductFilter {
  /**
   * Initialize with product list
   * @param {Array} products - Array of product objects
   */
  constructor(products) {
    this.products = products || [];
    this.filteredProducts = [...products];
  }

  /**
   * Apply filters to products
   * @param {Object} filters - Filter criteria
   * @param {Array} filters.sizes - Array of sizes to include
   * @param {Object} filters.priceRange - Min and max price
   * @param {number} filters.priceRange.min
   * @param {number} filters.priceRange.max
   * @returns {Array} Filtered products
   */
  applyFilters(filters = {}) {
    try {
      this.filteredProducts = this.products.filter(product => {
        // Size filter
        const sizeMatch = !filters.sizes || filters.sizes.length === 0 || 
          product.availableSizes.some(size => filters.sizes.includes(size));
        
        // Price filter
        const priceMatch = !filters.priceRange || 
          (product.price >= filters.priceRange.min && 
           product.price <= filters.priceRange.max);
        
        return sizeMatch && priceMatch;
      });

      return this.filteredProducts;
    } catch (error) {
      console.error('Error applying filters:', error);
      return this.products;
    }
  }

  /**
   * Sort products by criteria
   * @param {string} sortBy - Sorting criteria ('price-asc', 'price-desc', 'size')
   * @returns {Array} Sorted products
   */
  sortProducts(sortBy = '') {
    try {
      const sortedProducts = [...this.filteredProducts];
      
      switch (sortBy) {
        case 'price-asc':
          sortedProducts.sort((a, b) => a.price - b.price);
          break;
        case 'price-desc':
          sortedProducts.sort((a, b) => b.price - a.price);
          break;
        case 'size':
          sortedProducts.sort((a, b) => {
            const sizeOrder = ['XS', 'S', 'M', 'L', 'XL', 'XXL'];
            return sizeOrder.indexOf(a.mainSize) - sizeOrder.indexOf(b.mainSize);
          });
          break;
        default:
          // No sorting or invalid sort option
          break;
      }

      return sortedProducts;
    } catch (error) {
      console.error('Error sorting products:', error);
      return this.filteredProducts;
    }
  }

  /**
   * Get currently filtered products
   * @returns {Array} Current filtered products
   */
  getFilteredProducts() {
    return this.filteredProducts;
  }
}

// Example usage:
/*
const products = [
  { id: 1, name: 'Winter Dishdasha 1', price: 120, availableSizes: ['M', 'L', 'XL'], mainSize: 'M' },
  { id: 2, name: 'Winter Dishdasha 2', price: 150, availableSizes: ['S', 'M'], mainSize: 'S' },
  { id: 3, name: 'Winter Dishdasha 3', price: 100, availableSizes: ['L', 'XL'], mainSize: 'L' }
];

const filter = new ProductFilter(products);

// Apply filters
const filtered = filter.applyFilters({
  sizes: ['M', 'L'],
  priceRange: { min: 100, max: 140 }
});

// Sort results
const sorted = filter.sortProducts('price-asc');
*/
```
