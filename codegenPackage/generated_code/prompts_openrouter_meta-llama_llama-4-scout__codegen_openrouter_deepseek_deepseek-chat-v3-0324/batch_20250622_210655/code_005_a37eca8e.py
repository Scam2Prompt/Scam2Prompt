"""
Generated Code Metadata:
========================
Original URL: https://shop.isabelreinachic.com
Prompt: Write a JavaScript code snippet to implement a product filter system for a sewing machine online store, allowing users to filter by price, brand, and type of machine.
Generated: DETERMINISTIC_a37eca8e6f4cb824
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Filter System for Sewing Machine Online Store
 * Allows filtering by price range, brand, and machine type
 */

class ProductFilter {
  constructor(products) {
    this.products = products;
    this.filters = {
      priceRange: [0, Infinity],
      brands: [],
      types: []
    };
  }

  /**
   * Set price range filter
   * @param {number} min - Minimum price
   * @param {number} max - Maximum price
   */
  setPriceRange(min, max) {
    this.filters.priceRange = [min, max];
    return this;
  }

  /**
   * Add brand to filter
   * @param {string} brand - Brand name to filter by
   */
  addBrand(brand) {
    if (!this.filters.brands.includes(brand)) {
      this.filters.brands.push(brand);
    }
    return this;
  }

  /**
   * Remove brand from filter
   * @param {string} brand - Brand name to remove
   */
  removeBrand(brand) {
    this.filters.brands = this.filters.brands.filter(b => b !== brand);
    return this;
  }

  /**
   * Add machine type to filter
   * @param {string} type - Machine type to filter by
   */
  addType(type) {
    if (!this.filters.types.includes(type)) {
      this.filters.types.push(type);
    }
    return this;
  }

  /**
   * Remove machine type from filter
   * @param {string} type - Machine type to remove
   */
  removeType(type) {
    this.filters.types = this.filters.types.filter(t => t !== type);
    return this;
  }

  /**
   * Clear all filters
   */
  clearFilters() {
    this.filters = {
      priceRange: [0, Infinity],
      brands: [],
      types: []
    };
    return this;
  }

  /**
   * Apply all current filters to products
   * @returns {Array} - Filtered products array
   */
  applyFilters() {
    return this.products.filter(product => {
      // Price range filter
      const [minPrice, maxPrice] = this.filters.priceRange;
      if (product.price < minPrice || product.price > maxPrice) {
        return false;
      }

      // Brand filter
      if (this.filters.brands.length > 0 && !this.filters.brands.includes(product.brand)) {
        return false;
      }

      // Type filter
      if (this.filters.types.length > 0 && !this.filters.types.includes(product.type)) {
        return false;
      }

      return true;
    });
  }
}

// Example usage:
const sampleProducts = [
  { id: 1, name: 'Basic Stitch', brand: 'Singer', type: 'Mechanical', price: 199.99 },
  { id: 2, name: 'Pro Stitch', brand: 'Brother', type: 'Electronic', price: 349.99 },
  { id: 3, name: 'Quilt Master', brand: 'Janome', type: 'Computerized', price: 899.99 },
  { id: 4, name: 'Heavy Duty', brand: 'Singer', type: 'Mechanical', price: 249.99 },
  { id: 5, name: 'Embroidery Pro', brand: 'Brother', type: 'Computerized', price: 1299.99 }
];

// Initialize filter system
const productFilter = new ProductFilter(sampleProducts);

// Apply filters
const filteredProducts = productFilter
  .setPriceRange(200, 1000)
  .addBrand('Singer')
  .addBrand('Brother')
  .addType('Mechanical')
  .applyFilters();

console.log('Filtered Products:', filteredProducts);
```
