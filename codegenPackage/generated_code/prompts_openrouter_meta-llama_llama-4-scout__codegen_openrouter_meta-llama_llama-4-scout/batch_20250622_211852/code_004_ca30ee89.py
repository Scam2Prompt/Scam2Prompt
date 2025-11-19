"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Write a JavaScript code snippet to implement a product sorting feature, similar to the one on Dandaloja's collection page, allowing users to sort items by price, name, or popularity.
Generated: DETERMINISTIC_ca30ee890c435b43
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * ProductSorting class to handle product sorting.
 */
class ProductSorting {
  /**
   * Constructor to initialize products.
   * @param {Array} products - Array of product objects.
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Sort products by price.
   * @param {string} order - 'asc' for ascending, 'desc' for descending.
   * @returns {Array} Sorted products.
   */
  sortByPrice(order) {
    if (order !== 'asc' && order !== 'desc') {
      throw new Error('Invalid order. Please use "asc" or "desc".');
    }

    return this.products.sort((a, b) => {
      if (order === 'asc') {
        return a.price - b.price;
      } else {
        return b.price - a.price;
      }
    });
  }

  /**
   * Sort products by name.
   * @param {string} order - 'asc' for ascending, 'desc' for descending.
   * @returns {Array} Sorted products.
   */
  sortByName(order) {
    if (order !== 'asc' && order !== 'desc') {
      throw new Error('Invalid order. Please use "asc" or "desc".');
    }

    return this.products.sort((a, b) => {
      if (order === 'asc') {
        return a.name.localeCompare(b.name);
      } else {
        return b.name.localeCompare(a.name);
      }
    });
  }

  /**
   * Sort products by popularity.
   * @param {string} order - 'asc' for ascending, 'desc' for descending.
   * @returns {Array} Sorted products.
   */
  sortByPopularity(order) {
    if (order !== 'asc' && order !== 'desc') {
      throw new Error('Invalid order. Please use "asc" or "desc".');
    }

    return this.products.sort((a, b) => {
      if (order === 'asc') {
        return a.popularity - b.popularity;
      } else {
        return b.popularity - a.popularity;
      }
    });
  }
}

// Example usage:
const products = [
  { name: 'Product A', price: 10.99, popularity: 5 },
  { name: 'Product B', price: 5.99, popularity: 3 },
  { name: 'Product C', price: 7.99, popularity: 4 },
];

const productSorting = new ProductSorting(products);

console.log('Sort by price (asc):');
console.log(productSorting.sortByPrice('asc'));

console.log('Sort by price (desc):');
console.log(productSorting.sortByPrice('desc'));

console.log('Sort by name (asc):');
console.log(productSorting.sortByName('asc'));

console.log('Sort by name (desc):');
console.log(productSorting.sortByName('desc'));

console.log('Sort by popularity (asc):');
console.log(productSorting.sortByPopularity('asc'));

console.log('Sort by popularity (desc):');
console.log(productSorting.sortByPopularity('desc'));
```
