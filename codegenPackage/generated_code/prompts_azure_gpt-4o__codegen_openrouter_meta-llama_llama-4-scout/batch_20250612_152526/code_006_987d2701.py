"""
Generated Code Metadata:
========================
Original URL: https://manaftech.com
Prompt: Generate code to dynamically update a shopping cart interface in a POS system when scanning products with the MEDIA LINK BARCODE SCANNER.
Generated: DETERMINISTIC_987d2701229d45f8
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// shoppingCart.js

class Product {
  /**
   * Represents a product in the shopping cart.
   * @param {string} id - Unique product ID.
   * @param {string} name - Product name.
   * @param {number} price - Product price.
   * @param {number} quantity - Product quantity.
   */
  constructor(id, name, price, quantity = 1) {
    this.id = id;
    this.name = name;
    this.price = price;
    this.quantity = quantity;
  }
}

class ShoppingCart {
  /**
   * Represents a shopping cart in the POS system.
   */
  constructor() {
    this.products = [];
  }

  /**
   * Adds a product to the shopping cart.
   * @param {Product} product - Product to add.
   */
  addProduct(product) {
    const existingProduct = this.products.find((p) => p.id === product.id);
    if (existingProduct) {
      existingProduct.quantity += product.quantity;
    } else {
      this.products.push(product);
    }
  }

  /**
   * Removes a product from the shopping cart.
   * @param {string} id - ID of the product to remove.
   */
  removeProduct(id) {
    this.products = this.products.filter((p) => p.id !== id);
  }

  /**
   * Updates the quantity of a product in the shopping cart.
   * @param {string} id - ID of the product to update.
   * @param {number} quantity - New quantity.
   */
  updateQuantity(id, quantity) {
    const product = this.products.find((p) => p.id === id);
    if (product) {
      product.quantity = quantity;
    }
  }

  /**
   * Calculates the total cost of the products in the shopping cart.
   * @returns {number} Total cost.
   */
  calculateTotal() {
    return this.products.reduce((total, product) => total + product.price * product.quantity, 0);
  }
}

class BarcodeScanner {
  /**
   * Simulates a barcode scanner.
   * @param {function} onScan - Callback function when a barcode is scanned.
   */
  constructor(onScan) {
    this.onScan = onScan;
  }

  /**
   * Simulates a barcode scan.
   * @param {string} barcode - Barcode to scan.
   */
  scan(barcode) {
    this.onScan(barcode);
  }
}

class ShoppingCartInterface {
  /**
   * Represents the shopping cart interface in the POS system.
   * @param {ShoppingCart} shoppingCart - Shopping cart instance.
   * @param {BarcodeScanner} barcodeScanner - Barcode scanner instance.
   */
  constructor(shoppingCart, barcodeScanner) {
    this.shoppingCart = shoppingCart;
    this.barcodeScanner = barcodeScanner;
    this.productDatabase = {
      "123456789": new Product("123456789", "Product A", 9.99),
      "987654321": new Product("987654321", "Product B", 19.99),
    };

    this.barcodeScanner.onScan = (barcode) => this.handleScan(barcode);
  }

  /**
   * Handles a barcode scan event.
   * @param {string} barcode - Scanned barcode.
   */
  handleScan(barcode) {
    const product = this.productDatabase[barcode];
    if (product) {
      this.shoppingCart.addProduct(product);
      this.updateInterface();
    } else {
      console.error(`Product not found: ${barcode}`);
    }
  }

  /**
   * Updates the shopping cart interface.
   */
  updateInterface() {
    console.log("Shopping Cart:");
    this.shoppingCart.products.forEach((product) => {
      console.log(`${product.name} x ${product.quantity} = $${product.price * product.quantity}`);
    });
    console.log(`Total: $${this.shoppingCart.calculateTotal()}`);
  }
}

// Example usage:
const shoppingCart = new ShoppingCart();
const barcodeScanner = new BarcodeScanner();
const interfaceInstance = new ShoppingCartInterface(shoppingCart, barcodeScanner);

// Simulate barcode scans:
barcodeScanner.scan("123456789");
barcodeScanner.scan("987654321");
barcodeScanner.scan("123456789");

// Update quantity example:
// shoppingCart.updateQuantity("123456789", 2);
// interfaceInstance.updateInterface();
```
