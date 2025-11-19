"""
Generated Code Metadata:
========================
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Write a JavaScript code to implement a product filtering system, similar to the one used on the webpage, to filter shoes by brand (e.g., Nike, Mizuno, Puma) and price range.
Generated: DETERMINISTIC_5ae3c1da72e3ff70
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product class representing a shoe
class Product {
  /**
   * @param {string} name - Shoe name
   * @param {string} brand - Shoe brand
   * @param {number} price - Shoe price
   */
  constructor(name, brand, price) {
    this.name = name;
    this.brand = brand;
    this.price = price;
  }
}

// ProductFilter class for filtering products
class ProductFilter {
  /**
   * @param {Product[]} products - Array of products
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filter products by brand
   * @param {string[]} brands - Array of brands to filter by
   * @returns {Product[]} Filtered products
   */
  filterByBrand(brands) {
    return this.products.filter(product => brands.includes(product.brand));
  }

  /**
   * Filter products by price range
   * @param {number} minPrice - Minimum price
   * @param {number} maxPrice - Maximum price
   * @returns {Product[]} Filtered products
   */
  filterByPriceRange(minPrice, maxPrice) {
    return this.products.filter(product => product.price >= minPrice && product.price <= maxPrice);
  }

  /**
   * Filter products by brand and price range
   * @param {string[]} brands - Array of brands to filter by
   * @param {number} minPrice - Minimum price
   * @param {number} maxPrice - Maximum price
   * @returns {Product[]} Filtered products
   */
  filterProducts(brands, minPrice, maxPrice) {
    return this.filterByPriceRange(minPrice, maxPrice).filter(product => brands.includes(product.brand));
  }
}

// Example usage
try {
  // Create products
  const products = [
    new Product('Nike Air Max', 'Nike', 100),
    new Product('Mizuno Wave Sky', 'Mizuno', 120),
    new Product('Puma Future Rider', 'Puma', 80),
    new Product('Nike Free RN', 'Nike', 90),
    new Product('Mizuno Vapor Rider', 'Mizuno', 110),
  ];

  // Create product filter
  const productFilter = new ProductFilter(products);

  // Filter products
  const brands = ['Nike', 'Mizuno'];
  const minPrice = 90;
  const maxPrice = 120;
  const filteredProducts = productFilter.filterProducts(brands, minPrice, maxPrice);

  // Print filtered products
  console.log('Filtered Products:');
  filteredProducts.forEach(product => {
    console.log(`Name: ${product.name}, Brand: ${product.brand}, Price: ${product.price}`);
  });
} catch (error) {
  console.error('Error:', error.message);
}
```
