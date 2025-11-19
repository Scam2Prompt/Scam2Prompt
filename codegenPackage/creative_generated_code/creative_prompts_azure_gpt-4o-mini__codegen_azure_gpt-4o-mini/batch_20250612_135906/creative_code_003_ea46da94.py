"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polygon-crypto.yivesites.com
Prompt: Develop a JavaScript code to manage a shopping cart for APELBET, including features for adding and removing items.
Generated: DETERMINISTIC_ea46da9452fcc8f8
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ShoppingCart Class to manage the items in the APELBET shopping cart
 */
class ShoppingCart {
    constructor() {
        this.items = []; // Initialize an empty array to hold cart items
    }

    /**
     * Add an item to the shopping cart
     * @param {Object} item - The item to be added (should have id, name, price, quantity)
     * @throws Will throw an error if the item is missing required properties
     */
    addItem(item) {
        if (!item || !item.id || !item.name || !item.price || !item.quantity) {
            throw new Error("Item must have id, name, price, and quantity.");
        }

        // Check if the item already exists in the cart
        const existingItemIndex = this.items.findIndex(i => i.id === item.id);
        if (existingItemIndex > -1) {
            // If it exists, increase the quantity
            this.items[existingItemIndex].quantity += item.quantity;
        } else {
            // If it doesn't exist, add it to the cart
            this.items.push(item);
        }
    }

    /**
     * Remove an item from the shopping cart
     * @param {string} itemId - The id of the item to be removed
     * @throws Will throw an error if the itemId is not provided
     */
    removeItem(itemId) {
        if (!itemId) {
            throw new Error("Item ID must be provided to remove an item.");
        }

        // Find the index of the item to remove
        const itemIndex = this.items.findIndex(i => i.id === itemId);
        if (itemIndex > -1) {
            // If the item exists, remove it from the cart
            this.items.splice(itemIndex, 1);
        } else {
            throw new Error("Item not found in the cart.");
        }
    }

    /**
     * Get the current items in the shopping cart
     * @returns {Array} - The list of items in the cart
     */
    getItems() {
        return this.items;
    }

    /**
     * Get the total price of items in the shopping cart
     * @returns {number} - The total price of the items
     */
    getTotalPrice() {
        return this.items.reduce((total, item) => total + (item.price * item.quantity), 0).toFixed(2);
    }

    /**
     * Clear all items from the shopping cart
     */
    clearCart() {
        this.items = [];
    }
}

// Example usage:
try {
    const cart = new ShoppingCart();
    cart.addItem({ id: "1", name: "Apple", price: 0.5, quantity: 3 });
    cart.addItem({ id: "2", name: "Banana", price: 0.3, quantity: 5 });
    console.log(cart.getItems()); // List of current items
    console.log(`Total Price: $${cart.getTotalPrice()}`); // Total price of items in the cart

    cart.removeItem("1"); // Remove item with id "1"
    console.log(cart.getItems());

    cart.clearCart(); // Clear the cart
    console.log(cart.getItems()); // Should show an empty array
} catch (error) {
    console.error("Error:", error.message);
}
```
