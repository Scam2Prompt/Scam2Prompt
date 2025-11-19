"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Write code to implement a "Sort by" feature for filtering products on an online course platform, similar to the navigation options seen on the Sui Foundation's Teachable site.
Generated: DETERMINISTIC_e74f5bb7fb665132
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Sorting Module for Online Course Platform
 * Implements sort-by functionality similar to Teachable/Sui Foundation
 */

class ProductSorter {
  /**
   * Initialize the sorter with products and default options
   * @param {Array} products - Array of product objects to sort
   * @param {Object} options - Configuration options
   */
  constructor(products, options = {}) {
    this.products = [...products];
    this.defaultSortKey = options.defaultSortKey || 'popularity';
    this.sortOptions = {
      popularity: { label: 'Most Popular', fn: this.sortByPopularity.bind(this) },
      newest: { label: 'Newest', fn: this.sortByNewest.bind(this) },
      price_asc: { label: 'Price: Low to High', fn: this.sortByPriceAsc.bind(this) },
      price_desc: { label: 'Price: High to Low', fn: this.sortByPriceDesc.bind(this) },
      rating: { label: 'Highest Rated', fn: this.sortByRating.bind(this) },
      ...options.customSortOptions
    };
  }

  /**
   * Sort products by selected key
   * @param {string} sortKey - Key from sortOptions to sort by
   * @returns {Array} - Sorted array of products
   */
  sort(sortKey = this.defaultSortKey) {
    if (!this.sortOptions[sortKey]) {
      console.warn(`Invalid sort key: ${sortKey}. Using default.`);
      sortKey = this.defaultSortKey;
    }

    try {
      return [...this.products].sort(this.sortOptions[sortKey].fn);
    } catch (error) {
      console.error('Sorting failed:', error);
      return this.products;
    }
  }

  /**
   * Get available sort options for UI rendering
   * @returns {Array} - Array of {value, label} objects
   */
  getSortOptions() {
    return Object.entries(this.sortOptions).map(([value, { label }]) => ({
      value,
      label
    }));
  }

  // Sorting methods
  sortByPopularity(a, b) {
    return (b.popularity || 0) - (a.popularity || 0);
  }

  sortByNewest(a, b) {
    return new Date(b.createdAt || 0) - new Date(a.createdAt || 0);
  }

  sortByPriceAsc(a, b) {
    return (a.price || 0) - (b.price || 0);
  }

  sortByPriceDesc(a, b) {
    return (b.price || 0) - (a.price || 0);
  }

  sortByRating(a, b) {
    return (b.rating || 0) - (a.rating || 0);
  }
}

// Example usage:
/*
const products = [
  { id: 1, title: 'Intro to Blockchain', popularity: 150, createdAt: '2023-01-15', price: 99, rating: 4.8 },
  { id: 2, title: 'Advanced Smart Contracts', popularity: 200, createdAt: '2023-03-10', price: 149, rating: 4.9 },
  { id: 3, title: 'Web3 Security', popularity: 80, createdAt: '2022-11-20', price: 79, rating: 4.5 }
];

const sorter = new ProductSorter(products);
const sortedProducts = sorter.sort('price_asc');
const sortOptions = sorter.getSortOptions();
*/
```
