"""
Generated Code Metadata:
========================
Original URL: https://smartprice.co.ke
Prompt: Write a JavaScript code to create a simple product filter for smartphones on SmartPrice KE based on price, brand, and storage capacity.
Generated: DETERMINISTIC_c0198a4ead555d77
Batch ID: 20250622_212748
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
 * Product Filter class for filtering smartphones on SmartPrice KE.
 */
class ProductFilter {
  /**
   * Constructor for ProductFilter.
   * @param {Array} products - List of products to filter.
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filter products by price range.
   * @param {number} minPrice - Minimum price.
   * @param {number} maxPrice - Maximum price.
   * @returns {Array} Filtered products.
   */
  filterByPrice(minPrice, maxPrice) {
    return this.products.filter(product => product.price >= minPrice && product.price <= maxPrice);
  }

  /**
   * Filter products by brand.
   * @param {string} brand - Brand name.
   * @returns {Array} Filtered products.
   */
  filterByBrand(brand) {
    return this.products.filter(product => product.brand.toLowerCase() === brand.toLowerCase());
  }

  /**
   * Filter products by storage capacity.
   * @param {number} storageCapacity - Storage capacity in GB.
   * @returns {Array} Filtered products.
   */
  filterByStorage(storageCapacity) {
    return this.products.filter(product => product.storage === storageCapacity);
  }

  /**
   * Filter products by multiple criteria.
   * @param {number} minPrice - Minimum price.
   * @param {number} maxPrice - Maximum price.
   * @param {string} brand - Brand name.
   * @param {number} storageCapacity - Storage capacity in GB.
   * @returns {Array} Filtered products.
   */
  filterProducts(minPrice, maxPrice, brand, storageCapacity) {
    let filteredProducts = this.products;

    if (minPrice && maxPrice) {
      filteredProducts = filteredProducts.filter(product => product.price >= minPrice && product.price <= maxPrice);
    }

    if (brand) {
      filteredProducts = filteredProducts.filter(product => product.brand.toLowerCase() === brand.toLowerCase());
    }

    if (storageCapacity) {
      filteredProducts = filteredProducts.filter(product => product.storage === storageCapacity);
    }

    return filteredProducts;
  }
}

// Example usage:
const products = [
  { id: 1, brand: 'Apple', storage: 128, price: 50000 },
  { id: 2, brand: 'Samsung', storage: 256, price: 60000 },
  { id: 3, brand: 'Apple', storage: 64, price: 40000 },
  { id: 4, brand: 'Google', storage: 128, price: 55000 },
  { id: 5, brand: 'Samsung', storage: 512, price: 80000 },
];

const productFilter = new ProductFilter(products);

try {
  const filteredProducts = productFilter.filterProducts(40000, 70000, 'Apple');
  console.log('Filtered Products:');
  console.log(filteredProducts);
} catch (error) {
  console.error('Error:', error.message);
}
```
