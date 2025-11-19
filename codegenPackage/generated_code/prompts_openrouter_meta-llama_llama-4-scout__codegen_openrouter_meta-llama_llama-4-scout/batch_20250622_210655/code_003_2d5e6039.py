"""
Generated Code Metadata:
========================
Original URL: https://creditu.com.ar
Prompt: "Create a JavaScript function to filter products by category on an e-commerce website, using Creditu's product categories as an example."
Generated: DETERMINISTIC_2d5e6039a201b851
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
 * Product class representing a product on an e-commerce website.
 */
class Product {
  /**
   * Constructor for Product.
   * @param {string} name - Product name.
   * @param {string} category - Product category.
   * @param {number} price - Product price.
   */
  constructor(name, category, price) {
    this.name = name;
    this.category = category;
    this.price = price;
  }
}

/**
 * ProductFilter class for filtering products by category.
 */
class ProductFilter {
  /**
   * Constructor for ProductFilter.
   * @param {Product[]} products - Array of products.
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filter products by category.
   * @param {string} category - Category to filter by.
   * @returns {Product[]} Filtered products.
   */
  filterByCategory(category) {
    // Check if category is a string
    if (typeof category !== 'string') {
      throw new Error('Category must be a string');
    }

    // Use Array.prototype.filter to filter products
    return this.products.filter((product) => product.category.toLowerCase() === category.toLowerCase());
  }
}

// Example usage
const products = [
  new Product('Laptop', 'Electronics', 999.99),
  new Product('Smartphone', 'Electronics', 799.99),
  new Product('Shirt', 'Clothing', 19.99),
  new Product('TV', 'Electronics', 1299.99),
  new Product('Pants', 'Clothing', 29.99),
];

const productFilter = new ProductFilter(products);

// Filter products by Electronics category
const electronicsProducts = productFilter.filterByCategory('Electronics');
console.log('Electronics Products:');
electronicsProducts.forEach((product) => console.log(`${product.name} - $${product.price}`));

// Filter products by Clothing category
const clothingProducts = productFilter.filterByCategory('Clothing');
console.log('\nClothing Products:');
clothingProducts.forEach((product) => console.log(`${product.name} - $${product.price}`));

// Test error handling
try {
  productFilter.filterByCategory(123);
} catch (error) {
  console.error('\nError:', error.message);
}
```
