"""
Generated Code Metadata:
========================
Original URL: https://wouo.com.br
Prompt: Generate a JavaScript code snippet for creating a product catalog filter for inhaler accessories, including categories like nebulizers, humidifiers, and masks.
Generated: DETERMINISTIC_16ec3041ff4951db
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ProductCatalogFilter.js

/**
 * Product Catalog Filter class for inhaler accessories.
 */
class ProductCatalogFilter {
  /**
   * Constructor for ProductCatalogFilter.
   * @param {Array} products - List of products to filter.
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filter products by category.
   * @param {string} category - Category to filter by.
   * @returns {Array} Filtered products.
   */
  filterByCategory(category) {
    return this.products.filter(product => product.category === category);
  }

  /**
   * Filter products by name.
   * @param {string} query - Search query.
   * @returns {Array} Filtered products.
   */
  filterByName(query) {
    return this.products.filter(product => product.name.toLowerCase().includes(query.toLowerCase()));
  }

  /**
   * Filter products by price range.
   * @param {number} minPrice - Minimum price.
   * @param {number} maxPrice - Maximum price.
   * @returns {Array} Filtered products.
   */
  filterByPriceRange(minPrice, maxPrice) {
    return this.products.filter(product => product.price >= minPrice && product.price <= maxPrice);
  }
}

// Example usage:
const products = [
  { id: 1, name: 'Nebulizer', category: 'nebulizers', price: 50.99 },
  { id: 2, name: 'Humidifier', category: 'humidifiers', price: 30.99 },
  { id: 3, name: 'Face Mask', category: 'masks', price: 10.99 },
  { id: 4, name: 'Nebulizer Kit', category: 'nebulizers', price: 70.99 },
  { id: 5, name: 'Ultrasonic Humidifier', category: 'humidifiers', price: 40.99 },
];

// Create a ProductCatalogFilter instance
const filter = new ProductCatalogFilter(products);

// Filter by category
const nebulizers = filter.filterByCategory('nebulizers');
console.log('Nebulizers:', nebulizers);

// Filter by name
const query = 'humid';
const searchResults = filter.filterByName(query);
console.log(`Search results for "${query}":`, searchResults);

// Filter by price range
const minPrice = 20;
const maxPrice = 50;
const affordableProducts = filter.filterByPriceRange(minPrice, maxPrice);
console.log(`Products between $${minPrice} and $${maxPrice}:`, affordableProducts);

// Error handling example
try {
  const invalidCategory = filter.filterByCategory(null);
  console.log('Invalid category:', invalidCategory);
} catch (error) {
  console.error('Error:', error.message);
}

// Best practice: Export the class for reusability
export default ProductCatalogFilter;
```
