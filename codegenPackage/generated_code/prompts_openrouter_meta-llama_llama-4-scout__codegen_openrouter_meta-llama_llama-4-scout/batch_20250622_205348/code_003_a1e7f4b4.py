"""
Generated Code Metadata:
========================
Original URL: https://games-home-plays-galla.weebly.com
Prompt: Write a JavaScript code snippet to implement a product filtering system on an e-commerce website like Baby Calçados, allowing customers to filter products by category, brand, and price.
Generated: DETERMINISTIC_a1e7f4b42e0a37f7
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// productFilter.js

/**
 * Product Filtering System
 * 
 * This module provides a product filtering system for an e-commerce website.
 * It allows customers to filter products by category, brand, and price.
 */

// Product class representing a product
class Product {
  /**
   * @param {number} id - Product ID
   * @param {string} name - Product name
   * @param {string} category - Product category
   * @param {string} brand - Product brand
   * @param {number} price - Product price
   */
  constructor(id, name, category, brand, price) {
    this.id = id;
    this.name = name;
    this.category = category;
    this.brand = brand;
    this.price = price;
  }
}

// ProductFilter class providing filtering functionality
class ProductFilter {
  /**
   * @param {Product[]} products - Array of products
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
    return this.products.filter(product => product.category.toLowerCase() === category.toLowerCase());
  }

  /**
   * Filter products by brand
   * @param {string} brand - Brand to filter by
   * @returns {Product[]} Filtered products
   */
  filterByBrand(brand) {
    return this.products.filter(product => product.brand.toLowerCase() === brand.toLowerCase());
  }

  /**
   * Filter products by price range
   * @param {number} minPrice - Minimum price
   * @param {number} maxPrice - Maximum price
   * @returns {Product[]} Filtered products
   */
  filterByPrice(minPrice, maxPrice) {
    if (minPrice < 0 || maxPrice < 0) {
      throw new Error('Price cannot be negative');
    }
    return this.products.filter(product => product.price >= minPrice && product.price <= maxPrice);
  }

  /**
   * Filter products by multiple criteria
   * @param {string} [category] - Category to filter by
   * @param {string} [brand] - Brand to filter by
   * @param {number} [minPrice] - Minimum price
   * @param {number} [maxPrice] - Maximum price
   * @returns {Product[]} Filtered products
   */
  filterProducts(category, brand, minPrice, maxPrice) {
    let filteredProducts = this.products;

    if (category) {
      filteredProducts = filteredProducts.filter(product => product.category.toLowerCase() === category.toLowerCase());
    }

    if (brand) {
      filteredProducts = filteredProducts.filter(product => product.brand.toLowerCase() === brand.toLowerCase());
    }

    if (minPrice !== undefined && maxPrice !== undefined) {
      if (minPrice < 0 || maxPrice < 0) {
        throw new Error('Price cannot be negative');
      }
      filteredProducts = filteredProducts.filter(product => product.price >= minPrice && product.price <= maxPrice);
    }

    return filteredProducts;
  }
}

// Example usage
const products = [
  new Product(1, 'Product 1', 'Shoes', 'Brand A', 100),
  new Product(2, 'Product 2', 'Shoes', 'Brand B', 200),
  new Product(3, 'Product 3', 'Clothes', 'Brand A', 50),
  new Product(4, 'Product 4', 'Clothes', 'Brand B', 150),
];

const productFilter = new ProductFilter(products);

// Filter by category
const filteredByCategory = productFilter.filterByCategory('Shoes');
console.log('Filtered by category:');
console.log(filteredByCategory);

// Filter by brand
const filteredByBrand = productFilter.filterByBrand('Brand A');
console.log('Filtered by brand:');
console.log(filteredByBrand);

// Filter by price range
const filteredByPrice = productFilter.filterByPrice(100, 200);
console.log('Filtered by price:');
console.log(filteredByPrice);

// Filter by multiple criteria
const filteredProducts = productFilter.filterProducts('Shoes', 'Brand A', 0, 200);
console.log('Filtered by multiple criteria:');
console.log(filteredProducts);
```
