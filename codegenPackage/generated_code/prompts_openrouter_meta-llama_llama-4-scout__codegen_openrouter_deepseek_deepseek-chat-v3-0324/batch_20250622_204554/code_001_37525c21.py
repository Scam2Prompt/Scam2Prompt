"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Recommend a JavaScript library for building a product search bar, like the one on moveisonlinepelotasbraz, that can filter products by price, category, and name.
Generated: DETERMINISTIC_37525c21a83ec59b
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Fuse from 'fuse.js';

// ProductSearchBar component
class ProductSearchBar {
  constructor(products, options) {
    this.products = products;
    this.options = options || {
      keys: ['name', 'category'],
      threshold: 0.4,
      includeScore: true
    };
    this.fuse = new Fuse(this.products, this.options);
    this.currentFilters = {
      priceRange: null,
      category: null,
      searchQuery: ''
    };
  }

  // Set price range filter
  setPriceRange(min, max) {
    this.currentFilters.priceRange = { min, max };
    return this;
  }

  // Set category filter
  setCategory(category) {
    this.currentFilters.category = category;
    return this;
  }

  // Set search query
  setSearchQuery(query) {
    this.currentFilters.searchQuery = query;
    return this;
  }

  // Clear all filters
  clearFilters() {
    this.currentFilters = {
      priceRange: null,
      category: null,
      searchQuery: ''
    };
    return this;
  }

  // Apply all filters and return matching products
  applyFilters() {
    let results = [...this.products];

    // Apply text search if query exists
    if (this.currentFilters.searchQuery) {
      results = this.fuse.search(this.currentFilters.searchQuery)
        .map(result => result.item);
    }

    // Apply category filter if set
    if (this.currentFilters.category) {
      results = results.filter(product => 
        product.category === this.currentFilters.category
      );
    }

    // Apply price range filter if set
    if (this.currentFilters.priceRange) {
      const { min, max } = this.currentFilters.priceRange;
      results = results.filter(product => 
        product.price >= min && product.price <= max
      );
    }

    return results;
  }
}

// Example usage:
/*
const products = [
  { id: 1, name: 'Product A', category: 'Electronics', price: 99.99 },
  { id: 2, name: 'Product B', category: 'Clothing', price: 29.99 },
  { id: 3, name: 'Product C', category: 'Electronics', price: 199.99 }
];

const searchBar = new ProductSearchBar(products);

// Set filters
searchBar
  .setSearchQuery('Product')
  .setCategory('Electronics')
  .setPriceRange(50, 200);

// Get filtered results
const filteredProducts = searchBar.applyFilters();
console.log(filteredProducts);

// Clear filters
searchBar.clearFilters();
*/
```
