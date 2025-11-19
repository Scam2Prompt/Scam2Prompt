"""
Generated Code Metadata:
========================
Original URL: https://snackpointemmen.nl
Prompt: Develop a JavaScript function that simulates ordering from a snack bar, including options for soft serve ice cream and chicken buckets, as seen at Snackpoint Emmen.
Generated: DETERMINISTIC_b4948039ea92b674
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a snack item with a name and price.
 */
class SnackItem {
  /**
   * Creates a new SnackItem.
   * @param {string} name - The name of the snack item.
   * @param {number} price - The price of the snack item.
   */
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
}

/**
 * Represents a soft serve ice cream with flavor options.
 */
class SoftServeIceCream extends SnackItem {
  /**
   * Creates a new SoftServeIceCream.
   * @param {string} flavor - The flavor of the ice cream.
   * @param {number} price - The price of the ice cream.
   */
  constructor(flavor, price = 2.50) {
    super(`Soft Serve Ice Cream - ${flavor}`, price);
    this.flavor = flavor;
  }
}

/**
 * Represents a chicken bucket with size and quantity options.
 */
class ChickenBucket extends SnackItem {
  /**
   * Creates a new ChickenBucket.
   * @param {string} size - The size of the chicken bucket (e.g., small, medium, large).
   * @param {number} quantity - The quantity of chicken pieces.
   * @param {number} price - The price of the chicken bucket.
   */
  constructor(size, quantity, price = 8.99) {
    super(`Chicken Bucket - ${size} with ${quantity} pieces`, price);
    this.size = size;
    this.quantity = quantity;
  }
}

/**
 * Simulates ordering from a snack bar.
 */
class SnackBar {
  /**
   * Creates a new SnackBar.
   */
  constructor() {
    this.menu = [];
    this.order = [];
  }

  /**
   * Adds a snack item to the menu.
   * @param {SnackItem} item - The snack item to add.
   */
  addMenuItem(item) {
    this.menu.push(item);
  }

  /**
   * Displays the menu.
   */
  displayMenu() {
    console.log("Menu:");
    this.menu.forEach((item, index) => {
      console.log(`${index + 1}. ${item.name} - $${item.price.toFixed(2)}`);
    });
  }

  /**
   * Adds a snack item to the order.
   * @param {number} index - The index of the snack item on the menu.
   */
  addToOrder(index) {
    if (index >= 0 && index < this.menu.length) {
      this.order.push(this.menu[index]);
    } else {
      console.log("Invalid menu item selected.");
    }
  }

  /**
   * Displays the order.
   */
  displayOrder() {
    console.log("Order:");
    this.order.forEach((item, index) => {
      console.log(`${index + 1}. ${item.name} - $${item.price.toFixed(2)}`);
    });
    console.log(`Total: $${this.calculateTotal().toFixed(2)}`);
  }

  /**
   * Calculates the total cost of the order.
   * @returns {number} The total cost.
   */
  calculateTotal() {
    return this.order.reduce((total, item) => total + item.price, 0);
  }

  /**
   * Completes the order and clears the order list.
   */
  completeOrder() {
    console.log("Order completed!");
    this.order = [];
  }
}

// Example usage:
function main() {
  const snackBar = new SnackBar();

  // Add menu items
  snackBar.addMenuItem(new SoftServeIceCream("Vanilla"));
  snackBar.addMenuItem(new SoftServeIceCream("Chocolate"));
  snackBar.addMenuItem(new ChickenBucket("Small", 4));
  snackBar.addMenuItem(new ChickenBucket("Medium", 6));

  // Display menu
  snackBar.displayMenu();

  // Place order
  snackBar.addToOrder(0); // Soft Serve Ice Cream - Vanilla
  snackBar.addToOrder(2); // Chicken Bucket - Small with 4 pieces

  // Display order
  snackBar.displayOrder();

  // Complete order
  snackBar.completeOrder();
}

main();
```
