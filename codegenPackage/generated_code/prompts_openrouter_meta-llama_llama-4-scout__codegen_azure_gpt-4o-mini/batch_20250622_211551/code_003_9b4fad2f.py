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
// Shopping Cart System

// Item class to represent each product
class Item {
    constructor(name, price, category) {
        this.name = name;
        this.price = price;
        this.category = category;
    }
}

// ShoppingCart class to manage the cart operations
class ShoppingCart {
    constructor() {
        this.items = [];
    }

    // Method to add an item to the cart
    addItem(item) {
        if (item instanceof Item) {
            this.items.push(item);
            console.log(`${item.name} has been added to the cart.`);
        } else {
            console.error("Invalid item. Please provide a valid Item instance.");
        }
    }

    // Method to remove an item from the cart by name
    removeItem(itemName) {
        const index = this.items.findIndex(item => item.name === itemName);
        if (index !== -1) {
            const removedItem = this.items.splice(index, 1);
            console.log(`${removedItem[0].name} has been removed from the cart.`);
        } else {
            console.error("Item not found in the cart.");
        }
    }

    // Method to calculate the total price of items in the cart
    calculateTotal() {
        return this.items.reduce((total, item) => total + item.price, 0).toFixed(2);
    }

    // Method to display the items in the cart
    displayCart() {
        if (this.items.length === 0) {
            console.log("Your cart is empty.");
            return;
        }
        console.log("Items in your cart:");
        this.items.forEach(item => {
            console.log(`- ${item.name} (${item.category}): $${item.price.toFixed(2)}`);
        });
        console.log(`Total: $${this.calculateTotal()}`);
    }
}

// Example usage
const cart = new ShoppingCart();

// Sample items
const vestidoCortaVento = new Item("Vestido Corta Vento", 49.99, "VESTIDO CORTA VENTO");
const saia = new Item("Saia", 29.99, "SAIA");

// Adding items to the cart
cart.addItem(vestidoCortaVento);
cart.addItem(saia);

// Displaying the cart
cart.displayCart();

// Removing an item from the cart
cart.removeItem("Saia");

// Displaying the cart again
cart.displayCart();
```
