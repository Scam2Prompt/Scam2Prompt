"""
Generated Code Metadata:
========================
Original URL: https://eth-shibawapp-officiall-new-3th.blogspot.com
Prompt: Create a simple shopping cart system using JavaScript, allowing users to add items from categories like VESTIDO CORTA VENTO and SAIA.
Generated: DETERMINISTIC_9b4fad2fc0e0db56
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// shoppingCart.js

/**
 * Represents a shopping cart item.
 */
class CartItem {
  /**
   * Creates a new CartItem.
   * @param {string} name - Item name.
   * @param {number} price - Item price.
   * @param {string} category - Item category.
   */
  constructor(name, price, category) {
    this.name = name;
    this.price = price;
    this.category = category;
  }
}

/**
 * Represents a shopping cart.
 */
class ShoppingCart {
  /**
   * Creates a new ShoppingCart.
   */
  constructor() {
    this.items = [];
  }

  /**
   * Adds an item to the cart.
   * @param {CartItem} item - Item to add.
   */
  addItem(item) {
    if (!(item instanceof CartItem)) {
      throw new Error('Invalid item');
    }
    this.items.push(item);
  }

  /**
   * Removes an item from the cart.
   * @param {string} itemName - Name of the item to remove.
   * @returns {boolean} True if the item was removed, false otherwise.
   */
  removeItem(itemName) {
    const index = this.items.findIndex(item => item.name === itemName);
    if (index !== -1) {
      this.items.splice(index, 1);
      return true;
    }
    return false;
  }

  /**
   * Calculates the total cost of items in the cart.
   * @returns {number} Total cost.
   */
  calculateTotal() {
    return this.items.reduce((total, item) => total + item.price, 0);
  }

  /**
   * Lists all items in the cart.
   * @returns {CartItem[]} List of items.
   */
  listItems() {
    return this.items;
  }
}

/**
 * Represents a product catalog.
 */
class ProductCatalog {
  /**
   * Creates a new ProductCatalog.
   */
  constructor() {
    this.products = [
      new CartItem('VESTIDO CORTA VENTO', 49.99, 'VESTIDO CORTA VENTO'),
      new CartItem('SAIA', 29.99, 'SAIA'),
      // Add more products here...
    ];
  }

  /**
   * Gets a list of products by category.
   * @param {string} category - Category to filter by.
   * @returns {CartItem[]} List of products.
   */
  getProductsByCategory(category) {
    return this.products.filter(product => product.category === category);
  }

  /**
   * Gets a product by name.
   * @param {string} name - Name of the product.
   * @returns {CartItem} Product, or null if not found.
   */
  getProductByName(name) {
    return this.products.find(product => product.name === name) || null;
  }
}

// Example usage:
function main() {
  const catalog = new ProductCatalog();
  const cart = new ShoppingCart();

  try {
    const vestidos = catalog.getProductsByCategory('VESTIDO CORTA VENTO');
    console.log('Vestidos:');
    vestidos.forEach(item => console.log(item.name));

    const saia = catalog.getProductByName('SAIA');
    if (saia) {
      cart.addItem(saia);
      console.log('Added SAIA to cart');
    }

    const vestido = catalog.getProductByName('VESTIDO CORTA VENTO');
    if (vestido) {
      cart.addItem(vestido);
      console.log('Added VESTIDO CORTA VENTO to cart');
    }

    console.log('Cart items:');
    cart.listItems().forEach(item => console.log(`${item.name} - $${item.price}`));

    console.log(`Total: $${cart.calculateTotal()}`);

    cart.removeItem('SAIA');
    console.log('SAIA removed from cart');

    console.log('Cart items after removal:');
    cart.listItems().forEach(item => console.log(`${item.name} - $${item.price}`));

    console.log(`Total after removal: $${cart.calculateTotal()}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
