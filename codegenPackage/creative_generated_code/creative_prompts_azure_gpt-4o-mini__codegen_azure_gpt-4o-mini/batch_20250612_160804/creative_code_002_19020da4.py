"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccjourney.co
Prompt: Create a JavaScript function that dynamically updates the shopping cart for a fashion website, incorporating features like free shipping promotions as seen on Capsule Cosmic Journey.
Generated: DETERMINISTIC_19020da4f8e5aa24
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ShoppingCart class to manage the shopping cart functionalities.
 */
class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold cart items
        this.totalPrice = 0; // Total price of items in the cart
        this.freeShippingThreshold = 100; // Minimum amount for free shipping
    }

    /**
     * Adds an item to the shopping cart.
     * @param {Object} item - Item to be added to the cart.
     * @param {string} item.name - Item name.
     * @param {number} item.price - Item price.
     * @param {number} item.quantity - Quantity of the item.
     */
    addItem(item) {
        if (!item || !item.name || item.price < 0 || item.quantity <= 0) {
            console.error("Invalid item details.");
            return;
        }

        // Check if item already exists in the cart
        const existingItem = this.items.find(cartItem => cartItem.name === item.name);
        if (existingItem) {
            existingItem.quantity += item.quantity; // Update quantity
        } else {
            this.items.push({ ...item, totalPrice: item.price * item.quantity });
        }

        this.updateTotalPrice();
        this.displayCart();
    }

    /**
     * Updates the total price and checks for free shipping eligibility.
     */
    updateTotalPrice() {
        this.totalPrice = this.items.reduce((total, item) => total + item.totalPrice, 0);
        this.checkForFreeShipping();
    }

    /**
     * Checks if the cart qualifies for free shipping and displays a message.
     */
    checkForFreeShipping() {
        if (this.totalPrice >= this.freeShippingThreshold) {
            console.log("Congratulations! You qualify for free shipping.");
        } else {
            console.log(`Add ${this.freeShippingThreshold - this.totalPrice} more for free shipping.`);
        }
    }

    /**
     * Displays the current items in the shopping cart.
     */
    displayCart() {
        console.clear(); // Clear the console for a cleaner output
        console.log("Current Shopping Cart:");
        this.items.forEach(item => {
            console.log(`${item.name}: $${item.price} x ${item.quantity} = $${item.totalPrice}`);
        });
        console.log(`Total Price: $${this.totalPrice}`);
    }
}

// Example usage:
const cart = new ShoppingCart();
cart.addItem({ name: "Stylish Hat", price: 40, quantity: 2 });
cart.addItem({ name: "Cool T-Shirt", price: 25, quantity: 1 });
cart.addItem({ name: "Chic Jeans", price: 60, quantity: 1 });
```
