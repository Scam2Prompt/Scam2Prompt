"""
Generated Code Metadata:
========================
Original URL: https://www.brothernz.com
Prompt: Generate code in JavaScript to create a dynamic product search interface for Brother sewing machines, allowing users to filter by type (e.g., overlock, coverstitch) and price range.
Generated: DETERMINISTIC_a63a451fc6acdf26
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// productSearch.js

class Product {
  /**
   * Represents a Brother sewing machine product.
   * @param {string} name - Product name.
   * @param {string} type - Product type (e.g., overlock, coverstitch).
   * @param {number} price - Product price.
   */
  constructor(name, type, price) {
    this.name = name;
    this.type = type;
    this.price = price;
  }
}

class ProductSearch {
  /**
   * Manages a collection of Brother sewing machine products and provides filtering functionality.
   */
  constructor() {
    this.products = [];
  }

  /**
   * Adds a product to the collection.
   * @param {Product} product - Product to add.
   */
  addProduct(product) {
    if (product instanceof Product) {
      this.products.push(product);
    } else {
      throw new Error('Invalid product');
    }
  }

  /**
   * Filters products by type and price range.
   * @param {string} type - Product type to filter by (optional).
   * @param {number} minPrice - Minimum price (optional).
   * @param {number} maxPrice - Maximum price (optional).
   * @returns {Product[]} Filtered products.
   */
  filterProducts(type, minPrice, maxPrice) {
    return this.products.filter((product) => {
      let matchesType = type === undefined || product.type === type;
      let matchesPrice = (minPrice === undefined || product.price >= minPrice) 
                        && (maxPrice === undefined || product.price <= maxPrice);
      return matchesType && matchesPrice;
    });
  }
}

// Example usage:
function main() {
  let search = new ProductSearch();

  // Add some products
  search.addProduct(new Product('Brother Overlock Machine', 'overlock', 200));
  search.addProduct(new Product('Brother Coverstitch Machine', 'coverstitch', 300));
  search.addProduct(new Product('Brother Sewing Machine', 'sewing', 100));
  search.addProduct(new Product('Brother Serger Machine', 'overlock', 250));

  try {
    // Filter by type
    let overlockMachines = search.filterProducts('overlock');
    console.log('Overlock Machines:');
    overlockMachines.forEach((product) => console.log(`${product.name} - $${product.price}`));

    // Filter by price range
    let affordableMachines = search.filterProducts(undefined, 0, 250);
    console.log('\nAffordable Machines (under $250):');
    affordableMachines.forEach((product) => console.log(`${product.name} - $${product.price}`));

    // Filter by type and price range
    let coverstitchMachinesUnder300 = search.filterProducts('coverstitch', 0, 300);
    console.log('\nCoverstitch Machines under $300:');
    coverstitchMachinesUnder300.forEach((product) => console.log(`${product.name} - $${product.price}`));
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
