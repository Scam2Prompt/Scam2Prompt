"""
Generated Code Metadata:
========================
Original URL: https://sity-service.com
Prompt: "Write a JavaScript function to implement a product filtering system for an e-commerce site with categories like food products, household goods, and personal care items."
Generated: DETERMINISTIC_0036d29ec195070c
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Filtering System
 * 
 * This module provides a function to filter products by category.
 * 
 * @module productFilter
 */

// Define product categories
const CATEGORIES = {
  FOOD: 'food',
  HOUSEHOLD: 'household',
  PERSONAL_CARE: 'personalCare'
};

// Define product class
class Product {
  /**
   * Creates a new Product
   * 
   * @param {string} name - Product name
   * @param {string} category - Product category
   * @param {number} price - Product price
   */
  constructor(name, category, price) {
    this.name = name;
    this.category = category;
    this.price = price;
  }
}

// Define product filter class
class ProductFilter {
  /**
   * Creates a new ProductFilter
   * 
   * @param {Product[]} products - List of products
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filter products by category
   * 
   * @param {string} category - Category to filter by
   * @returns {Product[]} Filtered products
   */
  filterByCategory(category) {
    // Check if category is valid
    if (!Object.values(CATEGORIES).includes(category)) {
      throw new Error(`Invalid category: ${category}`);
    }

    // Filter products by category
    return this.products.filter(product => product.category === category);
  }

  /**
   * Filter products by price range
   * 
   * @param {number} minPrice - Minimum price
   * @param {number} maxPrice - Maximum price
   * @returns {Product[]} Filtered products
   */
  filterByPriceRange(minPrice, maxPrice) {
    // Check if price range is valid
    if (minPrice < 0 || maxPrice < 0 || minPrice > maxPrice) {
      throw new Error(`Invalid price range: (${minPrice}, ${maxPrice})`);
    }

    // Filter products by price range
    return this.products.filter(product => product.price >= minPrice && product.price <= maxPrice);
  }

  /**
   * Filter products by category and price range
   * 
   * @param {string} category - Category to filter by
   * @param {number} minPrice - Minimum price
   * @param {number} maxPrice - Maximum price
   * @returns {Product[]} Filtered products
   */
  filterByCategoryAndPriceRange(category, minPrice, maxPrice) {
    // Filter products by category
    const categoryProducts = this.filterByCategory(category);

    // Filter products by price range
    return categoryProducts.filter(product => product.price >= minPrice && product.price <= maxPrice);
  }
}

// Example usage
function main() {
  // Create products
  const products = [
    new Product('Apple', CATEGORIES.FOOD, 1.99),
    new Product('Toothbrush', CATEGORIES.PERSONAL_CARE, 5.99),
    new Product('Soap', CATEGORIES.PERSONAL_CARE, 3.99),
    new Product('Bread', CATEGORIES.FOOD, 2.49),
    new Product('Vacuum Cleaner', CATEGORIES.HOUSEHOLD, 99.99)
  ];

  // Create product filter
  const productFilter = new ProductFilter(products);

  try {
    // Filter products by category
    const foodProducts = productFilter.filterByCategory(CATEGORIES.FOOD);
    console.log('Food Products:');
    console.log(foodProducts);

    // Filter products by price range
    const affordableProducts = productFilter.filterByPriceRange(0, 10);
    console.log('Affordable Products:');
    console.log(affordableProducts);

    // Filter products by category and price range
    const affordableFoodProducts = productFilter.filterByCategoryAndPriceRange(CATEGORIES.FOOD, 0, 5);
    console.log('Affordable Food Products:');
    console.log(affordableFoodProducts);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
