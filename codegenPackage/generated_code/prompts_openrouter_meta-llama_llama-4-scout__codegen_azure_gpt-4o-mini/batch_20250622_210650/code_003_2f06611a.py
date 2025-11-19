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
// This system manages door hardware and bath accessories inventory

class InventoryItem {
    constructor(name, quantity, price) {
        this.name = name; // Name of the item
        this.quantity = quantity; // Available quantity of the item
        this.price = price; // Price per item
    }

    // Method to update the quantity of the item
    updateQuantity(amount) {
        if (this.quantity + amount < 0) {
            throw new Error(`Insufficient stock for ${this.name}.`);
        }
        this.quantity += amount;
    }

    // Method to get the total value of the item in stock
    getTotalValue() {
        return this.quantity * this.price;
    }
}

class Inventory {
    constructor() {
        this.items = {}; // Object to hold inventory items
    }

    // Method to add a new item to the inventory
    addItem(name, quantity, price) {
        if (this.items[name]) {
            throw new Error(`Item ${name} already exists in the inventory.`);
        }
        this.items[name] = new InventoryItem(name, quantity, price);
    }

    // Method to update the quantity of an existing item
    updateItemQuantity(name, amount) {
        if (!this.items[name]) {
            throw new Error(`Item ${name} does not exist in the inventory.`);
        }
        this.items[name].updateQuantity(amount);
    }

    // Method to get the total inventory value
    getTotalInventoryValue() {
        return Object.values(this.items).reduce((total, item) => total + item.getTotalValue(), 0);
    }

    // Method to list all items in the inventory
    listItems() {
        return Object.values(this.items).map(item => ({
            name: item.name,
            quantity: item.quantity,
            price: item.price,
            totalValue: item.getTotalValue()
        }));
    }
}

// Example usage
try {
    const inventory = new Inventory();

    // Adding items to the inventory
    inventory.addItem('Door Handle', 50, 15.99);
    inventory.addItem('Bath Faucet', 30, 89.99);

    // Updating item quantities
    inventory.updateItemQuantity('Door Handle', -5); // Sold 5 door handles
    inventory.updateItemQuantity('Bath Faucet', 10); // Received 10 bath faucets

    // Listing all items
    console.log('Current Inventory:', inventory.listItems());

    // Getting total inventory value
    console.log('Total Inventory Value:', inventory.getTotalInventoryValue().toFixed(2));
} catch (error) {
    console.error('Error:', error.message);
}
```
