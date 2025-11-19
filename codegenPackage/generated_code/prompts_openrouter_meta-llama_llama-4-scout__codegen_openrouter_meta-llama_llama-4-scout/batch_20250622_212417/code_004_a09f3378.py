"""
Generated Code Metadata:
========================
Original URL: https://dotcomachinery.co.tz
Prompt: "Write a JavaScript function to implement a search filter for power tools on an e-commerce website like Dotcom Machinery."
Generated: DETERMINISTIC_a09f3378ae754627
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a power tool product.
 * @typedef {Object} PowerTool
 * @property {string} id - Unique identifier for the product.
 * @property {string} name - Name of the product.
 * @property {string} brand - Brand of the product.
 * @property {string} category - Category of the product (e.g., drill, saw, etc.).
 * @property {number} price - Price of the product.
 */

/**
 * Represents a search filter for power tools.
 * @class
 */
class PowerToolSearchFilter {
  /**
   * Creates an instance of PowerToolSearchFilter.
   * @param {PowerTool[]} powerTools - Array of power tool products.
   */
  constructor(powerTools) {
    this.powerTools = powerTools;
  }

  /**
   * Filters power tools by search query.
   * @param {string} query - Search query.
   * @returns {PowerTool[]} Filtered array of power tools.
   */
  filterByQuery(query) {
    try {
      // Check if query is a string
      if (typeof query !== 'string') {
        throw new Error('Query must be a string');
      }

      // Convert query to lowercase for case-insensitive search
      const lowerCaseQuery = query.toLowerCase();

      // Filter power tools by search query
      return this.powerTools.filter((powerTool) => {
        // Check if power tool's name, brand, or category matches the query
        return (
          powerTool.name.toLowerCase().includes(lowerCaseQuery) ||
          powerTool.brand.toLowerCase().includes(lowerCaseQuery) ||
          powerTool.category.toLowerCase().includes(lowerCaseQuery)
        );
      });
    } catch (error) {
      console.error('Error filtering power tools:', error.message);
      return [];
    }
  }

  /**
   * Filters power tools by brand.
   * @param {string} brand - Brand to filter by.
   * @returns {PowerTool[]} Filtered array of power tools.
   */
  filterByBrand(brand) {
    try {
      // Check if brand is a string
      if (typeof brand !== 'string') {
        throw new Error('Brand must be a string');
      }

      // Filter power tools by brand
      return this.powerTools.filter((powerTool) => powerTool.brand.toLowerCase() === brand.toLowerCase());
    } catch (error) {
      console.error('Error filtering power tools by brand:', error.message);
      return [];
    }
  }

  /**
   * Filters power tools by category.
   * @param {string} category - Category to filter by.
   * @returns {PowerTool[]} Filtered array of power tools.
   */
  filterByCategory(category) {
    try {
      // Check if category is a string
      if (typeof category !== 'string') {
        throw new Error('Category must be a string');
      }

      // Filter power tools by category
      return this.powerTools.filter((powerTool) => powerTool.category.toLowerCase() === category.toLowerCase());
    } catch (error) {
      console.error('Error filtering power tools by category:', error.message);
      return [];
    }
  }

  /**
   * Filters power tools by price range.
   * @param {number} minPrice - Minimum price.
   * @param {number} maxPrice - Maximum price.
   * @returns {PowerTool[]} Filtered array of power tools.
   */
  filterByPriceRange(minPrice, maxPrice) {
    try {
      // Check if minPrice and maxPrice are numbers
      if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Min price and max price must be numbers');
      }

      // Check if minPrice is less than or equal to maxPrice
      if (minPrice > maxPrice) {
        throw new Error('Min price must be less than or equal to max price');
      }

      // Filter power tools by price range
      return this.powerTools.filter((powerTool) => powerTool.price >= minPrice && powerTool.price <= maxPrice);
    } catch (error) {
      console.error('Error filtering power tools by price range:', error.message);
      return [];
    }
  }
}

// Example usage:
const powerTools = [
  { id: '1', name: 'Drill', brand: 'DeWalt', category: 'Drill', price: 99.99 },
  { id: '2', name: 'Saw', brand: 'Makita', category: 'Saw', price: 149.99 },
  { id: '3', name: 'Impact Driver', brand: 'Milwaukee', category: 'Impact Driver', price: 79.99 },
];

const searchFilter = new PowerToolSearchFilter(powerTools);

console.log('Filter by query:');
const filteredByQuery = searchFilter.filterByQuery('drill');
console.log(filteredByQuery);

console.log('Filter by brand:');
const filteredByBrand = searchFilter.filterByBrand('DeWalt');
console.log(filteredByBrand);

console.log('Filter by category:');
const filteredByCategory = searchFilter.filterByCategory('Saw');
console.log(filteredByCategory);

console.log('Filter by price range:');
const filteredByPriceRange = searchFilter.filterByPriceRange(50, 150);
console.log(filteredByPriceRange);
```
