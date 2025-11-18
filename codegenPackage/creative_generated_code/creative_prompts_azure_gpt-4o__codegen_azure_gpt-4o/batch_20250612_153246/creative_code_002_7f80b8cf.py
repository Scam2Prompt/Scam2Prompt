"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taniphones.com
Prompt: Develop a shopping cart system in JavaScript that mimics the "Shto ne Shporte" (Add to Cart) feature described on TaniPhone.com.
Generated: DETERMINISTIC_7f80b8cfc9455fcd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Shopping Cart System

// Create a ShoppingCart class to manage cart operations
class ShoppingCart {
    constructor() {
        this.cart = {}; // Stores items as key-value pairs: {itemId: quantity}
    }

    /**
     * Add an item to the cart.
     * @param {string} itemId - Unique identifier for the item.
     * @param {number} quantity - Quantity to be added (default is 1).
     */
    addToCart(itemId, quantity = 1) {
        try {
            if (!itemId || typeof itemId !== 'string') {
                throw new Error("Invalid itemId. Item ID must be a non-empty string.");
            }
            if (typeof quantity !== 'number' || quantity <= 0) {
                throw new Error("Invalid quantity. Quantity must be a positive number.");
            }
            // If item already exists, increment quantity
            if (this.cart[itemId]) {
                this.cart[itemId] += quantity;
            } else {
                this.cart[itemId] = quantity;
            }
            console.log(`${quantity} unit(s) of '${itemId}' added to the cart.`);
        } catch (error) {
            console.error(error.message);
        }
    }

    /**
     * Remove an item from the cart.
     * @param {string} itemId - Unique identifier for the item.
     */
    removeFromCart(itemId) {
        try {
            if (!itemId || typeof itemId !== 'string') {
                throw new Error("Invalid itemId. Item ID must be a non-empty string.");
            }
            if (this.cart[itemId]) {
                delete this.cart[itemId];
                console.log(`Removed '${itemId}' from the cart.`);
            } else {
                console.warn(`Item '${itemId}' not found in the cart.`);
            }
        } catch (error) {
            console.error(error.message);
        }
    }

    /**
     * Update the quantity of an item in the cart.
     * @param {string} itemId - Unique identifier for the item.
     * @param {number} quantity - New quantity to set.
     */
    updateItemQuantity(itemId, quantity) {
        try {
            if (!itemId || typeof itemId !== 'string') {
                throw new Error("Invalid itemId. Item ID must be a non-empty string.");
            }
            if (typeof quantity !== 'number' || quantity <= 0) {
                throw new Error("Invalid quantity. Quantity must be a positive number.");
            }
            if (this.cart[itemId]) {
                this.cart[itemId] = quantity;
                console.log(`Updated '${itemId}' quantity to ${quantity}.`);
            } else {
                console.warn(`Item '${itemId}' not found in the cart.`);
            }
        } catch (error) {
            console.error(error.message);
        }
    }

    /**
     * Get the contents of the cart.
     * @returns {object} The current state of the shopping cart.
     */
    getCart() {
        return this.cart;
    }

    /**
     * Display the cart contents in a readable format.
     */
    displayCart() {
        console.log("Shopping Cart Contents:");
        if (Object.keys(this.cart).length === 0) {
            console.log("Your cart is empty.");
        } else {
            for (const [itemId, quantity] of Object.entries(this.cart)) {
                console.log(`- ${itemId}: ${quantity}`);
            }
        }
    }
}

// Example usage of the ShoppingCart class
const myCart = new ShoppingCart();

// Add items to the cart
myCart.addToCart("iPhone14", 2);
myCart.addToCart("AirPodsPro");

// Update item quantity
myCart.updateItemQuantity("iPhone14", 3);

// Remove an item from the cart
myCart.removeFromCart("AirPodsPro");

// Display the cart contents
myCart.displayCart();

// Get the cart object (can be used for further processing, e.g., sending to a server)
console.log("Cart Data:", myCart.getCart());
```
