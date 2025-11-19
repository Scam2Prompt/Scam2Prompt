"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Create a JavaScript code snippet to implement a simple inventory management system for a rolling store that delivers door hardware and bath accessories to job sites.
Generated: DETERMINISTIC_2f06611af2f16240
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Inventory Management System for a Rolling Store
// This system manages door hardware and bath accessories inventory and allows adding, removing, and checking stock levels.

class InventoryManagement {
  constructor() {
    // Initialize inventory as an empty object
    this.inventory = {};
  }

  /**
   * Adds a new item to the inventory or updates the quantity if the item already exists.
   * @param {string} itemName - Name of the item.
   * @param {number} quantity - Quantity to add.
   */
  addItem(itemName, quantity) {
    if (!itemName || typeof itemName !== 'string') {
      throw new Error('Invalid item name.');
    }
    if (!quantity || typeof quantity !== 'number' || quantity <= 0) {
      throw new Error('Invalid quantity. Must be a positive number.');
    }

    if (this.inventory[itemName]) {
      this.inventory[itemName] += quantity; // Update quantity if item exists
    } else {
      this.inventory[itemName] = quantity; // Add new item
    }
    console.log(`${quantity} units of "${itemName}" added to inventory.`);
  }

  /**
   * Removes a specified quantity of an item from the inventory.
   * @param {string} itemName - Name of the item.
   * @param {number} quantity - Quantity to remove.
   */
  removeItem(itemName, quantity) {
    if (!itemName || typeof itemName !== 'string') {
      throw new Error('Invalid item name.');
    }
    if (!quantity || typeof quantity !== 'number' || quantity <= 0) {
      throw new Error('Invalid quantity. Must be a positive number.');
    }

    if (!this.inventory[itemName]) {
      throw new Error(`Item "${itemName}" does not exist in inventory.`);
    }

    if (this.inventory[itemName] < quantity) {
      throw new Error(`Insufficient stock of "${itemName}". Available: ${this.inventory[itemName]}`);
    }

    this.inventory[itemName] -= quantity; // Deduct quantity
    console.log(`${quantity} units of "${itemName}" removed from inventory.`);
  }

  /**
   * Checks the stock level of a specific item.
   * @param {string} itemName - Name of the item.
   * @returns {number} - Quantity of the item in stock.
   */
  checkStock(itemName) {
    if (!itemName || typeof itemName !== 'string') {
      throw new Error('Invalid item name.');
    }

    if (!this.inventory[itemName]) {
      console.log(`Item "${itemName}" is not in inventory.`);
      return 0;
    }

    console.log(`Stock level of "${itemName}": ${this.inventory[itemName]}`);
    return this.inventory[itemName];
  }

  /**
   * Displays the entire inventory.
   */
  displayInventory() {
    console.log('Current Inventory:');
    if (Object.keys(this.inventory).length === 0) {
      console.log('Inventory is empty.');
    } else {
      for (const [itemName, quantity] of Object.entries(this.inventory)) {
        console.log(`- ${itemName}: ${quantity} units`);
      }
    }
  }
}

// Example usage
try {
  const storeInventory = new InventoryManagement();

  storeInventory.addItem('Door Handle', 50);
  storeInventory.addItem('Bath Towel Rack', 30);
  storeInventory.addItem('Door Lock', 20);

  storeInventory.displayInventory();

  storeInventory.removeItem('Door Handle', 10);
  storeInventory.checkStock('Door Handle');

  storeInventory.removeItem('Bath Towel Rack', 5);
  storeInventory.checkStock('Bath Towel Rack');

  storeInventory.displayInventory();
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
