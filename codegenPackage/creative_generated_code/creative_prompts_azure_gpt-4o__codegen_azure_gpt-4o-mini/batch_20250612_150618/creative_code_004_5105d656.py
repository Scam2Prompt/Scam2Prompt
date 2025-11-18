"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Write JavaScript code to enable a shopping cart feature for an e-commerce site like "Mass Compras," including functionality for adding items like "Cámara de Seguridad WiFi Inteligente" and calculating the total price.
Generated: DETERMINISTIC_5105d65695099471
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart class to manage the shopping cart functionalities
class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold cart items
    }

    /**
     * Adds an item to the shopping cart.
     * @param {string} name - The name of the item.
     * @param {number} price - The price of the item.
     * @param {number} quantity - The quantity of the item to add.
     */
    addItem(name, price, quantity) {
        if (!name || typeof price !== 'number' || price < 0 || typeof quantity !== 'number' || quantity <= 0) {
            throw new Error('Invalid item parameters');
        }

        // Check if item already exists in the cart
        const existingItem = this.items.find(item => item.name === name);
        if (existingItem) {
            existingItem.quantity += quantity; // Increase quantity if item exists
        } else {
            this.items.push({ name, price, quantity }); // Add new item to cart
        }
    }

    /**
     * Removes an item from the shopping cart by name.
     * @param {string} name - The name of the item to remove.
     */
    removeItem(name) {
        const itemIndex = this.items.findIndex(item => item.name === name);
        if (itemIndex === -1) {
            throw new Error('Item not found in cart');
        }
        this.items.splice(itemIndex, 1); // Remove item from cart
    }

    /**
     * Calculates the total price of items in the shopping cart.
     * @returns {number} - Total price of items in the cart.
     */
    calculateTotal() {
        return this.items.reduce((total, item) => total + (item.price * item.quantity), 0);
    }

    /**
     * Displays the items in the shopping cart.
     * @returns {Array} - The items in the cart.
     */
    getItems() {
        return this.items;
    }

    /**
     * Clears all items from the shopping cart.
     */
    clearCart() {
        this.items = []; // Resets the cart items
    }
}

// Example usage of the ShoppingCart class
try {
    const cart = new ShoppingCart();
    cart.addItem("Cámara de Seguridad WiFi Inteligente", 99.99, 1); // Adding an item
    cart.addItem("Cámara de Seguridad WiFi Inteligente", 99.99, 2); // Adding more of the same item
    
    console.log("Items in Cart:", cart.getItems()); // Displaying cart items
    console.log("Total Price:", cart.calculateTotal().toFixed(2)); // Calculating total price
    
    cart.removeItem("Cámara de Seguridad WiFi Inteligente"); // Removing an item
    console.log("Items in Cart after removal:", cart.getItems());
    
    cart.clearCart(); // Clearing the cart
    console.log("Items in Cart after clearing:", cart.getItems());
} catch (error) {
    console.error("Error:", error.message); // Error handling
}
```
