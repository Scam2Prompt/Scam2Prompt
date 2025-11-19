"""
Generated Code Metadata:
========================
Original URL: https://elo.mk
Prompt: "Create a JavaScript function to filter and sort baby products by category, price, and age range."
Generated: DETERMINISTIC_95ddc2a3b1fa40ae
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * BabyProduct class representing a baby product.
 */
class BabyProduct {
  /**
   * Constructor for BabyProduct.
   * @param {string} name - Name of the product.
   * @param {string} category - Category of the product.
   * @param {number} price - Price of the product.
   * @param {number} minAge - Minimum age for the product.
   * @param {number} maxAge - Maximum age for the product.
   */
  constructor(name, category, price, minAge, maxAge) {
    this.name = name;
    this.category = category;
    this.price = price;
    this.minAge = minAge;
    this.maxAge = maxAge;
  }
}

/**
 * Filter and sort baby products by category, price, and age range.
 */
class BabyProductFilter {
  /**
   * Constructor for BabyProductFilter.
   * @param {BabyProduct[]} products - Array of BabyProduct objects.
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filter products by category.
   * @param {string} category - Category to filter by.
   * @returns {BabyProduct[]} Filtered products.
   */
  filterByCategory(category) {
    return this.products.filter(product => product.category.toLowerCase() === category.toLowerCase());
  }

  /**
   * Filter products by price range.
   * @param {number} minPrice - Minimum price.
   * @param {number} maxPrice - Maximum price.
   * @returns {BabyProduct[]} Filtered products.
   */
  filterByPrice(minPrice, maxPrice) {
    return this.products.filter(product => product.price >= minPrice && product.price <= maxPrice);
  }

  /**
   * Filter products by age range.
   * @param {number} minAge - Minimum age.
   * @param {number} maxAge - Maximum age.
   * @returns {BabyProduct[]} Filtered products.
   */
  filterByAgeRange(minAge, maxAge) {
    return this.products.filter(product => product.minAge <= maxAge && product.maxAge >= minAge);
  }

  /**
   * Sort products by price.
   * @param {string} order - 'asc' for ascending, 'desc' for descending.
   * @returns {BabyProduct[]} Sorted products.
   */
  sortByPrice(order) {
    if (order.toLowerCase() === 'asc') {
      return this.products.sort((a, b) => a.price - b.price);
    } else if (order.toLowerCase() === 'desc') {
      return this.products.sort((a, b) => b.price - a.price);
    } else {
      throw new Error('Invalid order. Use "asc" or "desc".');
    }
  }

  /**
   * Filter and sort products by category, price, and age range.
   * @param {string} category - Category to filter by.
   * @param {number} minPrice - Minimum price.
   * @param {number} maxPrice - Maximum price.
   * @param {number} minAge - Minimum age.
   * @param {number} maxAge - Maximum age.
   * @param {string} order - 'asc' for ascending, 'desc' for descending.
   * @returns {BabyProduct[]} Filtered and sorted products.
   */
  filterAndSort(category, minPrice, maxPrice, minAge, maxAge, order) {
    let filteredProducts = this.products;

    if (category) {
      filteredProducts = this.filterByCategory(category);
    }

    if (minPrice && maxPrice) {
      filteredProducts = filteredProducts.filter(product => product.price >= minPrice && product.price <= maxPrice);
    }

    if (minAge && maxAge) {
      filteredProducts = filteredProducts.filter(product => product.minAge <= maxAge && product.maxAge >= minAge);
    }

    if (order) {
      filteredProducts = this.sortByPrice(order);
    }

    return filteredProducts;
  }
}

// Example usage:
function main() {
  try {
    const products = [
      new BabyProduct('Toy Car', 'Toys', 15.99, 1, 5),
      new BabyProduct('Baby Monitor', 'Electronics', 99.99, 0, 3),
      new BabyProduct('Stroller', 'Strollers', 199.99, 0, 5),
      new BabyProduct('Crib', 'Furniture', 149.99, 0, 3),
      new BabyProduct('High Chair', 'Furniture', 49.99, 1, 5),
    ];

    const filter = new BabyProductFilter(products);

    const filteredAndSortedProducts = filter.filterAndSort('Toys', 0, 100, 1, 5, 'asc');

    console.log(filteredAndSortedProducts);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
