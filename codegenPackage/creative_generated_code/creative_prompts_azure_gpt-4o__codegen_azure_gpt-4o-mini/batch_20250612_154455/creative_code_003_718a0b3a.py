"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solandsol.com
Prompt: Write JavaScript code to implement a dynamic shopping cart system for Sol & Sol Pharmaceutical's online store, ensuring functionality for adding products, calculating totals, and checking out.
Generated: DETERMINISTIC_718a0b3aa8895a8c
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ShoppingCart.js

class ShoppingCart {
    constructor() {
        this.items = []; // Array to hold the items in the cart
    }

    /**
     * Adds a product to the shopping cart.
     * @param {Object} product - The product to add (should include id, name, price, and quantity).
     * @throws {Error} Throws an error if the product is invalid.
     */
    addProduct(product) {
        if (!product.id || !product.name || product.price < 0 || product.quantity <= 0) {
            throw new Error("Invalid product. Must contain id, name, price, and quantity.");
        }
        this.items.push(product);
    }

    /**
     * Calculates the total price of items in the cart.
     * @returns {number} The total price of all items in the cart.
     */
    calculateTotal() {
        return this.items.reduce((total, item) => total + (item.price * item.quantity), 0);
    }

    /**
     * Removes a product from the shopping cart by its id.
     * @param {string} productId - The id of the product to remove.
     * @throws {Error} Throws an error if the product does not exist in the cart.
     */
    removeProduct(productId) {
        const index = this.items.findIndex(item => item.id === productId);
        if (index === -1) {
            throw new Error("Product not found in cart.");
        }
        this.items.splice(index, 1);
    }

    /**
     * Clears all items from the shopping cart.
     */
    clearCart() {
        this.items = [];
    }

    /**
     * Checks out the shopping cart and returns the order summary.
     * @returns {Object} Summary of the order including total price and items.
     */
    checkout() {
        if (this.items.length === 0) {
            throw new Error("Cannot checkout: Cart is empty.");
        }

        const total = this.calculateTotal();
        const orderSummary = {
            items: this.items,
            total: total,
            date: new Date().toISOString(),
        };

        // Clear the cart after checkout
        this.clearCart();
        return orderSummary;
    }
}

// Example usage:
// const cart = new ShoppingCart();
// cart.addProduct({ id: '1', name: 'Aspirin', price: 10.99, quantity: 2 });
// cart.addProduct({ id: '2', name: 'Ibuprofen', price: 8.99, quantity: 1 });
// console.log(cart.calculateTotal()); // Should log the total price
// console.log(cart.checkout()); // Should log the order summary
```

This code represents a simple and dynamic shopping cart system, encapsulated in a class that provides methods to add, remove, calculate totals, and checkout. Each method includes error handling as necessary to ensure the cart's integrity.
