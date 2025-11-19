"""
Generated Code Metadata:
========================
Original URL: https://familyicon.ru
Prompt: "Write a code snippet in JavaScript to implement a simple e-commerce functionality for a religious item store, focusing on product categorization and shopping cart management, inspired by the structure of https://familyicon.ru."
Generated: DETERMINISTIC_b7af32ae34941666
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product.js
class Product {
  /**
   * @param {number} id 
   * @param {string} name 
   * @param {string} category 
   * @param {number} price 
   * @param {string} description 
   */
  constructor(id, name, category, price, description) {
    this.id = id;
    this.name = name;
    this.category = category;
    this.price = price;
    this.description = description;
  }
}

// Category.js
class Category {
  /**
   * @param {string} name 
   */
  constructor(name) {
    this.name = name;
    this.products = [];
  }

  /**
   * @param {Product} product 
   */
  addProduct(product) {
    if (product.category === this.name) {
      this.products.push(product);
    } else {
      throw new Error(`Product ${product.name} does not belong to category ${this.name}`);
    }
  }
}

// ShoppingCart.js
class ShoppingCart {
  constructor() {
    this.items = [];
  }

  /**
   * @param {Product} product 
   */
  addItem(product) {
    this.items.push(product);
  }

  /**
   * @param {Product} product 
   */
  removeItem(product) {
    this.items = this.items.filter(item => item.id !== product.id);
  }

  calculateTotal() {
    return this.items.reduce((total, item) => total + item.price, 0);
  }
}

// Store.js
class Store {
  constructor() {
    this.categories = [];
    this.shoppingCart = new ShoppingCart();
  }

  /**
   * @param {Category} category 
   */
  addCategory(category) {
    this.categories.push(category);
  }

  /**
   * @param {Product} product 
   */
  addProductToCart(product) {
    this.shoppingCart.addItem(product);
  }

  /**
   * @param {Product} product 
   */
  removeProductFromCart(product) {
    this.shoppingCart.removeItem(product);
  }
}

// Usage example
function main() {
  try {
    const store = new Store();

    const category1 = new Category('Icons');
    const category2 = new Category('Prayers');

    store.addCategory(category1);
    store.addCategory(category2);

    const product1 = new Product(1, 'Icon of Jesus', 'Icons', 20.00, 'A beautiful icon of Jesus');
    const product2 = new Product(2, 'Prayer Book', 'Prayers', 15.00, 'A comprehensive prayer book');

    category1.addProduct(product1);
    category2.addProduct(product2);

    store.addProductToCart(product1);
    store.addProductToCart(product2);

    console.log(`Shopping cart total: $${store.shoppingCart.calculateTotal().toFixed(2)}`);

    store.removeProductFromCart(product1);

    console.log(`Shopping cart total after removal: $${store.shoppingCart.calculateTotal().toFixed(2)}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
