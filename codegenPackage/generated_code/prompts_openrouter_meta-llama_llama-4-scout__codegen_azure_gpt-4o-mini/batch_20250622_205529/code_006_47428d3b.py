"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Generate a JavaScript code to implement a shopping cart functionality for a website like Jurunense Home Center."
Generated: DETERMINISTIC_47428d3b7a01e1b5
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ShoppingCart class to manage the shopping cart functionality
class ShoppingCart {
    constructor() {
        // Initialize an empty cart
        this.cart = [];
    }

    // Add an item to the cart
    addItem(item) {
        // Validate item
        if (!item || !item.id || !item.name || item.price <= 0) {
            throw new Error("Invalid item. Item must have an id, name, and a positive price.");
        }

        // Check if the item already exists in the cart
        const existingItem = this.cart.find(cartItem => cartItem.id === item.id);
        if (existingItem) {
            // If it exists, increase the quantity
            existingItem.quantity += 1;
        } else {
            // If it doesn't exist, add it to the cart with quantity 1
            this.cart.push({ ...item, quantity: 1 });
        }
        console.log(`${item.name} added to the cart.`);
    }

    // Remove an item from the cart
    removeItem(itemId) {
        // Validate itemId
        if (!itemId) {
            throw new Error("Invalid item ID.");
        }

        // Find the index of the item to remove
        const itemIndex = this.cart.findIndex(cartItem => cartItem.id === itemId);
        if (itemIndex > -1) {
            // Remove the item from the cart
            const removedItem = this.cart.splice(itemIndex, 1);
            console.log(`${removedItem[0].name} removed from the cart.`);
        } else {
            console.log("Item not found in the cart.");
        }
    }

    // Get the total price of items in the cart
    getTotal() {
        return this.cart.reduce((total, item) => total + (item.price * item.quantity), 0).toFixed(2);
    }

    // Get the list of items in the cart
    getItems() {
        return this.cart;
    }

    // Clear the cart
    clearCart() {
        this.cart = [];
        console.log("Cart has been cleared.");
    }
}

// Example usage
try {
    const cart = new ShoppingCart();

    // Adding items to the cart
    cart.addItem({ id: 1, name: "Hammer", price: 9.99 });
    cart.addItem({ id: 2, name: "Nails", price: 4.99 });
    cart.addItem({ id: 1, name: "Hammer", price: 9.99 }); // Adding Hammer again

    // Display cart items and total
    console.log("Cart Items:", cart.getItems());
    console.log("Total Price: $", cart.getTotal());

    // Removing an item
    cart.removeItem(1);
    console.log("Cart Items after removal:", cart.getItems());

    // Clearing the cart
    cart.clearCart();
    console.log("Cart Items after clearing:", cart.getItems());
} catch (error) {
    console.error("Error:", error.message);
}
```
