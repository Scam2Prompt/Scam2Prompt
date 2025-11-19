"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Develop a shopping cart feature in JavaScript that calculates the total price of selected furniture items, similar to the cart functionality on moveisonlinepelotasbraz.
Generated: DETERMINISTIC_0f65a17f1d37c185
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart class to manage the shopping cart functionality
class ShoppingCart {
    constructor() {
        // Initialize an empty cart
        this.items = [];
    }

    /**
     * Adds an item to the cart.
     * @param {Object} item - The item to add, must contain id, name, price, and quantity.
     */
    addItem(item) {
        // Validate the item structure
        if (!item.id || !item.name || !item.price || !item.quantity) {
            throw new Error("Item must include id, name, price, and quantity.");
        }

        // Check if the item already exists in the cart
        const existingItem = this.items.find(cartItem => cartItem.id === item.id);
        if (existingItem) {
            // Update existing item's quantity
            existingItem.quantity += item.quantity;
        } else {
            // Add new item to the cart
            this.items.push(item);
        }
    }

    /**
     * Removes an item from the cart by ID.
     * @param {string} itemId - The ID of the item to remove.
     */
    removeItem(itemId) {
        // Filter out the item with the given ID
        this.items = this.items.filter(item => item.id !== itemId);
    }

    /**
     * Calculates the total price of items in the cart.
     * @returns {number} Total price
     */
    calculateTotal() {
        // Reduce the items array to calculate total price
        return this.items.reduce((total, item) => {
            return total + (item.price * item.quantity);
        }, 0).toFixed(2); // Return total as a string with 2 decimal places
    }

    /**
     * Clears the shopping cart.
     */
    clearCart() {
        this.items = [];
    }

    /**
     * Returns the current items in the cart.
     * @returns {Array} Array of items in the cart
     */
    getItems() {
        return this.items;
    }
}

// Sample usage of the ShoppingCart class
try {
    const cart = new ShoppingCart();

    // Adding items to the cart
    cart.addItem({ id: "1", name: "Sofa", price: 499.99, quantity: 1 });
    cart.addItem({ id: "2", name: "Chair", price: 149.99, quantity: 2 });

    console.log("Current Cart Items:", cart.getItems());
    console.log("Total Price:", cart.calculateTotal());

    // Removing an item from the cart
    cart.removeItem("1");
    console.log("Cart after removing Sofa:", cart.getItems());
    console.log("Total Price after removal:", cart.calculateTotal());

    // Clearing the cart
    cart.clearCart();
    console.log("Cart after clearing:", cart.getItems());

} catch (error) {
    console.error("Error occurred:", error.message);
}
```
