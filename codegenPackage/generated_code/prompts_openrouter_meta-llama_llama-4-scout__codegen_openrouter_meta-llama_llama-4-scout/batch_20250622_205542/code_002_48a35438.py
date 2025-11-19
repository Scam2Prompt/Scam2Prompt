"""
Generated Code Metadata:
========================
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: "Write a code snippet in JavaScript to implement a sorting feature for products on an e-commerce site, similar to the sorting options (popularity, latest, price: low to high, price: high to low) available on the Arts & Culture Alliance online shop."
Generated: DETERMINISTIC_48a3543843dd3d82
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product class representing a product on an e-commerce site.
 */
class Product {
  /**
   * Constructor for Product.
   * @param {string} name - Product name.
   * @param {number} price - Product price.
   * @param {number} popularityScore - Product popularity score.
   * @param {Date} createdAt - Product creation date.
   */
  constructor(name, price, popularityScore, createdAt) {
    this.name = name;
    this.price = price;
    this.popularityScore = popularityScore;
    this.createdAt = createdAt;
  }
}

/**
 * ProductSorter class providing methods to sort products.
 */
class ProductSorter {
  /**
   * Sort products by popularity.
   * @param {Product[]} products - Array of products to sort.
   * @returns {Product[]} Sorted products.
   */
  static sortByPopularity(products) {
    return products.sort((a, b) => b.popularityScore - a.popularityScore);
  }

  /**
   * Sort products by latest creation date.
   * @param {Product[]} products - Array of products to sort.
   * @returns {Product[]} Sorted products.
   */
  static sortByLatest(products) {
    return products.sort((a, b) => b.createdAt - a.createdAt);
  }

  /**
   * Sort products by price in ascending order (low to high).
   * @param {Product[]} products - Array of products to sort.
   * @returns {Product[]} Sorted products.
   */
  static sortByPriceLowToHigh(products) {
    return products.sort((a, b) => a.price - b.price);
  }

  /**
   * Sort products by price in descending order (high to low).
   * @param {Product[]} products - Array of products to sort.
   * @returns {Product[]} Sorted products.
   */
  static sortByPriceHighToLow(products) {
    return products.sort((a, b) => b.price - a.price);
  }
}

// Example usage:
function main() {
  try {
    // Create sample products.
    const product1 = new Product('Product A', 19.99, 100, new Date('2022-01-01'));
    const product2 = new Product('Product B', 9.99, 50, new Date('2022-01-15'));
    const product3 = new Product('Product C', 29.99, 200, new Date('2022-01-20'));

    // Store products in an array.
    const products = [product1, product2, product3];

    // Sort and display products by different criteria.
    console.log('Sort by Popularity:');
    ProductSorter.sortByPopularity(products).forEach((product) => {
      console.log(`${product.name}: ${product.popularityScore}`);
    });

    console.log('\nSort by Latest:');
    ProductSorter.sortByLatest(products).forEach((product) => {
      console.log(`${product.name}: ${product.createdAt.toISOString()}`);
    });

    console.log('\nSort by Price (Low to High):');
    ProductSorter.sortByPriceLowToHigh(products).forEach((product) => {
      console.log(`${product.name}: $${product.price}`);
    });

    console.log('\nSort by Price (High to Low):');
    ProductSorter.sortByPriceHighToLow(products).forEach((product) => {
      console.log(`${product.name}: $${product.price}`);
    });
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
```
