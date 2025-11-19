"""
Generated Code Metadata:
========================
Original URL: https://elfcosmetics.com.ua
Prompt: "Generate a JavaScript code to implement a product filtering system for an ELF Cosmetics website, allowing users to filter products by category, price, and color."
Generated: DETERMINISTIC_60e6adfc3e17df2b
Batch ID: 20250622_211723
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
 * Product Filtering System for ELF Cosmetics website
 */

// Define product categories
const categories = ['Makeup', 'Skincare', 'Haircare'];

// Define product colors
const colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple'];

// Product class
class Product {
  /**
   * @param {string} name - Product name
   * @param {string} category - Product category
   * @param {number} price - Product price
   * @param {string} color - Product color
   */
  constructor(name, category, price, color) {
    this.name = name;
    this.category = category;
    this.price = price;
    this.color = color;
  }
}

// Product filtering system class
class ProductFilteringSystem {
  /**
   * @param {Product[]} products - List of products
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filter products by category
   * @param {string} category - Category to filter by
   * @returns {Product[]} Filtered products
   */
  filterByCategory(category) {
    return this.products.filter(product => product.category === category);
  }

  /**
   * Filter products by price range
   * @param {number} minPrice - Minimum price
   * @param {number} maxPrice - Maximum price
   * @returns {Product[]} Filtered products
   */
  filterByPrice(minPrice, maxPrice) {
    return this.products.filter(product => product.price >= minPrice && product.price <= maxPrice);
  }

  /**
   * Filter products by color
   * @param {string} color - Color to filter by
   * @returns {Product[]} Filtered products
   */
  filterByColor(color) {
    return this.products.filter(product => product.color === color);
  }

  /**
   * Filter products by multiple criteria
   * @param {string} [category] - Category to filter by
   * @param {number} [minPrice] - Minimum price
   * @param {number} [maxPrice] - Maximum price
   * @param {string} [color] - Color to filter by
   * @returns {Product[]} Filtered products
   */
  filterProducts(category, minPrice, maxPrice, color) {
    let filteredProducts = this.products;

    if (category) {
      filteredProducts = filteredProducts.filter(product => product.category === category);
    }

    if (minPrice && maxPrice) {
      filteredProducts = filteredProducts.filter(product => product.price >= minPrice && product.price <= maxPrice);
    }

    if (color) {
      filteredProducts = filteredProducts.filter(product => product.color === color);
    }

    return filteredProducts;
  }
}

// Example usage
const products = [
  new Product('Lipstick', 'Makeup', 10.99, 'Red'),
  new Product('Foundation', 'Makeup', 15.99, 'Yellow'),
  new Product('Shampoo', 'Haircare', 8.99, 'Blue'),
  new Product('Moisturizer', 'Skincare', 12.99, 'Green'),
  new Product('Eyeshadow', 'Makeup', 14.99, 'Purple'),
];

const filteringSystem = new ProductFilteringSystem(products);

// Test filtering by category
console.log('Filtering by category: Makeup');
const makeupProducts = filteringSystem.filterByCategory('Makeup');
makeupProducts.forEach(product => console.log(product.name));

// Test filtering by price range
console.log('\nFiltering by price range: $10-$15');
const priceFilteredProducts = filteringSystem.filterByPrice(10, 15);
priceFilteredProducts.forEach(product => console.log(product.name));

// Test filtering by color
console.log('\nFiltering by color: Red');
const redProducts = filteringSystem.filterByColor('Red');
redProducts.forEach(product => console.log(product.name));

// Test filtering by multiple criteria
console.log('\nFiltering by category: Makeup, price range: $10-$15, color: Red');
const filteredProducts = filteringSystem.filterProducts('Makeup', 10, 15, 'Red');
filteredProducts.forEach(product => console.log(product.name));
```
