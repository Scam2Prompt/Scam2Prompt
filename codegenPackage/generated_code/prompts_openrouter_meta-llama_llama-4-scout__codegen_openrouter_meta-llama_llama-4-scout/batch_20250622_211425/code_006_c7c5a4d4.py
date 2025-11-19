"""
Generated Code Metadata:
========================
Original URL: https://glisten.site
Prompt: Write a code snippet in JavaScript to implement a product filtering system, similar to the one used on Glisten's website, allowing users to filter iPhone cases by model, price, and design.
Generated: DETERMINISTIC_c7c5a4d4fdf1a409
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ProductFilteringSystem.js

/**
 * Represents a product filter.
 */
class ProductFilter {
  /**
   * Creates a new ProductFilter instance.
   * @param {Object[]} products - The list of products to filter.
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filters products by model.
   * @param {string} model - The model to filter by.
   * @returns {Object[]} The filtered products.
   */
  filterByModel(model) {
    return this.products.filter(product => product.model === model);
  }

  /**
   * Filters products by price range.
   * @param {number} minPrice - The minimum price.
   * @param {number} maxPrice - The maximum price.
   * @returns {Object[]} The filtered products.
   */
  filterByPrice(minPrice, maxPrice) {
    return this.products.filter(product => product.price >= minPrice && product.price <= maxPrice);
  }

  /**
   * Filters products by design.
   * @param {string} design - The design to filter by.
   * @returns {Object[]} The filtered products.
   */
  filterByDesign(design) {
    return this.products.filter(product => product.design === design);
  }

  /**
   * Applies multiple filters to the products.
   * @param {Object} filters - The filters to apply.
   * @param {string} [filters.model] - The model to filter by.
   * @param {number} [filters.minPrice] - The minimum price.
   * @param {number} [filters.maxPrice] - The maximum price.
   * @param {string} [filters.design] - The design to filter by.
   * @returns {Object[]} The filtered products.
   */
  applyFilters(filters) {
    let filteredProducts = this.products;

    if (filters.model) {
      filteredProducts = filteredProducts.filter(product => product.model === filters.model);
    }

    if (filters.minPrice && filters.maxPrice) {
      filteredProducts = filteredProducts.filter(product => product.price >= filters.minPrice && product.price <= filters.maxPrice);
    }

    if (filters.design) {
      filteredProducts = filteredProducts.filter(product => product.design === filters.design);
    }

    return filteredProducts;
  }
}

// Example usage:
const products = [
  { id: 1, model: 'iPhone 13', price: 29.99, design: 'Glitter' },
  { id: 2, model: 'iPhone 13', price: 39.99, design: 'Matte' },
  { id: 3, model: 'iPhone 14', price: 49.99, design: 'Glitter' },
  { id: 4, model: 'iPhone 14', price: 59.99, design: 'Glossy' },
];

const filter = new ProductFilter(products);

// Filter by model
const iphone13Products = filter.filterByModel('iPhone 13');
console.log('iPhone 13 products:', iphone13Products);

// Filter by price range
const affordableProducts = filter.filterByPrice(20, 40);
console.log('Affordable products:', affordableProducts);

// Filter by design
const glitterProducts = filter.filterByDesign('Glitter');
console.log('Glitter products:', glitterProducts);

// Apply multiple filters
const filters = {
  model: 'iPhone 13',
  minPrice: 20,
  maxPrice: 40,
  design: 'Glitter',
};

const filteredProducts = filter.applyFilters(filters);
console.log('Filtered products:', filteredProducts);
```
