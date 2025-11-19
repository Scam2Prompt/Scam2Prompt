"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate a JavaScript code to create a simple product filter for a sports equipment website, allowing users to filter by sport (e.g., beach volleyball, handball, etc.) and product type (e.g., balls, shoes, etc.).
Generated: DETERMINISTIC_4fc72dbbefdbfdda
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// productFilter.js

class Product {
  /**
   * Represents a product
   * @param {string} name - Product name
   * @param {string} sport - Sport associated with the product (e.g., beach volleyball, handball)
   * @param {string} type - Product type (e.g., balls, shoes)
   */
  constructor(name, sport, type) {
    this.name = name;
    this.sport = sport;
    this.type = type;
  }
}

class ProductFilter {
  /**
   * Represents a product filter
   * @param {Product[]} products - List of products to filter
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filters products by sport
   * @param {string} sport - Sport to filter by
   * @returns {Product[]} Filtered products
   */
  filterBySport(sport) {
    return this.products.filter(product => product.sport.toLowerCase() === sport.toLowerCase());
  }

  /**
   * Filters products by type
   * @param {string} type - Product type to filter by
   * @returns {Product[]} Filtered products
   */
  filterByType(type) {
    return this.products.filter(product => product.type.toLowerCase() === type.toLowerCase());
  }

  /**
   * Filters products by sport and type
   * @param {string} sport - Sport to filter by
   * @param {string} type - Product type to filter by
   * @returns {Product[]} Filtered products
   */
  filterBySportAndType(sport, type) {
    return this.products.filter(product => product.sport.toLowerCase() === sport.toLowerCase() && product.type.toLowerCase() === type.toLowerCase());
  }
}

// Example usage
const products = [
  new Product('Beach Volleyball', 'beach volleyball', 'balls'),
  new Product('Handball', 'handball', 'balls'),
  new Product('Running Shoes', 'running', 'shoes'),
  new Product('Beach Volleyball Shoes', 'beach volleyball', 'shoes'),
  new Product('Handball Shoes', 'handball', 'shoes'),
];

const productFilter = new ProductFilter(products);

// Filter by sport
const filteredBySport = productFilter.filterBySport('beach volleyball');
console.log('Filtered by sport:');
console.log(filteredBySport);

// Filter by type
const filteredByType = productFilter.filterByType('shoes');
console.log('Filtered by type:');
console.log(filteredByType);

// Filter by sport and type
const filteredBySportAndType = productFilter.filterBySportAndType('handball', 'shoes');
console.log('Filtered by sport and type:');
console.log(filteredBySportAndType);

// Error handling example
try {
  const invalidProduct = new Product('', null, 'balls');
  productFilter.products.push(invalidProduct);
  console.log('Invalid product added:', invalidProduct);
} catch (error) {
  console.error('Error adding product:', error.message);
}

// Validate product inputs
function validateProduct(product) {
  if (!product.name || typeof product.name !== 'string') {
    throw new Error('Product name is required and must be a string');
  }
  if (!product.sport || typeof product.sport !== 'string') {
    throw new Error('Product sport is required and must be a string');
  }
  if (!product.type || typeof product.type !== 'string') {
    throw new Error('Product type is required and must be a string');
  }
}

// Usage with validation
const newProduct = {
  name: 'New Product',
  sport: 'new sport',
  type: 'new type',
};
try {
  validateProduct(newProduct);
  productFilter.products.push(new Product(newProduct.name, newProduct.sport, newProduct.type));
  console.log('New product added:', newProduct);
} catch (error) {
  console.error('Error adding new product:', error.message);
}
```
