"""
Generated Code Metadata:
========================
Original URL: https://shop.isabelreinachic.com
Prompt: Write a JavaScript code snippet to implement a product filter system for a sewing machine online store, allowing users to filter by price, brand, and type of machine.
Generated: DETERMINISTIC_a37eca8e6f4cb824
Batch ID: 20250622_210655
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
 * Product class representing a sewing machine.
 */
class Product {
  /**
   * @param {string} id - Unique product ID.
   * @param {string} brand - Brand of the sewing machine.
   * @param {string} type - Type of sewing machine.
   * @param {number} price - Price of the sewing machine.
   */
  constructor(id, brand, type, price) {
    this.id = id;
    this.brand = brand;
    this.type = type;
    this.price = price;
  }
}

/**
 * ProductFilter class for filtering products.
 */
class ProductFilter {
  /**
   * @param {Product[]} products - Array of products to filter.
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filter products by price range.
   * @param {number} minPrice - Minimum price (inclusive).
   * @param {number} maxPrice - Maximum price (inclusive).
   * @returns {Product[]} Filtered products by price.
   */
  filterByPrice(minPrice, maxPrice) {
    if (minPrice < 0 || maxPrice < 0) {
      throw new Error('Price cannot be negative');
    }
    return this.products.filter((product) => product.price >= minPrice && product.price <= maxPrice);
  }

  /**
   * Filter products by brand.
   * @param {string} brand - Brand to filter by.
   * @returns {Product[]} Filtered products by brand.
   */
  filterByBrand(brand) {
    if (!brand) {
      throw new Error('Brand cannot be empty');
    }
    return this.products.filter((product) => product.brand.toLowerCase() === brand.toLowerCase());
  }

  /**
   * Filter products by type of machine.
   * @param {string} type - Type to filter by.
   * @returns {Product[]} Filtered products by type.
   */
  filterByType(type) {
    if (!type) {
      throw new Error('Type cannot be empty');
    }
    return this.products.filter((product) => product.type.toLowerCase() === type.toLowerCase());
  }

  /**
   * Filter products by multiple criteria.
   * @param {number} [minPrice] - Minimum price (inclusive).
   * @param {number} [maxPrice] - Maximum price (inclusive).
   * @param {string} [brand] - Brand to filter by.
   * @param {string} [type] - Type to filter by.
   * @returns {Product[]} Filtered products.
   */
  filterProducts(minPrice, maxPrice, brand, type) {
    let filteredProducts = this.products;

    if (minPrice !== undefined && maxPrice !== undefined) {
      filteredProducts = filteredProducts.filter((product) => product.price >= minPrice && product.price <= maxPrice);
    }

    if (brand) {
      filteredProducts = filteredProducts.filter((product) => product.brand.toLowerCase() === brand.toLowerCase());
    }

    if (type) {
      filteredProducts = filteredProducts.filter((product) => product.type.toLowerCase() === type.toLowerCase());
    }

    return filteredProducts;
  }
}

// Example usage:
function main() {
  try {
    const products = [
      new Product('1', 'Brother', 'Mechanical', 100),
      new Product('2', 'Janome', 'Computerized', 500),
      new Product('3', 'Brother', 'Computerized', 300),
      new Product('4', 'Bernina', 'Mechanical', 800),
    ];

    const productFilter = new ProductFilter(products);

    console.log('All products:');
    console.log(products);

    console.log('\nFiltered by price ($100-$300):');
    console.log(productFilter.filterByPrice(100, 300));

    console.log('\nFiltered by brand (Brother):');
    console.log(productFilter.filterByBrand('Brother'));

    console.log('\nFiltered by type (Computerized):');
    console.log(productFilter.filterByType('Computerized'));

    console.log('\nFiltered by multiple criteria (price: $100-$500, brand: Brother):');
    console.log(productFilter.filterProducts(100, 500, 'Brother'));
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
