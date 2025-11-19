"""
Generated Code Metadata:
========================
Original URL: https://daddysoluniversity.com
Prompt: Generate a JavaScript code snippet to create a simple online store filter, allowing customers to search for books, manga, or stationery, and apply filters for discounts or promotions.
Generated: DETERMINISTIC_074d570a9fd4980f
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Define a class for products
class Product {
  /**
   * @param {string} name - Product name
   * @param {string} category - Product category (book, manga, stationery)
   * @param {number} price - Product price
   * @param {boolean} onSale - Whether the product is on sale
   * @param {boolean} hasPromotion - Whether the product has a promotion
   */
  constructor(name, category, price, onSale = false, hasPromotion = false) {
    this.name = name;
    this.category = category;
    this.price = price;
    this.onSale = onSale;
    this.hasPromotion = hasPromotion;
  }
}

// Define a class for the online store
class OnlineStore {
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
    return this.products.filter((product) => product.category === category);
  }

  /**
   * Filter products by search query
   * @param {string} query - Search query
   * @returns {Product[]} Filtered products
   */
  searchProducts(query) {
    return this.products.filter((product) => product.name.toLowerCase().includes(query.toLowerCase()));
  }

  /**
   * Filter products by discount or promotion
   * @param {string} filterType - Type of filter (discount or promotion)
   * @returns {Product[]} Filtered products
   */
  filterByDiscountOrPromotion(filterType) {
    if (filterType === 'discount') {
      return this.products.filter((product) => product.onSale);
    } else if (filterType === 'promotion') {
      return this.products.filter((product) => product.hasPromotion);
    } else {
      throw new Error('Invalid filter type');
    }
  }

  /**
   * Apply multiple filters to products
   * @param {string} category - Category to filter by
   * @param {string} query - Search query
   * @param {string} filterType - Type of filter (discount or promotion)
   * @returns {Product[]} Filtered products
   */
  applyFilters(category, query, filterType) {
    let filteredProducts = this.products;

    if (category) {
      filteredProducts = filteredProducts.filter((product) => product.category === category);
    }

    if (query) {
      filteredProducts = filteredProducts.filter((product) => product.name.toLowerCase().includes(query.toLowerCase()));
    }

    if (filterType) {
      if (filterType === 'discount') {
        filteredProducts = filteredProducts.filter((product) => product.onSale);
      } else if (filterType === 'promotion') {
        filteredProducts = filteredProducts.filter((product) => product.hasPromotion);
      } else {
        throw new Error('Invalid filter type');
      }
    }

    return filteredProducts;
  }
}

// Example usage
const products = [
  new Product('Book 1', 'book', 10.99),
  new Product('Manga 1', 'manga', 9.99, true),
  new Product('Stationery 1', 'stationery', 5.99, false, true),
  new Product('Book 2', 'book', 12.99, false, false),
  new Product('Manga 2', 'manga', 11.99, false, false),
];

const onlineStore = new OnlineStore(products);

// Test the filters
try {
  const filteredProducts = onlineStore.applyFilters('book', '', 'discount');
  console.log('Filtered products:');
  console.log(filteredProducts);

  const searchedProducts = onlineStore.searchProducts('manga');
  console.log('Searched products:');
  console.log(searchedProducts);

  const discountedProducts = onlineStore.filterByDiscountOrPromotion('discount');
  console.log('Discounted products:');
  console.log(discountedProducts);
} catch (error) {
  console.error(error.message);
}
```
